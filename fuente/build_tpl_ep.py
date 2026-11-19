import re, pprint
EP='/tmp/claude-0/w/ep/'
out={}
# Planetpedia: blog/ (profundidad 1) y en/blog/ (profundidad 2); los enlaces van siempre a la raíz física ({I})
d={'head':{}, 'cab':{}, 'pie':{}, 'body':{}}
for lang,f,alt in (('es',EP+'planetpedia/tierra/index.html','../en/earth/'),('en',EP+'planetpedia/en/earth/index.html','../../tierra/')):
    c=open(f).read()
    h=c[c.find('<link rel="preconnect"'):c.find('<script type="application/ld+json">')].strip()
    body=re.search(r'<body([^>]*)>',c).group(1)
    cb=c[c.find('<header class="top">'):c.find('</header>')+9]
    p=c[c.rfind('<footer'):c.rfind('</body>')].strip()
    cb=cb.replace(f'href="{alt}"','href="{ALT}"')
    up='../' if lang=='es' else '../../'
    def n(s): return s.replace(f'"{up}','"{I}')
    h,cb,p,body=n(h),n(cb),n(p),n(body)
    cb=cb.replace('<a class="idioma"','<a class="idioma" href="./">Blog</a>\n    <a class="idioma"',1).replace('<a class="idioma" href="./">Blog</a>','<a class="idioma menu-blog" href="./">Blog</a>',1)
    for x in (h,cb,p,body): assert '../' not in x, (lang,x[:200])
    assert '{ALT}' in cb
    d['head'][lang]=h; d['cab'][lang]=cb; d['pie'][lang]=p; d['body'][lang]=body
out['planetpedia']=d
# Escolapedia: solo ES; la web publicada es dist/; blog/ con profundidad 1, como eso/
c=open(EP+'escolapedia/dist/eso/index.html').read()
h=c[c.find('<link rel="preconnect"'):c.find('</head>')].strip()
cb=c[c.find('<body>')+6:c.find('<main')].strip()
p=c[c.rfind('<footer'):c.rfind('</body>')].strip()
def n(s):
    s=re.sub(r'(href|src)="\.\./assets/', r'\1="{I}assets/', s)
    s=re.sub(r'(href)="\.\./', r'\1="{R}', s)
    return s.replace('window.BASE="../"','window.BASE="{R}"')
h,cb,p=n(h),n(cb),n(p)
cb=cb.replace('</nav>','  <a href="./" aria-current="page">Blog</a>\n  </nav>',1)
for x in (h,cb,p): assert '../' not in x, x[:300]
out['escolapedia']={'head':{'es':h,'en':h},'cab':{'es':cb,'en':cb},'pie':{'es':p,'en':p}}
open('/tmp/claude-0/w/blogs/plantillas_ep.py','w').write('# Plantillas copiadas de páginas reales de Planetpedia y Escolapedia (19-11-2026)\nPLANT = '+pprint.pformat(out,width=200)+'\n')
print(out['planetpedia']['cab']['en'][-700:]); print(out['planetpedia']['body']); print(out['escolapedia']['pie']['es'][-200:])
