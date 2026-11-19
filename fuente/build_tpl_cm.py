import re, pprint
P='/tmp/claude-0/w/cm/pag/'; M='/tmp/claude-0/w/cm/med/'
def parts(f):
    c=open(f).read().replace('\r\n','\n')
    hs=c.find('<link rel="stylesheet"')
    he=c.find('<script type="application/ld+json">')
    if not (0<he<c.find('</head>')): he=c.find('</head>')
    head=c[hs:he].strip()
    i=c.find('<body>')+len('<body>'); j=c.find('<main')
    cab=c[i:j].strip()
    k=c.rfind('<footer'); pie=c[k:].replace('</body></html>','').replace('</body>\n</html>','').strip()
    return head,cab,pie
def norm(s, lang, alt):
    s=s.replace(alt,'{ALT}')
    if lang=='es':
        s=re.sub(r'(href|src)="\.\./assets/', r'\1="{I}assets/', s)
        s=re.sub(r'(href|action|data-raiz)="\.\./', r'\1="{R}', s)
    else:
        s=s.replace('"../../assets/','"{I}assets/')
        s=re.sub(r'(href|action|data-raiz)="\.\./(?!\.\.)', r'\1="{R}', s)
    return s
out={}
cfg=[('cinematopedia', P+'cine-p_lo-que-el-viento-se-llevo-1939.html', P+'cine-en_p_casablanca-1942.html', '../en/p/lo-que-el-viento-se-llevo-1939.html','../../p/casablanca-1942.html'),
     ('medicapedia', M+'p_edward-jenner.html', P+'med-en_p_edward-jenner.html','../en/p/edward-jenner.html','../../p/edward-jenner.html')]
for site,es,en,altes,alten in cfg:
    d={'head':{}, 'cab':{}, 'pie':{}}
    for lang,f,alt in (('es',es,altes),('en',en,alten)):
        h,cb,p=parts(f)
        if site=='medicapedia':
            # el blog no tiene versión catalana: quitamos el enlace CA
            cb=re.sub(r'<a href="[^"]*ca/p/edward-jenner\.html"[^>]*>CA</a>','',cb)
        h,cb,p=[norm(x,lang,alt) for x in (h,cb,p)]
        h=re.sub(r'\?v=[0-9a-z]+','',h) if False else h
        blog='<a class="menu-blog" href="./">Blog</a>'
        assert cb.count('</nav>')==1
        cb=cb.replace('</nav>', blog+'</nav>',1)
        for x in (h,cb,p): assert '../' not in x, (site,lang,re.findall(r'.{40}\.\./.{40}',x)[:3])
        assert '{ALT}' in cb, (site,lang)
        d['head'][lang]=h; d['cab'][lang]=cb; d['pie'][lang]=p
    out[site]=d
open('/tmp/claude-0/w/blogs/plantillas_cm.py','w').write('# Plantillas copiadas de páginas reales de Cinematopedia y Medicapedia (19-11-2026)\nPLANT = '+pprint.pformat(out,width=200)+'\n')
for s in out:
    for l in ('es','en'): print(s,l,'\n HEAD',out[s]['head'][l][:300],'\n CAB',out[s]['cab'][l][-700:],'\n')
