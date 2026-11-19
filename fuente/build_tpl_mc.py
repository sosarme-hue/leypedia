import re, pprint
P='/tmp/claude-0/w/mc/pag/'
def parts(f):
    c=open(f).read()
    head=c[c.find('<link rel="preconnect"'):c.find('</head>')].strip()
    cab=c[c.find('<body>')+6:c.find('<main')].strip()
    pie=c[c.rfind('<footer'):c.rfind('</body>')].strip()
    return head,cab,pie
d={'head':{},'cab':{},'pie':{}}
for lang,f in (('es','myth-dioses.html'),('en','myth-en-dioses.html')):
    out=[]
    for s in parts(P+f):
        if lang=='es':
            s=s.replace('href="en/dioses.html"','href="{ALT}"')
            s=re.sub(r'(href|src)="assets/', r'\1="{I}assets/', s)
            s=re.sub(r'href="(?!https?:|\{|#)([a-z\-]+\.html)"', r'href="{R}\1"', s)
        else:
            s=s.replace('href="../dioses.html"','href="{ALT}"')
            s=re.sub(r'(href|src)="\.\./assets/', r'\1="{I}assets/', s)
            s=s.replace('href="../en/','href="{R}')
        assert '../' not in s and not re.search(r'href="(?!https?:)[a-z]',s), (lang, re.findall(r'href="[a-z.][^"]*"',s)[:5])
        out.append(s)
    h,cb,p=out
    assert cb.count('</nav>')==1
    cb=cb.replace('</nav>','<a class="menu-blog" href="./" aria-current="page">Blog</a></nav>',1)
    d['head'][lang]=h; d['cab'][lang]=cb; d['pie'][lang]=p
open('/tmp/claude-0/w/blogs/plantillas_mc.py','w').write('# Generado por build_tpl_mc.py\nPLANT = '+pprint.pformat({'mythicapedia':d},width=200)+'\n')
print('ok')
