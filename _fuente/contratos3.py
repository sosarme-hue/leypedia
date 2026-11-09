# -*- coding: utf-8 -*-
# 45 contratos más con el motor genérico (50 en total) y catálogo por categorías
import json
from leysite import *
from cbase import LISTA, FIRMA_ES, FIRMA_CA
import c_vivienda, c_bienes, c_trabajo, c_tramites  # noqa: F401 (rellenan LISTA)

def kc(cid):
    return "c" + "".join(ch for ch in cid if ch.isalpha())

CATS = [("vivienda", "Vivienda y alquiler", "Habitatge i lloguer"), ("bienes", "Compraventa y objetos", "Compravenda i objectes"),
        ("dinero", "Dinero y deudas", "Diners i deutes"), ("trabajo", "Trabajo y negocios", "Feina i negocis"),
        ("tramites", "Autorizaciones y trámites", "Autoritzacions i tràmits"), ("consumo", "Consumo y datos personales", "Consum i dades personals"),
        ("familia", "Familia y herencias", "Família i herències")]
CATN = {c: (a, b) for c, a, b in CATS}
# los cinco contratos con plantilla propia
BASE5 = [("calquiler", "vivienda", "alquiler"), ("chabitacion", "vivienda", "habitacion"), ("cgaraje", "vivienda", "garaje"), ("ccoche", "bienes", "coche"), ("contrato", "dinero", "prestamo")]

def localize(f, es):
    if isinstance(f, list):
        return [localize(x, es) for x in f]
    if f[3] == "text":
        ph = f[5][0 if es else 1]
        return (f[0], f[1], f[2], "text", f[4], f'placeholder="{ph}"' if ph else "")
    if f[3] == "area":
        return (f[0], f[1], f[2], "area", "", f[5][0 if es else 1])
    return f

def gform(c, es):
    fs = [localize(x, es) for x in c["f"]]
    ids = set()
    def walk(x):
        for y in (x if isinstance(x, list) else [x]):
            if isinstance(y, list): walk(y)
            else: ids.add(y[0])
    walk(fs)
    if "ci" not in ids:
        fs.append(("ci", "Ciudad", "Ciutat", "text", "Barcelona", ""))
    rows = "".join(('<div class="row2">' + "".join(field(x, es) for x in f) + '</div>') if isinstance(f, list) else field(f, es) for f in fs)
    hasname = any(x[3] == "name" for x in (y for f in fs for y in (f if isinstance(f, list) else [f])))
    bl = (f'<label class="check" for="bl"><input id="bl" type="checkbox"> {"Dejar los nombres en blanco para rellenarlos a mano" if es else "Deixar els noms en blanc per omplir-los a mà"}</label>') if hasname else '<input id="bl" type="checkbox" hidden>'
    return (f'<form class="form" id="f" autocomplete="off">{rows}{bl}'
            f'<p class="safe">{"Tus datos no salen de este navegador: no se envían ni se guardan." if es else "Les teves dades no surten d&#39;aquest navegador: no s&#39;envien ni es desen."}</p></form>')

def gpage(c, lang):
    es = lang == "es"
    i = 0 if es else 1
    data = {"t": c["t"][i].upper(), "i": c["intro"][i], "c": c["c"][i], "s": c["s"][i], "f": (FIRMA_ES if es else FIRMA_CA) if c["firma"] else ""}
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    cat = CATN[c["cat"]][i]
    meta = [("Precio" if es else "Preu", "Gratis" if es else "Gratuït"), ("Norma" if es else "Norma", c["ley"][i])]
    m = "".join(f'<div><span class="status">{a}</span><b>{b}</b></div>' for a, b in meta)
    return f'''<div class="wrap"><div class="fhead"><span class="label">{("Contrato · " if es else "Contracte · ") + cat}</span>
<h1>{c["t"][i]}</h1>
<p class="lead">{c["lead"][i]} {"Rellena los datos y el documento se escribe solo, en tu navegador." if es else "Omple les dades i el document s&#39;escriu sol, al teu navegador."}</p>
<div class="meta">{m}</div></div>
<div class="gen" style="padding-block:24px 46px">{gform(c, es)}
<div style="min-width:0"><article class="doc" id="doc" aria-live="polite" data-tipo="gen"></article>
<script type="application/json" id="cdata">{js}</script>
<div class="actions"><button type="button" id="copiar">{"Copiar texto" if es else "Copiar el text"}</button><button type="button" class="ghost" id="imprimir">{"Imprimir o guardar en PDF" if es else "Imprimir o desar en PDF"}</button><button type="button" class="ghost" id="borrar">{"Borrar datos" if es else "Esborrar les dades"}</button><span class="status" id="cmsg"></span></div>
<div class="box" style="margin-top:16px"><h3>{"Consejos" if es else "Consells"}</h3>{ul(c["tips"][i])}</div>
<div class="box cc" style="margin-top:16px"><h3>{"En Catalunya" if es else "A Catalunya"}</h3><p>{c["catn"][i]}</p></div>
<p class="disc">{"Modelo orientativo. Revísalo con un profesional si el caso tiene particularidades." if es else "Model orientatiu. Revisa'l amb un professional si el cas té particularitats."}</p>
{vig(lang, c["ley"][i])}</div></div></div>'''

for c in LISTA:
    key = kc(c["id"])
    assert key not in ROUTES, key
    ROUTES[key] = (f"contratos/{c['slug'][0]}/", f"ca/contractes/{c['slug'][1]}/")
    PARENT[key] = "contratos"
    PAGES[key] = {L: dict(title=c["t"][0 if L == "es" else 1],
        desc=c["lead"][0 if L == "es" else 1],
        crumbs=[("contratos", "Contratos" if L == "es" else "Contractes")], html=gpage(c, L)) for L in ("es", "ca")}

def cidx2(lang):
    es = lang == "es"
    i = 0 if es else 1
    items = {cat: [] for cat, _, _ in CATS}
    for key, cat, t in BASE5:
        items[cat].append((key, CT[t][i], CT[t][2 + i]))
    for c in LISTA:
        items[c["cat"]].append((kc(c["id"]), c["t"][i], c["lead"][i]))
    total = sum(len(v) for v in items.values())
    out = (f'<div class="box cc"><h3>{"Tus datos están seguros" if es else "Les teves dades estan segures"}</h3><p>{"Los documentos se escriben en tu propio navegador. Los nombres y datos que pongas no se envían a ningún servidor, no se guardan y se borran al cerrar la página. También puedes dejar los nombres en blanco y escribirlos a mano después de imprimir." if es else "Els documents s&#39;escriuen al teu propi navegador. Els noms i les dades que hi posis no s&#39;envien a cap servidor, no es desen i s&#39;esborren en tancar la pàgina. També pots deixar els noms en blanc i escriure&#39;ls a mà després d&#39;imprimir."}</p></div>'
           f'<p class="status" style="margin-top:14px">{total} {"modelos gratuitos" if es else "models gratuïts"}</p>')
    nav = '<div class="subt">' + "".join(f'<a href="#{cat}">{CATN[cat][i]}</a>' for cat, _, _ in CATS) + '</div>'
    for cat, _, _ in CATS:
        out += f'<section class="cgroup" id="{cat}"><h2>{CATN[cat][i]}</h2><div class="clinks">' + "".join(
            f'<a href="{{{k_}}}">{t}<span>{d[:110] + ("…" if len(d) > 110 else "")}</span></a>' for k_, t, d in items[cat]) + '</div></section>'
    return nav + out

PAGES["contratos"] = {
 "es": dict(title="Contratos y modelos", desc="50 modelos gratuitos de los contratos y escritos más usados: alquiler, compraventa, deudas, trabajo, consumo, autorizaciones y familia.", crumbs=[],
   html=simple("Contratos", "Los 50 contratos y escritos más usados", "Modelos claros y gratuitos para el día a día, en castellano y en catalán. Se rellenan en tu navegador y tus datos no salen de tu ordenador.", cidx2("es"))),
 "ca": dict(title="Contractes i models", desc="50 models gratuïts dels contractes i escrits més utilitzats: lloguer, compravenda, deutes, feina, consum, autoritzacions i família.", crumbs=[],
   html=simple("Contractes", "Els 50 contractes i escrits més utilitzats", "Models clars i gratuïts per al dia a dia, en castellà i en català. S'omplen al teu navegador i les teves dades no surten del teu ordinador.", cidx2("ca"))),
}
print(len(LISTA) + 5, "contratos")
