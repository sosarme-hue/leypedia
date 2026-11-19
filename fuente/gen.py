#!/usr/bin/env python3
"""Genera el blog de Pinacopedia y de Culinapedia (ES y EN).
Uso: python3 gen.py <sitio> [--vista]
Salida: <sitio>/payload/{blog,en/blog,indices/{es,en}}, <sitio>/manifiesto.json
"""
import html, json, re, sys
from pathlib import Path
from datetime import date

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))
from sitios import SITIOS  # noqa: E402

MESES = {'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
         'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
T = {
    'es': {'blog': 'Blog', 'inicio': 'Inicio', 'min': 'min de lectura', 'por': 'Por', 'mas': 'Más del blog', 'compartir': 'Compartir:',
           'todos': 'Ver todos los artículos', 'leer': 'Leer artículo →', 'otro': 'English'},
    'en': {'blog': 'Blog', 'inicio': 'Home', 'min': 'min read', 'por': 'By', 'mas': 'More from the blog', 'compartir': 'Share:',
           'todos': 'See all posts', 'leer': 'Read post →', 'otro': 'Español'},
}


def ffecha(f, lang):
    y, m, d = map(int, f.split('-'))
    return f'{d} de {MESES["es"][m-1]} de {y}' if lang == 'es' else f'{d} {MESES["en"][m-1]} {y}'


def esc(s):
    return html.escape(s, quote=True)


class Sitio:
    def __init__(self, nombre):
        self.n = nombre
        self.c = SITIOS[nombre]
        self.dir = BASE / nombre
        self.dom = self.c['dominio']
        self.art = self.c['articulos']
        self.idiomas = self.c.get('idiomas', ['es', 'en'])
        self.env = self.c.get('envoltura', ('', ''))
        self.orden = sorted(self.art, key=lambda k: (self.art[k]['fecha'], list(self.art).index(k)))

    def url(self, lang, slug=''):
        return f'https://{self.dom}/' + ('en/' if lang == 'en' else '') + 'blog/' + (f'{slug}.html' if slug else '')

    def raiz(self, lang):  # de la página del blog a la raíz del idioma
        return '../'

    def rimg(self, lang):  # de la página del blog a la raíz física (img, assets)
        return '../../' if lang == 'en' else '../'

    def hreflang(self, es_url, en_url):
        if len(self.idiomas) < 2: return ''
        return f'<link rel="alternate" hreflang="es" href="{es_url}"><link rel="alternate" hreflang="en" href="{en_url}">'

    def src(self, img, lang):  # imagen local (relativa a la raiz) o URL absoluta
        return img if img.startswith('http') else self.rimg(lang) + img

    def absimg(self, img):
        return img if img.startswith('http') else f'https://{self.dom}/{img}'

    def contenido(self, clave, lang):
        p = self.dir / 'contenido' / lang / f'{clave}.html'
        return p.read_text() if p.exists() else None

    def marcas(self, t, lang):
        R, I = self.raiz(lang), self.rimg(lang)
        def fig(m):
            src, enl, cap = m.group(1), m.group(2), m.group(3)
            return (f'<figure class="{self.c["clase_fig"]}"><a href="{R}{enl}"><img src="{self.src(src, lang)}" alt="{esc(cap.split(".")[0])}" loading="lazy"></a>'
                    f'<figcaption>{cap}</figcaption></figure>')
        t = re.sub(r'\{fig:([^|}]+)\|([^|}]+)\|([^}]+)\}', fig, t)
        def art(m):
            k = m.group(1)
            return f'<a href="{self.art[k][lang][0]}.html">{m.group(2)}</a>'
        t = re.sub(r'\{art:([a-z0-9]+)\|([^}]+)\}', art, t)
        pref = dict(self.c.get('pref', {'o': 'o/', 'b': 'b/', 'm': 'm/', 'p': 'p/'}), u='')
        def enl(m):
            k, slug, txt = m.group(1), m.group(2), m.group(3)
            dest = slug if k == 'u' else f'{pref[k]}{slug}.html'
            return f'<a href="{R}{dest}">{txt}</a>'
        t = re.sub(r'\{([' + ''.join(pref) + r']):([^|}]+)\|([^}]+)\}', enl, t)
        assert '{' not in re.sub(r'<script.*?</script>', '', t, flags=re.S), 'marca sin resolver'
        return t

    def cabecera(self, lang, titulo, desc, url, alt_url, og_img, og_type, extra=''):
        c = self.c
        I = self.rimg(lang)
        alt_lang = 'en' if lang == 'es' else 'es'
        es_url, en_url = (url, alt_url) if lang == 'es' else (alt_url, url)
        og = f'<meta property="og:image" content="{self.absimg(og_img)}">' if og_img else ''
        return f'''<!doctype html>
<html lang="{lang}" data-raiz="{c.get('data_raiz', {}).get(lang, I)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)} · {c["nombre"]}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{c["nombre"]}"><meta property="og:title" content="{esc(titulo)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">{og}<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">{self.hreflang(es_url, en_url)}
{(c["head"][lang] if isinstance(c["head"], dict) else c["head"]).replace("{I}", I)}
<style>{c["css"]}</style>{extra}
</head>
<body{c.get("body", {}).get(lang, "").replace("{I}", I)}>
{c["cab"][lang].replace("{R}", self.raiz(lang)).replace("{I}", I).replace("{ALT}", ("../../blog/" if lang == "en" else "../en/blog/") + ("" if alt_url.endswith("/") else alt_url.rsplit("/", 1)[1]))}
'''

    def pie(self, lang):
        return self.c['pie'][lang].replace('{R}', self.raiz(lang)).replace('{I}', self.rimg(lang)) + '\n</body>\n</html>\n'

    def compartir(self, lang, titulo, u):
        from urllib.parse import quote
        return (f'<p class="compartir"><span>{T[lang]["compartir"]}</span>'
                f'<a href="https://www.facebook.com/sharer/sharer.php?u={quote(u, safe="")}" target="_blank" rel="noopener">Facebook</a>'
                f'<a href="https://wa.me/?text={quote(titulo + " · " + self.c["nombre"] + " " + u, safe="")}" target="_blank" rel="noopener">WhatsApp</a></p>')

    def tarjeta(self, k, lang, rel=''):
        slug, tit, desc, mins = self.art[k][lang][:4]
        img = self.art[k]['img']
        return (f'<a class="blog-card" href="{rel}{slug}.html"><img src="{self.src(img, lang)}" alt="" loading="lazy">'
                f'<span class="blog-fecha">{ffecha(self.art[k]["fecha"], lang)}</span><b>{esc(tit)}</b><span>{esc(desc)}</span></a>')

    def articulo(self, k, lang):
        a = self.art[k]
        slug, tit, desc, mins = a[lang][:4]
        alt = 'en' if lang == 'es' else 'es'
        u, au = self.url(lang, slug), self.url(alt, a[alt][0])
        cuerpo = self.marcas(self.contenido(k, lang), lang)
        ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": tit, "description": desc, "inLanguage": lang,
              "datePublished": a['fecha'], "author": {"@type": "Person", "name": self.c['autor']},
              "image": self.absimg(a["img"]), "mainEntityOfPage": u,
              "publisher": {"@type": "Organization", "name": self.c['nombre']}}
        extra = f'\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        previas = [x for x in reversed(self.orden) if x != k and self.art[x]['fecha'] <= a['fecha']][:3]
        mas = ''
        if previas:
            mas = f'<section class="blog-mas"><h2>{T[lang]["mas"]}</h2><div class="blog-lista">' + ''.join(self.tarjeta(x, lang) for x in previas) + \
                  f'</div><p><a class="blog-todos" href="./">{T[lang]["todos"]}</a></p></section>'
        R = self.raiz(lang)
        h = self.cabecera(lang, tit, desc, u, au, a['img'], 'article', extra)
        h += f'''<main>{self.env[0]}
<article class="blog-art">
<nav class="{self.c["clase_miga"]}"><a href="{R}index.html">{T[lang]["inicio"]}</a> › <a href="./">Blog</a></nav>
<h1>{esc(tit)}</h1>
<p class="blog-meta">{ffecha(a["fecha"], lang)} · {mins} {T[lang]["min"]} · {T[lang]["por"]} {self.c["autor"]}</p>
<p class="blog-entradilla">{esc(desc)}</p>
<div class="blog-texto">
{cuerpo}
</div>
{self.compartir(lang, tit, u)}
</article>
{mas}
{self.env[1]}</main>
'''
        return h + self.pie(lang)

    def indice(self, lang, hasta):
        ks = [x for x in reversed(self.orden) if self.art[x]['fecha'] <= hasta]
        c = self.c['indice'][lang]
        alt = 'en' if lang == 'es' else 'es'
        h = self.cabecera(lang, c[0], c[1], self.url(lang), self.url(alt), self.art[ks[0]]['img'], 'website')
        R = self.raiz(lang)
        h += f'''<main>{self.env[0]}
<nav class="{self.c["clase_miga"]}"><a href="{R}index.html">{T[lang]["inicio"]}</a> › Blog</nav>
<section class="blog-cab"><h1>{c[0]}</h1><p>{c[1]}</p></section>
<div class="blog-lista blog-portada">{"".join(self.tarjeta(x, lang) for x in ks)}</div>
{self.env[1]}</main>
'''
        return h + self.pie(lang)

    def generar(self):
        out = self.dir / 'payload'
        import shutil
        if out.exists():
            shutil.rmtree(out)
        manif = {'articulos': [], 'indices': []}
        faltan = []
        for k in self.orden:
            arch, urls = [], []
            ok = all(self.contenido(k, l) for l in self.idiomas)
            if not ok:
                faltan.append(k)
                continue
            for lang in self.idiomas:
                rel = ('en/' if lang == 'en' else '') + f'blog/{self.art[k][lang][0]}.html'
                p = out / rel
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(self.articulo(k, lang))
                arch.append(rel); urls.append(self.url(lang, self.art[k][lang][0]))
            manif['articulos'].append({'clave': k, 'fecha': self.art[k]['fecha'], 'archivos': arch, 'urls': urls})
        fechas = sorted({self.art[k]['fecha'] for k in self.orden if k not in faltan})
        for f in fechas:
            for lang in self.idiomas:
                p = out / 'indices' / lang / f'{f}.html'
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(self.indice(lang, f))
        manif['indices'] = fechas
        manif['dominio'] = self.dom
        if self.idiomas != ['es', 'en']:
            manif['idiomas'] = self.idiomas
        if self.c.get('no_tocar_web'):
            manif['no_tocar_web'] = True
        if self.c.get('raiz_fisica'):
            manif['raiz'] = self.c['raiz_fisica']
        imgs = self.dir / 'imagenes'
        if imgs.exists():
            dimg = out / 'blog' / 'img'
            dimg.mkdir(parents=True, exist_ok=True)
            for f in imgs.iterdir():
                shutil.copy2(f, dimg / f.name)
            manif['imagenes'] = sorted('blog/img/' + f.name for f in imgs.iterdir())
        (self.dir / 'manifiesto.json').write_text(json.dumps(manif, ensure_ascii=False, indent=1))
        return faltan


if __name__ == '__main__':
    s = Sitio(sys.argv[1])
    f = s.generar()
    print(s.n, 'artículos:', len(s.orden) - len(f), 'sin texto todavía:', f)
