"""Vista previa: copia el payload y convierte las rutas a la web real en absolutas (CSS e imágenes cargan de la web)."""
import re, shutil, sys, json, os
from pathlib import Path
from urllib.parse import urljoin
BASE = Path(__file__).parent
SITIOS_V = sys.argv[1:] or ['pinacopedia', 'culinapedia']
out = BASE / ('vista-previa' if not sys.argv[1:] else 'vista-previa-' + '-'.join(SITIOS_V))
if out.exists(): shutil.rmtree(out)
for sitio in SITIOS_V:
    d = BASE / sitio / 'payload'
    m = json.loads((BASE / sitio / 'manifiesto.json').read_text())
    dom = m['dominio']
    ult = m['indices'][-1]
    pags = {}
    cps = {**{'es': '', 'en': 'en/'}, **m.get('carpetas', {})}
    CARPS = [cps[l] + 'blog' for l in m.get('idiomas', ['es', 'en'])]
    for lang, carp in [(l, cps[l] + 'blog') for l in m.get('idiomas', ['es', 'en'])]:
        for f in (d / carp).glob('*.html'):
            pags[f'{carp}/{f.name}'] = f.read_text()
        pags[f'{carp}/index.html'] = (d / 'indices' / lang / f'{ult}.html').read_text()
    for rel, h in pags.items():
        live = f'https://{dom}/{rel}'
        carp = rel.rsplit('/', 1)[0]
        def fix(mm):
            attr, q, v = mm.group(1), mm.group(2), mm.group(3)
            if v.startswith(('http', '#', 'mailto')): return mm.group(0)
            if v in ('./', ''): return f'{attr}={q}index.html{q}'
            if '/' not in v and v.endswith('.html'): return mm.group(0)  # otra página del blog
            ab = urljoin(live, v)
            # enlaces al blog del otro idioma: dentro de la vista previa
            for c in CARPS:
                pre = f'https://{dom}/{c}/'
                if ab.startswith(pre):
                    dest = ab[len(pre):] or 'index.html'
                    if carp == c: return f'{attr}={q}{dest}{q}'
                    return f'{attr}={q}{os.path.relpath(c, carp)}/{dest}{q}'
            return f'{attr}={q}{ab}{q}'
        h2 = re.sub(r'\b(href|src|action)=(["\'])([^"\']*)\2', fix, h)
        p = out / sitio / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(h2)
    if (d / 'blog' / 'img').exists():
        shutil.copytree(d / 'blog' / 'img', out / sitio / 'blog' / 'img')
print('ok', sorted(str(p.relative_to(out)) for p in out.rglob('*.html')))
