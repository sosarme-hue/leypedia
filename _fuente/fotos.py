# -*- coding: utf-8 -*-
# Fotos en materias y en las cabeceras de sección (todas de Wikimedia Commons, en assets/img/)
import re
from temas import *

MATIMG = {"Vivienda": "m-vivienda", "Habitatge": "m-vivienda", "Trabajo": "m-trabajo", "Treball": "m-trabajo",
          "Familia": "m-familia", "Família": "m-familia", "Sucesiones": "m-sucesiones", "Successions": "m-sucesiones",
          "Consumo": "m-consumo", "Consum": "m-consumo", "Autónomos y empresas": "m-autonomos", "Autònoms i empreses": "m-autonomos",
          "Fiscalidad": "m-fiscalidad", "Fiscalitat": "m-fiscalidad", "Seguridad Social": "s-jubilacion", "Seguretat Social": "s-jubilacion",
          "Extranjería": "m-extranjeria", "Estrangeria": "m-extranjeria", "Administración": "m-administracion", "Administració": "m-administracion",
          "Protección de datos": "m-datos", "Protecció de dades": "m-datos"}

def _mat(m):
    tag, attrs, name, rest = m.group(1), m.group(2), m.group(3), m.group(4)
    slug = MATIMG.get(name)
    if not slug or slug not in IMG_OK:
        return m.group(0)
    return f'<{tag} class="mat ph"{attrs}><img src="{{img}}{slug}.jpg" alt="" loading="lazy"><span class="mb"><b>{name}</b>{rest}</span></{tag}>'

def fhero(slug, alt, lang):
    if slug not in IMG or slug not in IMG_OK:
        return ""
    f, a, l = IMG[slug]
    if lang == "ca":
        l = {"Dominio público": "Domini públic", "Atribución": "Atribució"}.get(l, l)
        a = a.replace("Autor desconocido", "Autor desconegut")
    return (f'<figure class="fhero"><img src="{{img}}{slug}.jpg" alt="{alt}" loading="lazy">'
            f'<figcaption>{a} · {l} · <a href="{C}{f.replace(" ", "_")}" rel="noopener">Wikimedia Commons</a></figcaption></figure>')

HERO = {"eticas": "s-etica", "moral": "s-moral", "contratos": "s-contratos", "curiosidades": "s-curiosidades",
        "catalunya": "s-catalunya", "trabajo": "m-trabajo", "jubilacion": "s-jubilacion", "nomina": "s-nomina",
        "etica": "s-pena", "divorcio": "s-divorcio", "matrimonio": "s-matrimonio", "novedades": "s-boe",
        "vivienda": "m-vivienda", "familia": "m-familia", "sucesiones": "m-sucesiones", "consumo": "m-consumo",
        "autonomos": "m-autonomos", "fiscalidad": "m-fiscalidad", "segsocial": "s-jubilacion", "extranjeria": "m-extranjeria",
        "administracion": "m-administracion", "datos": "m-datos"}

for pid, pg in PAGES.items():
    for L in ("es", "ca"):
        if L not in pg or "html" not in pg[L]:
            continue
        h = re.sub(r'<(a|div) class="mat"([^>]*)><b>([^<]+)</b>(.*?)</\1>', _mat, pg[L]["html"], flags=re.S)
        slug = HERO.get(pid)
        if slug:
            fig = fhero(slug, pg[L]["title"], L)
            if fig:
                if '<article class="prose">' in h:
                    h = h.replace('<article class="prose">', '<article class="prose">' + fig, 1)
                elif 'class="prose-wide">' in h:
                    h = h.replace('class="prose-wide">', 'class="prose-wide">' + fig, 1)
        pg[L]["html"] = h
