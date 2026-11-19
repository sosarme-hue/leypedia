import re, pprint
P='/tmp/claude-0/w/mc/pag/'
d={'head':{},'cab':{},'pie':{}}
for lang,f,ca in (('es','cel-es-masias.txt','/ca/masies-i-finques/'),('en','cel-en-farm.txt','/ca/masies-i-finques/')):
    c=open(P+f).read()
    head=c[c.find('<link rel="icon"'):c.find('</head>')].strip()
    cab=c[c.find('<header>'):c.find('</header>')+9]
    pie=c[c.rfind('<footer>'):]
    pie=pie[:pie.find('</footer>')+9]+'\n<script src="/estatico/sitio.js?v=mw8dg1qx" defer></script>'
    assert 'CLAVE' not in head+cab+pie and 'correo@' not in head+cab+pie and 'TEL' not in head+cab+pie
    if lang=='es':
        cab=cab.replace('<a href="/en/farmhouses-and-estates/" hreflang="en">EN</a>','<a href="{ALT_en}" hreflang="en">EN</a>').replace(ca,'{ALT_ca}')
        cab=cab.replace('</nav>','<a href="/es/blog/" aria-current="page">Blog</a></nav>',1)
    else:
        cab=cab.replace('<a href="/es/masias-y-fincas/" hreflang="es">ES</a>','<a href="{ALT_es}" hreflang="es">ES</a>').replace(ca,'{ALT_ca}')
        cab=cab.replace('</nav>','<a href="/en/blog/" aria-current="page">Blog</a></nav>',1)
    assert cab.count('{ALT_')==2 and cab.count('Blog</a>')==1
    d['head'][lang]=head; d['cab'][lang]=cab; d['pie'][lang]=pie
# catalán: cabecera y pie de ca/index.html (extraer.php), misma cabecera <head>
cab, pie = open(P+'cel-ca-partes.txt').read().split('<!-- PIE -->')
cab = cab.strip().replace('<a href="/es/" hreflang="es">', '<a href="{ALT_es}" hreflang="es">').replace('<a href="/en/" hreflang="en">', '<a href="{ALT_en}" hreflang="en">')
cab = cab.replace('</nav>', '<a href="/ca/blog/" aria-current="page">Blog</a></nav>', 1)
assert cab.count('{ALT_') == 2 and cab.count('Blog</a>') == 1
d['head']['ca'] = d['head']['es']
d['cab']['ca'] = cab; d['pie']['ca'] = pie.strip() + '\n<script src="/estatico/sitio.js?v=mw8dg1qx" defer></script>'
open('/tmp/claude-0/w/blogs/plantillas_cel.py','w').write('# Generado por build_tpl_cel.py\nPLANT = '+pprint.pformat({'celebraciones':d},width=200)+'\n')
print(d['cab']['en']); print(d['head']['es'])
