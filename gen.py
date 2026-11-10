#!/usr/bin/env python3
"""Genera el blog de Classicapedia (ES y EN) en payload/blog y payload/en/blog."""
import html, json, re, sys
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'payload'
FECHA = '2026-11-10'
AUTOR = 'Alejandro Rosàs Navarro'
FB_ES = 'https://www.facebook.com/profile.php?id=61593056551514'
FB_EN = 'https://www.facebook.com/partenope'

ART = {
    'mesias': {
        'es': ('el-mesias-de-handel-guia-para-escucharlo', 'El Mesías de Händel: guía para escucharlo esta Navidad',
               'Historia, momentos clave y grabaciones recomendadas del oratorio más famoso de Händel, del estreno en Dublín al «Aleluya».', 9,
               ('https://www.facebook.com/groups/7449623075076737', 'Baroque Composers Group')),
        'en': ('handels-messiah-listening-guide', "Handel's Messiah: a listening guide for Christmas",
               "History, key moments and recommended recordings of Handel's most famous oratorio, from the Dublin premiere to the Hallelujah chorus.", 9,
               ('https://www.facebook.com/groups/7449623075076737', 'Baroque Composers Group')),
    },
    'navidad': {
        'es': ('musica-clasica-para-navidad-12-obras', 'Música clásica para Navidad: 12 obras imprescindibles',
               'De Schütz a Britten: doce obras de música clásica para acompañar las fiestas, con la historia de cada una.', 8,
               ('https://www.facebook.com/groups/2570606293398264', 'Sacred Music: From Gregorian Chant to the Modern Age')),
        'en': ('christmas-classical-music-12-works', 'Classical music for Christmas: 12 essential works',
               'From Schütz to Britten: twelve pieces of classical music for the holidays, with the story behind each one.', 8,
               ('https://www.facebook.com/groups/2570606293398264', 'Sacred Music: From Gregorian Chant to the Modern Age')),
    },
    'anonuevo': {
        'es': ('concierto-de-ano-nuevo-de-viena-historia', 'El Concierto de Año Nuevo de Viena: historia y curiosidades',
               'La familia Strauss, el origen del concierto en 1939, los grandes directores y los rituales del Danubio azul y la Marcha Radetzky.', 8,
               ('https://www.facebook.com/groups/7719320188080233', 'Conductors and Instrumental Soloists')),
        'en': ('vienna-new-years-concert-history', "The Vienna New Year's Concert: history and curiosities",
               'The Strauss family, the 1939 origins of the concert, its great conductors and the rituals of the Blue Danube and the Radetzky March.', 8,
               ('https://www.facebook.com/groups/7719320188080233', 'Conductors and Instrumental Soloists')),
    },
}
ORDEN = ['mesias', 'navidad', 'anonuevo']

T = {
    'es': dict(lang='es', otro='en', inicio='Inicio', blog='Blog', fecha='10 de noviembre de 2026', por='Por', min='min de lectura',
               compartir='Compartir:', mas='Sigue leyendo en el blog', bios='Biografías citadas en este artículo',
               com_t='Únete a la comunidad', com_p='Cada día compartimos grabaciones, documentos y descubrimientos con miles de aficionados en Facebook. La participación es libre y gratuita.',
               com_fb='Página de Facebook en español', com_ver='Ver todos los grupos', fb=FB_ES,
               idx_t='Blog de Classicapedia', idx_d='Artículos sobre música clásica: guías para escuchar, historias de obras y de músicos, y recomendaciones de grabaciones, con enlaces a más de 22.000 biografías.',
               idx_e='Guías para escuchar, historias de obras y de músicos, y recomendaciones de grabaciones. Cada artículo enlaza con las biografías de Classicapedia para que puedas seguir leyendo.',
               leer='Leer el artículo', locale='es_ES', locale2='en_GB'),
    'en': dict(lang='en', otro='es', inicio='Home', blog='Blog', fecha='10 November 2026', por='By', min='min read',
               compartir='Share:', mas='Keep reading on the blog', bios='Biographies mentioned in this article',
               com_t='Join the community', com_p='Every day we share recordings, documents and discoveries with thousands of music lovers on Facebook. Membership is free and open to all.',
               com_fb='Our Facebook page', com_ver='See all the groups', fb=FB_EN,
               idx_t='The Classicapedia blog', idx_d='Articles on classical music: listening guides, stories of works and musicians, and recording recommendations, linked to over 22,000 biographies.',
               idx_e='Listening guides, stories of works and musicians, and recording recommendations. Every article links to the Classicapedia biographies so you can keep reading.',
               leer='Read the article', locale='en_GB', locale2='es_ES'),
}

TJS = {
    'es': '{"loc": "es", "bios": "biografías", "pn": {"medieval": "Edad Media", "renacimiento": "Renacimiento", "barroco": "Barroco", "clasicismo": "Clasicismo", "romanticismo": "Romanticismo", "siglo-xx": "Siglo XX", "contemporaneo": "Música contemporánea"}, "meses": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"], "de": " de ", "nace": "Nace", "muere": "Muere", "sin_efe": "Hoy no hay efemérides registradas.", "en_pagina": "En esta página", "anec_tag": "Curiosidad", "po_res": "{n} posts encontrados", "po_ninguno": "Ningún post coincide con la búsqueda.", "ver_res": "Ver todos los resultados, también en los posts"}',
    'en': '{"loc": "en", "bios": "biographies", "pn": {"medieval": "Middle Ages", "renacimiento": "Renaissance", "barroco": "Baroque", "clasicismo": "Classical", "romanticismo": "Romantic", "siglo-xx": "20th century", "contemporaneo": "Contemporary"}, "meses": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], "de": " ", "nace": "Born", "muere": "Died", "sin_efe": "No anniversaries recorded for today.", "en_pagina": "On this page", "anec_tag": "Curiosity", "po_res": "{n} stories found", "po_ninguno": "No story matches your search.", "ver_res": "See all results, including the stories"}',
}

MENU = {
    'es': [('explorar.html', 'Explorar'), ('explorar.html?a=compositor', 'Compositores'), ('explorar.html?a=batuta', 'Directores'),
           ('explorar.html?a=solista', 'Solistas'), ('maestros.html', 'Maestros y alumnos'), ('comunidad.html', 'Comunidad'),
           ('posts.html', 'Posts'), ('blog/', 'Blog')],
    'en': [('explorar.html', 'Explore'), ('explorar.html?a=compositor', 'Composers'), ('explorar.html?a=batuta', 'Conductors'),
           ('explorar.html?a=solista', 'Soloists'), ('maestros.html', 'Teachers & pupils'), ('comunidad.html', 'Community'),
           ('posts.html', 'Stories'), ('blog/', 'Blog')],
}
AUDIO = {'es': 'https://classicalarchive.org/es/audio/', 'en': 'https://classicalarchive.org/audio/'}
BUSCA = {'es': ('Buscar compositor, intérprete, luthier…', 'Buscar', '☰ Índice', 'Índice'),
         'en': ('Search composer, performer, luthier…', 'Search', '☰ Index', 'Index')}
PIE = {
    'es': ('Biografías originales redactadas en castellano. Periodos: Edad Media · Renacimiento · Barroco · Clasicismo · Romanticismo · Siglo XX · Contemporánea.',
           [('sobre.html', 'Quién soy'), ('comunidad.html', 'Comunidad')], [('aviso-legal.html', 'Aviso legal'), ('privacidad.html', 'Privacidad'), ('cookies.html', 'Cookies')], 'Configurar cookies'),
    'en': ('Original biographies. Periods: Middle Ages · Renaissance · Baroque · Classical · Romantic · 20th century · Contemporary.',
           [('sobre.html', 'About me'), ('comunidad.html', 'Community')], [('aviso-legal.html', 'Legal notice'), ('privacidad.html', 'Privacy'), ('cookies.html', 'Cookies')], 'Cookie settings'),
}
LOGO = '<svg class="logo" viewBox="0 0 56 64" aria-hidden="true"><path d="M40 14a20 20 0 1 0 0 36" fill="none" stroke="var(--marca,#a8823a)" stroke-width="5" stroke-linecap="round"/><ellipse cx="26" cy="40" rx="7" ry="5" fill="currentColor" transform="rotate(-20 26 40)"/><path d="M32.5 38V16c4 3 8 6 9 11" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>'
FBSVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>'

CSS = """<style>
.blog-art .texto p:first-child::first-letter{color:var(--marca)}
.blog-art .autor{color:var(--suave);font-size:.92rem;margin:4px 0 0}
.blog-art .texto h2{font-size:1.65rem;margin:1.6em 0 .4em;line-height:1.2}
.blog-art .texto ul{padding-left:1.2em}.blog-art .texto li{margin:.5em 0}
.blog-art .texto a{color:var(--oro);text-decoration-thickness:1px;text-underline-offset:2px}
.caja-com{background:var(--blanco);border:1px solid var(--linea);border-left:4px solid #1877f2;border-radius:10px;padding:16px 20px;margin:36px 0 0}
.caja-com h2{margin:0 0 6px!important;font-size:1.4rem!important}.caja-com p{margin:0 0 10px}
.caja-com .botones-com{display:flex;flex-wrap:wrap;gap:8px}
.caja-com .botones-com a{display:inline-block;padding:7px 14px;border-radius:999px;text-decoration:none;font-weight:600;font-size:.9rem}
.caja-com .fbb{background:#1877f2;color:#fff}.caja-com .otro{border:1px solid var(--linea);color:var(--tinta)}
.bios-citadas{margin-top:32px}.bios-citadas h2{font-size:1.4rem}
.bios-citadas ul{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.bios-citadas li a{display:inline-block;padding:3px 11px;border:1px solid var(--linea);border-radius:12px;background:var(--blanco);text-decoration:none;font-size:.86rem}
.mas-blog{margin-top:32px}.mas-blog h2{font-size:1.4rem}
.blog-lista{display:grid;gap:14px;margin:18px 0 8px}
.blog-card{display:block;padding:18px 20px;border:1px solid var(--linea);border-left:4px solid var(--marca);border-radius:10px;background:var(--blanco);text-decoration:none}
.blog-card:hover{border-color:var(--oro)}
.blog-card small{color:var(--suave);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}
.blog-card strong{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:1.6rem;line-height:1.2;margin:4px 0 6px}
.blog-card em{display:block;font-style:normal;color:var(--suave)}
.blog-card .leer{display:inline-block;margin-top:8px;color:var(--oro);font-weight:600;font-size:.92rem}
.blog-idx{max-width:760px}
.blog-art .texto .caja-com .fbb{color:#fff;text-decoration:none}.blog-art .texto .caja-com .otro{color:var(--tinta);text-decoration:none}
.blog-art .texto .bios-citadas ul{padding-left:0}.blog-art .texto .bios-citadas li{margin:0}
.blog-art .texto .compartir a{color:#fff;text-decoration:none}
.blog-art .texto .blog-card{color:var(--tinta);text-decoration:none}
</style>"""

e = html.escape


def enlaces(texto, lang, bios):
    def b(m):
        slug, nombre = m.group(1), m.group(2)
        if slug not in [s for s, _ in bios]:
            bios.append((slug, re.sub(r'<[^>]+>', '', nombre)))
        return f'<a href="../b/{slug}.html">{nombre}</a>'

    def a(m):
        return f'<a href="{ART[m.group(1)][lang][0]}.html">{m.group(2)}</a>'
    texto = re.sub(r'\{b:([a-z0-9-]+)\|([^}]+)\}', b, texto)
    texto = re.sub(r'\{art:([a-z]+)\|([^}]+)\}', a, texto)
    assert '{' not in texto, 'marcador sin resolver'
    return texto


def cabecera(lang, titulo, desc, url, alt_url, og_type, extra=''):
    t = T[lang]
    menu = '\n'.join(f'  <a href="../{h}">{n}</a>' for h, n in MENU[lang])
    ph, al, bi, ind = BUSCA[lang]
    otro = t['otro'].upper()
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)} · Classicapedia</title>
<meta name="description" content="{e(desc)}">
<link rel="alternate" hreflang="{lang}" href="{url}">
<link rel="alternate" hreflang="{t['otro']}" href="{alt_url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Classicapedia">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://classicapedia.com/assets/og-classicapedia.png">
<meta property="og:locale" content="{t['locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="../assets/fuentes.css">
<link rel="stylesheet" href="../assets/estilo.css">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/icono-180.png">
<script>window.T={TJS[lang]};window.RAIZ='../';</script>
<meta name="google-adsense-account" content="ca-pub-6250668607782976">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6250668607782976" crossorigin="anonymous"></script>
<script src="../assets/ga.js"></script>
{CSS}
{extra}</head>
<body>
<header class="cab">
 <button class="btn-indice" type="button" aria-controls="lateral" aria-expanded="false">{bi}</button>
 <a class="marca" href="../index.html">{LOGO}Classicapedia</a>
 <nav class="menu">
{menu}
  <a class="patreon" href="{AUDIO[lang]}" rel="noopener">Audio</a>
  <a class="facebook" href="../comunidad.html">{FBSVG}Facebook</a>
 </nav>
 <span class="idioma">{'<b>ES</b> | <a href="%s" hreflang="en">EN</a>' % alt_url.replace('https://classicapedia.com/', '../') if lang == 'es' else '<a href="%s" hreflang="es">ES</a> | <b>EN</b>' % alt_url.replace('https://classicapedia.com/', '../../')}</span>
 <form class="busca-mini" action="../explorar.html"><input name="q" type="search" placeholder="{ph}" aria-label="{al}" autocomplete="off"><div id="sug-mini" class="sug-mini"></div></form>
</header>
<div class="cuerpo">
<aside id="lateral" class="lateral" aria-label="{ind}"></aside>
<main>
'''


def pie(lang):
    txt, redes, leg, conf = PIE[lang]
    r = ' · '.join(f'<a href="../{h}">{n}</a>' for h, n in redes) + ' · <a href="https://www.patreon.com/c/ClassicMusicComposersGroup">Patreon</a>'
    l = ' · '.join(f'<a href="../{h}">{n}</a>' for h, n in leg)
    return f'''</main>
</div>
<script src="../assets/menu.js"></script>

<footer class="pie">
 <p>{txt}</p>
 <p class="redes">{r}</p>
 <p class="legales">{l} · <a href="#" data-cookies>{conf}</a> · © 2026 Classicapedia</p>
</footer>
<script src="../assets/pie.js"></script>
</body>
</html>
'''


def url(lang, slug=''):
    pre = 'https://classicapedia.com/' + ('en/' if lang == 'en' else '') + 'blog/'
    return pre + (slug + '.html' if slug else '')


def compartir(lang, titulo, u):
    q = __import__('urllib.parse').parse.quote
    return (f'<p class="compartir"><span>{T[lang]["compartir"]}</span>'
            f'<a class="sh-fb" href="https://www.facebook.com/sharer/sharer.php?u={q(u, safe="")}" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>'
            f'<a class="sh-wa" href="https://wa.me/?text={q(titulo + " — Classicapedia " + u, safe="")}" target="_blank" rel="noopener" aria-label="WhatsApp">WhatsApp</a></p>')


def articulo(clave, lang):
    t = T[lang]
    slug, titulo, desc, mins, grupo = ART[clave][lang]
    otro = t['otro']
    u, alt = url(lang, slug), url(otro, ART[clave][otro][0])
    bios = []
    cuerpo = enlaces((BASE / 'contenido' / lang / f'{clave}.html').read_text(), lang, bios)
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": titulo, "description": desc,
          "datePublished": FECHA, "dateModified": FECHA, "inLanguage": lang, "mainEntityOfPage": u,
          "image": "https://classicapedia.com/assets/og-classicapedia.png",
          "author": {"@type": "Person", "name": AUTOR, "url": "https://classicapedia.com/" + ('en/' if lang == 'en' else '') + "sobre.html"},
          "publisher": {"@type": "Organization", "name": "Classicapedia", "url": "https://classicapedia.com/"}}
    extra = f'<meta property="article:published_time" content="{FECHA}">\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    h = cabecera(lang, titulo, desc, u, alt, 'article', extra)
    otros = [k for k in ORDEN if k != clave]
    mas = '\n'.join(f'<a class="blog-card" href="{ART[k][lang][0]}.html"><small>{t["fecha"]}</small><strong>{e(ART[k][lang][1])}</strong><em>{e(ART[k][lang][2])}</em></a>' for k in otros)
    lb = '\n'.join(f'<li><a href="../b/{s}.html">{e(n)}</a></li>' for s, n in bios)
    h += f'''<article class="ficha post blog-art">
<nav class="miga"><a href="../index.html">{t['inicio']}</a> › <a href="./">{t['blog']}</a></nav>
<header><p class="fecha-post">{t['fecha']} · {mins} {t['min']}</p><h1>{e(titulo)}</h1>
<p class="sub">{e(desc)}</p>
<p class="autor">{t['por']} <a href="../sobre.html">{AUTOR}</a></p>
{compartir(lang, titulo, u)}</header>
<div class="texto">
{cuerpo}
<section class="caja-com"><h2>{t['com_t']}</h2><p>{t['com_p']}</p>
<p class="botones-com"><a class="fbb" href="{t['fb']}" rel="noopener">{t['com_fb']}</a><a class="fbb" href="{grupo[0]}" rel="noopener">{e(grupo[1])}</a><a class="otro" href="../comunidad.html">{t['com_ver']}</a></p></section>
<section class="bios-citadas"><h2>{t['bios']}</h2><ul>
{lb}
</ul></section>
<section class="mas-blog"><h2>{t['mas']}</h2><div class="blog-lista">
{mas}
</div></section>
{compartir(lang, titulo, u)}
</div>
</article>
'''
    h += pie(lang)
    return slug, h, bios


def indice(lang):
    t = T[lang]
    otro = t['otro']
    h = cabecera(lang, t['idx_t'], t['idx_d'], url(lang), url(otro), 'website')
    cards = '\n'.join(f'<a class="blog-card" href="{ART[k][lang][0]}.html"><small>{t["fecha"]} · {ART[k][lang][3]} {t["min"]}</small><strong>{e(ART[k][lang][1])}</strong><em>{e(ART[k][lang][2])}</em><span class="leer">{t["leer"]} →</span></a>' for k in ORDEN)
    h += f'''<section class="explorar blog-idx"><nav class="miga"><a href="../index.html">{t['inicio']}</a> › {t['blog']}</nav>
<h1>{t['idx_t']}</h1><p class="entradilla">{t['idx_e']}</p>
<div class="blog-lista">
{cards}
</div>
<section class="caja-com"><h2>{t['com_t']}</h2><p>{t['com_p']}</p>
<p class="botones-com"><a class="fbb" href="{t['fb']}" rel="noopener">{t['com_fb']}</a><a class="otro" href="../comunidad.html">{t['com_ver']}</a></p></section>
</section>
'''
    h += pie(lang)
    return h


def main():
    todas = set()
    for lang in ('es', 'en'):
        d = OUT / ('en/blog' if lang == 'en' else 'blog')
        d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(indice(lang))
        for k in ORDEN:
            slug, h, bios = articulo(k, lang)
            (d / f'{slug}.html').write_text(h)
            todas.update(s for s, _ in bios)
    (BASE / 'bios-enlazadas.txt').write_text('\n'.join(sorted(todas)) + '\n')
    urls = []
    for lang in ('es', 'en'):
        urls.append(url(lang))
        urls += [url(lang, ART[k][lang][0]) for k in ORDEN]
    (BASE / 'urls.json').write_text(json.dumps(urls, indent=1))
    print(len(todas), 'biografías enlazadas;', len(urls), 'páginas')


main()
