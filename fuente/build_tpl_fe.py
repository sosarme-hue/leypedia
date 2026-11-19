import re, pprint
P='/tmp/claude-0/w/fe/pag/'
out={}
# Filopedia
def fparts(f):
    c=open(f).read().replace('\r\n','\n')
    hs=c.find('<link rel="stylesheet"'); he=c.find('<script type="application/ld+json">')
    head=c[hs:he].strip()+'\n'+c[c.find('<link rel="icon"'):c.find('</head>')].strip()
    cab=c[c.find('<body>')+6:c.find('<main')].strip()
    pie=c[c.rfind('<footer'):c.rfind('</body>')].strip()
    return head,cab,pie
def norm(s, lang, alt):
    s=s.replace(alt,'{ALT}')
    if lang=='es':
        s=re.sub(r'(href|src)="\.\./assets/', r'\1="{I}assets/', s)
        s=re.sub(r'(href|action|data-raiz|data-ra)="\.\./', r'\1="{R}', s)
    else:
        s=s.replace('"../../assets/','"{I}assets/').replace('data-ra="../../"','data-ra="{I}"')
        s=re.sub(r'(href|action|data-raiz)="\.\./(?!\.\.)', r'\1="{R}', s)
    return s
d={'head':{}, 'cab':{}, 'pie':{}}
for lang,f,alt in (('es',P+'filo-a_socrates.html','../en/a/socrates.html'),('en',P+'filo-en_a_socrates.html','../../a/socrates.html')):
    h,cb,p=[norm(x,lang,alt) for x in fparts(f)]
    assert cb.count('</nav>')==1
    cb=cb.replace('</nav>','<a class="menu-blog" href="./">Blog</a></nav>',1)
    for x in (h,cb,p): assert '../' not in x, (lang,re.findall(r'.{40}\.\./.{40}',x)[:3])
    assert '{ALT}' in cb
    d['head'][lang]=h; d['cab'][lang]=cb; d['pie'][lang]=p
out['filopedia']=d
# Enfermería (solo ES, páginas en carpetas; blog/ tiene profundidad 1 como novedades/)
c=open('/tmp/claude-0/w/enf-repo/novedades/index.html').read()
h=c[c.find('<link rel="icon"'):c.find('</head>')].strip()
cb=c[c.find('<body>')+6:c.find('<main')].strip()
p=c[c.rfind('<footer'):c.rfind('</body>')].strip()
def en(s):
    s=re.sub(r'(href|src)="\.\./assets/', r'\1="{I}assets/', s)
    return re.sub(r'(href|action)="\.\./', r'\1="{R}', s)
h,cb,p=en(h),en(cb),en(p)
assert cb.count('</nav>')==1
cb=cb.replace('</nav>','<a href="./" aria-current="page">Blog</a></nav>',1)
for x in (h,cb,p): assert '../' not in x
d={'head':{'es':h,'en':h},'cab':{'es':cb,'en':cb},'pie':{'es':p,'en':p}}
out['enfermeria']=d
open('/tmp/claude-0/w/blogs/plantillas_fe.py','w').write('# Plantillas copiadas de páginas reales de Filopedia y enfermeria.si (19-11-2026)\nPLANT = '+pprint.pformat(out,width=200)+'\n')
print(out['filopedia']['cab']['en'][-900:]); print(out['enfermeria']['cab']['es'][-1200:-500])
