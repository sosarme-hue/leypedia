# -*- coding: utf-8 -*-
# Montaje final: menú, portada con fotos, historia, buscador
from contratos2 import *

ROUTES["buscar"] = ("buscar/", "ca/cercar/")

UI["es"]["nav"] = [("materias", "Materias"), ("novedades", "Novedades"), ("contratos", "Contratos"), ("catalunya", "Catalunya"), ("internacional", "UE e internacional"), ("historia", "Historia"), ("eticas", "Ética"), ("moral", "Moral")]
UI["ca"]["nav"] = [("materias", "Matèries"), ("novedades", "Novetats"), ("contratos", "Contractes"), ("catalunya", "Catalunya"), ("internacional", "UE i internacional"), ("historia", "Història"), ("eticas", "Ètica"), ("moral", "Moral")]

# Sección a la que pertenece cada página (para marcar el menú)
PARENT = {"vivienda": "materias", "cambio": "materias", "pregunta": "materias",
          "contrato": "contratos", "calquiler": "contratos", "chabitacion": "contratos", "ccoche": "contratos", "cgaraje": "contratos",
          "ue": "internacional", "transfronterizo": "internacional",
          "hito": "historia", "bio": "historia", "juicio": "historia", "enciclopedia": "historia",
          "etica": "eticas", "eutanasia": "eticas", "divorcio": "moral", "matrimonio": "moral"}
for e in E:
    PARENT["e" + k(e[0])] = "historia"
for s in P:
    PARENT["p" + k(s)] = "historia"

# Ámbitos para filtrar el buscador
def ambitos(pid, html):
    a = set()
    if PARENT.get(pid) == "historia" or pid == "historia":
        a.add("hist")
    if pid in ("internacional", "ue", "transfronterizo"):
        a.add("ue")
    if pid == "catalunya" or "box cc" in html or "Catalunya" in html[:3000]:
        a.add("cat")
    if pid not in ("internacional", "ue"):
        a.add("es")
    return sorted(a)

AMB = {"es": [("", "Todo"), ("es", "España"), ("cat", "Catalunya"), ("ue", "Europa"), ("hist", "Historia")],
       "ca": [("", "Tot"), ("es", "Espanya"), ("cat", "Catalunya"), ("ue", "Europa"), ("hist", "Història")]}

def searchbox(lang, big=False):
    es = lang == "es"
    chips = "".join(f'<label class="chip"><input type="radio" name="a" value="{v}"{" checked" if not v else ""}><span>{t}</span></label>' for v, t in AMB[lang])
    return (f'<form class="search{" big" if big else ""}" action="{{buscar}}" method="get" role="search">'
            f'<label class="vh" for="q{"b" if big else ""}">{"Buscar en Leypedia" if es else "Cercar a Leypedia"}</label>'
            f'<div class="sbar"><input id="q{"b" if big else ""}" name="q" type="search" autocomplete="off" placeholder="{"Busca una ley, una duda o un contrato" if es else "Cerca una llei, un dubte o un contracte"}">'
            f'<button type="submit">{"Buscar" if es else "Cercar"}</button></div>'
            + (f'<div class="chips">{chips}</div>' if big else "") + '</form>')

def home2(lang):
    es = lang == "es"
    T = lambda a, b: a if es else b
    hero = f'''<div class="hero"><div class="wrap">
<div><span class="label">{T("Legislación española, catalana y europea", "Legislació espanyola, catalana i europea")}</span>
<h1>{T("Comprende la ley. <em>Resuelve tus dudas.</em> Prepara tus documentos.", "Comprèn la llei. <em>Resol els teus dubtes.</em> Prepara els teus documents.")}</h1>
<p>{T("Legislación española, catalana y europea explicada con claridad, con fuentes y fechas de actualización.", "Legislació espanyola, catalana i europea explicada amb claredat, amb fonts i dates d'actualització.")}</p>
{searchbox(lang, True)}</div>
<aside class="panel diarios" id="boe-panel" data-lang="{lang}"><div class="label">{T("Diarios oficiales · hoy", "Diaris oficials · avui")}</div>
<a class="diario" href="{{novedades}}"><span class="sig">BOE</span><span class="dt"><b><span id="boe-total">—</span> {T("disposiciones", "disposicions")}</b><span id="boe-fecha">{T("Boletín Oficial del Estado", "Boletín Oficial del Estado")}</span></span><span class="go">›</span></a>
<a class="diario" href="{{novedades}}#dogc"><span class="sig cat">DOGC</span><span class="dt"><b id="dogc-n">{T("Diari Oficial", "Diari Oficial")}</b><span id="dogc-fecha">Diari Oficial de la Generalitat de Catalunya</span></span><span class="go">›</span></a>
<a class="diario" href="{{novedades}}#ue"><span class="sig ue">UE</span><span class="dt"><b id="ue-n">EUR-Lex</b><span id="ue-fecha">{T("Diario Oficial de la Unión Europea", "Diari Oficial de la Unió Europea")}</span></span><span class="go">›</span></a>
</aside>
</div></div>'''
    caminos = f'''<div class="home-block"><div class="wrap"><div class="caminos">
<div class="camino"><h2>{T("Comprender", "Comprendre")}</h2><p>{T("La ley explicada por materias, las novedades del BOE y el DOGC, y la historia y la ética del derecho.", "La llei explicada per matèries, les novetats del BOE i el DOGC, i la història i l'ètica del dret.")}</p>
<p class="links"><a href="{{materias}}">{T("Materias", "Matèries")}</a><a href="{{novedades}}">{T("Novedades", "Novetats")}</a><a href="{{enciclopedia}}">{T("Enciclopedia", "Enciclopèdia")}</a></p></div>
<div class="camino dark"><h2>{T("Preparar", "Preparar")}</h2><p>{T("Los contratos más usados, gratis y en tu navegador: alquiler, habitación, compraventa de coche, garaje y préstamo.", "Els contractes més utilitzats, gratis i al teu navegador: lloguer, habitació, compravenda de cotxe, garatge i préstec.")}</p>
<p class="links"><a href="{{contratos}}">{T("Ver los contratos", "Veure els contractes")}</a></p></div>
</div></div></div>'''
    inst = [("home-congreso", "novedades", T("Las Cortes Generales", "Les Corts Generals"), T("Aprueban las leyes del Estado, que se publican en el BOE.", "Aproven les lleis de l'Estat, que es publiquen al BOE.")),
            ("home-parlament", "catalunya", T("El Parlament de Catalunya", "El Parlament de Catalunya"), T("Legisla en las materias que son competencia de la Generalitat.", "Legisla en les matèries que són competència de la Generalitat.")),
            ("home-berlaymont", "internacional", T("La Unión Europea", "La Unió Europea"), T("Sus reglamentos se aplican directamente en España.", "Els seus reglaments s'apliquen directament a Espanya."))]
    fotos = ('<div class="home-block"><div class="wrap"><h2>' + T("Quién hace las leyes que te afectan", "Qui fa les lleis que t'afecten") + '</h2><p>' + T("Cada ficha te dice qué norma se aplica y de dónde viene: del Estado, de Catalunya o de Europa.", "Cada fitxa et diu quina norma s'aplica i d'on ve: de l'Estat, de Catalunya o d'Europa.") + '</p><div class="cols">'
             + "".join(f'<div class="card photo">{foto(img, t, lang, "foto top")}<h3><a href="{{{key}}}">{t}</a></h3><p>{d}</p></div>' for img, key, t, d in inst) + '</div></div></div>')
    mats = f'''<div class="home-block"><div class="wrap"><h2>{T("Materias", "Matèries")}</h2>
<p>{T("Toda la parte práctica se organiza por materias, con la ley estatal y lo que cambia en Catalunya.", "Tota la part pràctica s'organitza per matèries, amb la llei estatal i el que canvia a Catalunya.")}</p>{mats_grid(lang)}</div></div>'''
    cts = [("calquiler", CT["alquiler"]), ("chabitacion", CT["habitacion"]), ("ccoche", CT["coche"]), ("cgaraje", CT["garaje"]), ("contrato", CT["prestamo"])]
    contratos = (f'<div class="home-block contracts"><div class="wrap"><h2>{T("Contratos gratis para el día a día", "Contractes gratuïts per al dia a dia")}</h2>'
                 f'<p>{T("Se rellenan en tu navegador. Tus datos no se envían ni se guardan.", "S&#39;omplen al teu navegador. Les teves dades no s&#39;envien ni es desen.")}</p><div class="clist">'
                 + "".join(f'<a href="{{{key}}}">{t[0] if es else t[1]}</a>' for key, t in cts) + '</div></div></div>')
    pers = ["alfonso-x", "jaime-i", "concepcion-arenal", "clara-campoamor", "macia", "tarradellas"]
    enc = (f'<div class="home-block"><div class="wrap"><div class="enc">{foto("home-cortes-cadiz", T("Promulgación de la Constitución de 1812", "Promulgació de la Constitució del 1812"), lang, "foto wide")}'
           f'<div><span class="label">{T("Enciclopedia", "Enciclopèdia")}</span><h2>{T("La historia del derecho en España y Catalunya", "La història del dret a Espanya i Catalunya")}</h2>'
           f'<p>{T("De las leyes de bronce de Roma al Codi civil de Catalunya: veintiuna épocas, sus anécdotas y las personas que las protagonizaron.", "De les lleis de bronze de Roma al Codi civil de Catalunya: vint-i-una èpoques, les seves anècdotes i les persones que les van protagonitzar.")}</p>'
           f'<p><a class="btn" href="{{enciclopedia}}">{T("Abrir la enciclopedia", "Obrir l&#39;enciclopèdia")}</a></p></div></div>'
           '<div class="perslist mini">' + "".join(pcard(s, lang) for s in pers) + '</div></div></div>')
    em = (f'<div class="home-block"><div class="wrap"><div class="cols two">'
          f'<a class="card" href="{{eticas}}"><span class="label">{T("Ética", "Ètica")}</span><h3>{T("¿Lo legal es siempre justo?", "El que és legal és sempre just?")}</h3><p>{T("Pena de muerte, eutanasia, inteligencia artificial: los grandes debates con los argumentos de cada lado.", "Pena de mort, eutanàsia, intel·ligència artificial: els grans debats amb els arguments de cada banda.")}</p><span class="go">{T("Entrar en Ética", "Entrar a Ètica")}</span></a>'
          f'<a class="card" href="{{moral}}"><span class="label">Moral</span><h3>{T("Lo que antes era delito", "El que abans era delicte")}</h3><p>{T("Divorcio, matrimonio, voto de la mujer: cómo han cambiado las costumbres y las leyes con ellas.", "Divorci, matrimoni, vot de la dona: com han canviat els costums i les lleis amb ells.")}</p><span class="go">{T("Entrar en Moral", "Entrar a Moral")}</span></a>'
          '</div></div></div>')
    return hero + caminos + fotos + mats + contratos + enc + em

for L in ("es", "ca"):
    PAGES["home"][L]["html"] = home2(L)

def historia3(lang):
    es = lang == "es"
    items = [("hito", "Historia del derecho" if es else "Història del dret", "Las Siete Partidas" if es else "Les Siete Partidas"),
             ("bio", "Biografía" if es else "Biografia", "Clara Campoamor"),
             ("juicio", "Juicio célebre" if es else "Judici cèlebre", "Los juicios de Núremberg" if es else "Els judicis de Nuremberg")]
    enc = (f'<a class="card enc-cta" href="{{enciclopedia}}"><img src="{{img}}doc-usatges.jpg" alt="" loading="lazy" style="width:100%;border-radius:6px"><div><span class="label">{"Enciclopedia" if es else "Enciclopèdia"}</span>'
           f'<h3>{"Historia del derecho en España y Catalunya" if es else "Història del dret a Espanya i Catalunya"}</h3><p>{"Veintiuna épocas y más de setenta personajes con su ficha y su retrato." if es else "Vint-i-una èpoques i més de setanta personatges amb la seva fitxa i el seu retrat."}</p><span class="go">{"Abrir la enciclopedia" if es else "Obrir l&#39;enciclopèdia"}</span></div></a>')
    return (enc + '<div class="cols" style="margin-top:16px">' + "".join(f'<a class="card" href="{{{k_}}}"><span class="label">{l}</span><h3>{t}</h3><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>' for k_, l, t in items) + '</div>'
      + f'<h2 class="sec">{"Línea del tiempo" if es else "Línia del temps"}</h2>' + tl(TL_ES if es else TL_CA)
      + f'<p class="status">{"La ética y la moral tienen ahora sus propias secciones: " if es else "L&#39;ètica i la moral tenen ara les seves pròpies seccions: "}<a href="{{eticas}}">{"Ética" if es else "Ètica"}</a> · <a href="{{moral}}">Moral</a>.</p>')

PAGES["historia"] = {
 "es": dict(title="Historia del derecho", desc="La historia del derecho en España y Catalunya: enciclopedia por épocas, biografías, juicios célebres y línea del tiempo.", crumbs=[],
   html=simple("Historia", "Historia del derecho", "De dónde vienen nuestras leyes y quién las hizo.", historia3("es"))),
 "ca": dict(title="Història del dret", desc="La història del dret a Espanya i Catalunya: enciclopèdia per èpoques, biografies, judicis cèlebres i línia del temps.", crumbs=[],
   html=simple("Història", "Història del dret", "D'on vénen les nostres lleis i qui les va fer.", historia3("ca"))),
}
for L in ("es", "ca"):
    for pid in ("hito", "juicio"):
        PAGES[pid][L]["crumbs"] = [("historia", "Historia" if L == "es" else "Història")]
    # enlaces antiguos a "Historia y ética"
    for pid in PAGES:
        p = PAGES[pid][L]
        p["html"] = p["html"].replace("Historia y ética", "Historia").replace("Història i ètica", "Història")

def buscar_page(lang):
    es = lang == "es"
    return simple("Buscador" if es else "Cercador", "Buscar en Leypedia" if es else "Cercar a Leypedia",
                  "Busca en todas las fichas, preguntas, contratos y la enciclopedia." if es else "Cerca a totes les fitxes, preguntes, contractes i l'enciclopèdia.",
                  searchbox(lang, True) + f'<p class="status" id="sinfo" aria-live="polite"></p><ol class="results" id="sres" data-lang="{lang}"></ol>')
PAGES["buscar"] = {
 "es": dict(title="Buscar", desc="Buscador de Leypedia.", crumbs=[], html=buscar_page("es")),
 "ca": dict(title="Cercar", desc="Cercador de Leypedia.", crumbs=[], html=buscar_page("ca")),
}

# ---------- Novedades: BOE, DOGC y EUR-Lex ----------
def nov2(lang):
    es = lang == "es"
    f = ["Qué se ha publicado", "Qué cambia", "A quién afecta", "Desde cuándo", "Qué hay que hacer", "Régimen transitorio", "Fuente"] if es else ["Què s'ha publicat", "Què canvia", "A qui afecta", "Des de quan", "Què cal fer", "Règim transitori", "Font"]
    def bloque(h, info_id, info, lista, extra=""):
        return f'<h2>{h}</h2><p class="status" id="{info_id}">{info}</p><ul class="dispo" {lista}></ul>{extra}'
    carga = "Se cargan cada día de la fuente oficial cuando la web está publicada." if es else "Es carreguen cada dia de la font oficial quan la web està publicada."
    return (f'<div class="fbody" style="padding-block:0"><div class="prose" style="max-width:none">'
      + bloque("Boletín Oficial del Estado · disposiciones generales" if es else "Boletín Oficial del Estado · disposicions generals", "boe-info", carga, f'id="boe-list" data-lang="{lang}"')
      + '<span id="dogc"></span>' + bloque("Diari Oficial de la Generalitat de Catalunya", "dogc-info", carga, 'data-feed="dogc" data-info="dogc-info"')
      + '<span id="ue"></span>' + bloque("EUR-Lex · Diario Oficial de la Unión Europea", "ue-info", carga, 'data-feed="ue" data-info="ue-info"')
      + f'<p class="status">{"Los títulos se muestran tal como los publica cada diario oficial, sin traducir. Se actualizan automáticamente cada día." if es else "Els títols es mostren tal com els publica cada diari oficial, sense traduir. S&#39;actualitzen automàticament cada dia."}</p></div>'
      + f'<aside class="side"><div class="box"><h3>{"Cada novedad explicada responde a" if es else "Cada novetat explicada respon a"}</h3><ol style="margin:0;padding-left:20px;font-size:14px">{"".join(f"<li>{x}</li>" for x in f)}</ol></div>'
      + box("Fuentes oficiales" if es else "Fonts oficials", ul(['<a href="https://www.boe.es/" rel="noopener">Boletín Oficial del Estado</a>', '<a href="https://dogc.gencat.cat/" rel="noopener">Diari Oficial de la Generalitat de Catalunya</a>', '<a href="https://portaljuridic.gencat.cat/" rel="noopener">Portal Jurídic de Catalunya</a>', '<a href="https://eur-lex.europa.eu/" rel="noopener">EUR-Lex</a>']))
      + '</aside></div>')

PAGES["novedades"] = {
 "es": dict(title="Novedades del BOE, el DOGC y la UE", desc="Lo último publicado en el Boletín Oficial del Estado, el Diari Oficial de la Generalitat de Catalunya y el Diario Oficial de la Unión Europea, actualizado cada día.", crumbs=[],
   html=simple("Novedades", "Novedades del BOE, el DOGC y la UE", "Lo que se ha publicado en los diarios oficiales, actualizado cada día y con enlace al texto original.", nov2("es"))),
 "ca": dict(title="Novetats del BOE, el DOGC i la UE", desc="L'últim publicat al Boletín Oficial del Estado, al Diari Oficial de la Generalitat de Catalunya i al Diario Oficial de la Unión Europea, actualitzat cada dia.", crumbs=[],
   html=simple("Novetats", "Novetats del BOE, el DOGC i la UE", "El que s'ha publicat als diaris oficials, actualitzat cada dia i amb enllaç al text original.", nov2("ca"))),
}
