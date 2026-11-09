# -*- coding: utf-8 -*-
import os, re, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from curiosidades import *

OUT = sys.argv[1]
PREVIEW = "preview" in sys.argv[2:]
PALETA = True  # paleta azul marino y verde petróleo elegida por Alex
import json, html as _h
BASE = "https://leypedia.com/"
HERE = os.path.dirname(__file__)

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

def rel(from_route, to_route):
    depth = from_route.count("/")
    if PREVIEW:
        to_route = to_route + "index.html"
    return ("../" * depth) + to_route if (("../" * depth) + to_route) else "./"

def fill_links(html, lang, route):
    def rep(m):
        k = m.group(1)
        if k == "img":
            return "../" * route.count("/") + "assets/img/"
        if k in ROUTES:
            r = rel(route, ROUTES[k][0 if lang == "es" else 1])
            return r or "./"
        return m.group(0)
    return re.sub(r"\{([a-z]+)\}", rep, html)

def page(pid, lang):
    p = PAGES[pid][lang]
    route = ROUTES[pid][0 if lang == "es" else 1]
    alt = ROUTES[pid][1 if lang == "es" else 0]
    ui = UI[lang]
    pre = "../" * route.count("/")
    nav = "".join(
        f'<a href="{{{k}}}"{" aria-current=\"page\"" if (k == pid or PARENT.get(pid) == k) else ""}>{t}</a>'
        for k, t in ui["nav"])
    crumbs = ""
    if p.get("crumbs") is not None:
        cs = [f'<a href="{{home}}">{ui["inicio"]}</a>'] + [f'<a href="{{{k}}}">{t}</a>' for k, t in p["crumbs"]]
        crumbs = f'<div class="wrap"><div class="crumbs">{" › ".join(cs)}</div></div>'
    title = p["title"] if p.get("plain_title") else p["title"] + " · Leypedia"
    legal = " · ".join(f'<a href="{{{k}}}">{t}</a>' for k, t in ui["legal"])
    html = f'''<!doctype html>
<html lang="{lang}"{" data-preview" if PREVIEW else ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{BASE}{route}">
<link rel="alternate" hreflang="es" href="{BASE}{ROUTES[pid][0]}">
<link rel="alternate" hreflang="ca" href="{BASE}{ROUTES[pid][1]}">
<link rel="alternate" hreflang="x-default" href="{BASE}{ROUTES[pid][0]}">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}assets/style.css">
<script src="{pre}assets/app.js" defer></script>
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{{home}}">Ley<span>pedia</span></a>
<nav class="main" aria-label="{"Secciones" if lang=="es" else "Seccions"}">{nav}</nav>
{searchbox(lang)}
<a class="langlink" href="{rel(route, alt)}" hreflang="{ui["otra_l"]}" lang="{ui["otra_l"]}">{ui["otra"]}</a>
</div></header>
<main>
{crumbs}
{p["html"]}
</main>
<footer><div class="wrap">
<div><p>{ui["aviso"]}</p><p>{ui["fuentes"]}</p></div>
<div><p>{legal}</p><p>© 2026 Leypedia</p></div>
</div></footer>
</body>
</html>
'''
    html = fill_links(html, lang, route)
    d = os.path.join(OUT, route)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    txt = re.sub(r"<[^>]+>", " ", p["html"])
    txt = re.sub(r"\s+", " ", _h.unescape(txt)).strip()
    INDEX[lang].append({"t": p["title"], "d": _h.unescape(p["desc"]), "u": route, "a": ambitos(pid, p["html"]), "x": txt[:5000]})
    return route

INDEX = {"es": [], "ca": []}
routes = []
for pid in ROUTES:
    if pid not in PAGES:
        continue
    for lang in ("es", "ca"):
        routes.append(page(pid, lang))

# assets
os.makedirs(os.path.join(OUT, "assets"))
css = open(os.path.join(HERE, "base.css"), encoding="utf-8").read()
css = css.replace('--f-display:"Spectral", Georgia, "Times New Roman", serif;', '--f-display:"Iowan Old Style","Palatino Linotype","Book Antiqua",Palatino,Georgia,serif;')
css = css.replace('--f-body:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;', '--f-body:system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;')
css = css.replace('--f-mono:"IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;', '--f-mono:ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;')
css += open(os.path.join(HERE, "extra.css"), encoding="utf-8").read()
css += open(os.path.join(HERE, "extra2.css"), encoding="utf-8").read()
if PALETA:
    css += open(os.path.join(HERE, "paleta.css"), encoding="utf-8").read()
open(os.path.join(OUT, "assets/style.css"), "w", encoding="utf-8").write(css)
shutil.copy(os.path.join(HERE, "app.js"), os.path.join(OUT, "assets/app.js"))
open(os.path.join(OUT, "assets/favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#8C2F39"/><text x="32" y="45" font-family="Georgia,serif" font-size="40" font-weight="700" text-anchor="middle" fill="#fff">L</text></svg>')

shutil.copytree(os.path.join(HERE, "img"), os.path.join(OUT, "assets/img"))
for L in ("es", "ca"):
    INDEX[L] = [x for x in INDEX[L] if x["u"] not in ("buscar/", "ca/cercar/")]
    json.dump(INDEX[L], open(os.path.join(OUT, f"assets/buscar-{L}.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

# api
os.makedirs(os.path.join(OUT, "api/cache"))
shutil.copy(os.path.join(HERE, "boe.php"), os.path.join(OUT, "api/boe.php"))
shutil.copy(os.path.join(HERE, "feed.php"), os.path.join(OUT, "api/feed.php"))
shutil.copy(os.path.join(HERE, "actualizar.php"), os.path.join(OUT, "api/actualizar.php"))
open(os.path.join(OUT, "api/cache/.htaccess"), "w").write("Require all denied\n")
open(os.path.join(OUT, "api/cache/.gitkeep"), "w").write("")
shutil.copy(os.path.join(HERE, "htaccess"), os.path.join(OUT, ".htaccess"))

# sitemap / robots
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}{r}</loc><lastmod>2026-11-09</lastmod></url>\n" for r in routes) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nDisallow: /api/\nSitemap: {BASE}sitemap.xml\n")
print(len(routes), "páginas")
