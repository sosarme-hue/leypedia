# -*- coding: utf-8 -*-
# Contenido de Leypedia (fase 1: España y Catalunya). Cada página tiene versión es y ca.

MATERIAS = [
  # slug_es, slug_ca, es, ca, desc_es, desc_ca, varia_cat
  ("vivienda","habitatge","Vivienda","Habitatge","Alquiler, compraventa, vecinos","Lloguer, compravenda, veïns",True),
  ("trabajo","treball","Trabajo","Treball","Contratos, despidos, vacaciones","Contractes, acomiadaments, vacances",False),
  ("familia","familia","Familia","Família","Matrimonio, divorcio, custodia","Matrimoni, divorci, custòdia",True),
  ("sucesiones","successions","Sucesiones","Successions","Herencias, testamentos, impuesto","Herències, testaments, impost",True),
  ("consumo","consum","Consumo","Consum","Devoluciones, garantías, reclamaciones","Devolucions, garanties, reclamacions",True),
  ("autonomos-y-empresas","autonoms-i-empreses","Autónomos y empresas","Autònoms i empreses","Alta, cuotas, sociedades, ayudas","Alta, quotes, societats, ajuts",True),
  ("fiscalidad","fiscalitat","Fiscalidad","Fiscalitat","IRPF, IVA, tributos catalanes","IRPF, IVA, tributs catalans",True),
  ("seguridad-social","seguretat-social","Seguridad Social","Seguretat Social","Pensiones, bajas, prestaciones","Pensions, baixes, prestacions",False),
  ("extranjeria","estrangeria","Extranjería","Estrangeria","Residencia, arraigo, nacionalidad","Residència, arrelament, nacionalitat",False),
  ("administracion","administracio","Administración","Administració","Multas, recursos, plazos","Multes, recursos, terminis",True),
  ("proteccion-de-datos","proteccio-de-dades","Protección de datos","Protecció de dades","RGPD, tus derechos, reclamar","RGPD, els teus drets, reclamar",False),
]

# id: (ruta_es, ruta_ca)
ROUTES = {
  "home": ("", "ca/"),
  "materias": ("materias/", "ca/materies/"),
  "vivienda": ("materias/vivienda/", "ca/materies/habitatge/"),
  "novedades": ("novedades/", "ca/novetats/"),
  "cambio": ("cambios/ley-de-vivienda/", "ca/canvis/llei-de-l-habitatge/"),
  "pregunta": ("preguntas/preaviso-para-dejar-un-alquiler/", "ca/preguntes/preavis-per-deixar-un-lloguer/"),
  "contrato": ("contratos/prestamo-entre-particulares/", "ca/contractes/prestec-entre-particulars/"),
  "historia": ("historia/", "ca/historia/"),
  "hito": ("historia/siete-partidas/", "ca/historia/set-partides/"),
  "bio": ("biografias/clara-campoamor/", "ca/biografies/clara-campoamor/"),
  "juicio": ("juicios/nuremberg/", "ca/judicis/nuremberg/"),
  "etica": ("etica/pena-de-muerte/", "ca/etica/pena-de-mort/"),
  "catalunya": ("catalunya/", "ca/catalunya/"),
  "aviso": ("aviso-legal/", "ca/avis-legal/"),
  "privacidad": ("privacidad/", "ca/privacitat/"),
  "cookies": ("cookies/", "ca/galetes/"),
}

UI = {
 "es": {
  "nav": [("home","Inicio"),("materias","Materias"),("novedades","Novedades"),("contrato","Contratos"),("catalunya","Catalunya"),("historia","Historia y ética")],
  "tagline": "Comprende la ley. Resuelve tus dudas. Prepara tus documentos.",
  "aviso": "<b>Aviso legal.</b> Leypedia ofrece información jurídica general y no presta asesoramiento legal. No es un despacho de abogados y lo que escribas aquí no está protegido por el secreto profesional. Para un caso concreto, consulta con un abogado colegiado.",
  "fuentes": "Los textos legales proceden del Boletín Oficial del Estado (BOE) y del Diari Oficial de la Generalitat de Catalunya (DOGC). La versión con valor jurídico es siempre la publicada en el diario oficial.",
  "legal": [("aviso","Aviso legal"),("privacidad","Privacidad"),("cookies","Cookies")],
  "inicio": "Inicio", "vigente": "Vigente a", "otra": "Català", "otra_l": "ca", "cat_box": "En Catalunya",
 },
 "ca": {
  "nav": [("home","Inici"),("materias","Matèries"),("novedades","Novetats"),("contrato","Contractes"),("catalunya","Catalunya"),("historia","Història i ètica")],
  "tagline": "Comprèn la llei. Resol els teus dubtes. Prepara els teus documents.",
  "aviso": "<b>Avís legal.</b> Leypedia ofereix informació jurídica general i no presta assessorament legal. No és un despatx d'advocats i el que hi escriguis no està protegit pel secret professional. Per a un cas concret, consulta un advocat col·legiat.",
  "fuentes": "Els textos legals provenen del Boletín Oficial del Estado (BOE) i del Diari Oficial de la Generalitat de Catalunya (DOGC). La versió amb valor jurídic és sempre la publicada al diari oficial.",
  "legal": [("aviso","Avís legal"),("privacidad","Privacitat"),("cookies","Galetes")],
  "inicio": "Inici", "vigente": "Vigent a", "otra": "Castellano", "otra_l": "es", "cat_box": "A Catalunya",
 },
}

REV = "9 de noviembre de 2026"
REV_CA = "9 de novembre de 2026"

def ficha(label, h1, lead, meta, body, side):
    m = "".join(f'<div><span class="status">{k}</span><b>{v}</b></div>' for k,v in meta)
    return f'''<div class="wrap">
<div class="fhead"><span class="label">{label}</span><h1>{h1}</h1><p class="lead">{lead}</p>{('<div class="meta">'+m+'</div>') if meta else ''}</div>
<div class="fbody"><article class="prose">{body}</article><aside class="side">{side}</aside></div></div>'''

def box(t, inner, cls="box"):
    return f'<div class="{cls}"><h3>{t}</h3>{inner}</div>'

def ul(items):
    return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"

def tl(items):
    return '<ol class="mini-tl">'+"".join(f'<li><span class="yr">{a}</span><br>{b}</li>' for a,b in items)+"</ol>"

def table(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>"+"".join(f"<td>{c}</td>" for c in row)+"</tr>" for row in rows)
    return f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'

def vig(lang, fuente):
    return f'<span class="vig">{UI[lang]["vigente"]} {REV if lang=="es" else REV_CA} · {fuente}</span>'

PAGES = {}

# ---------------- CAMBIO: LEY DE VIVIENDA ----------------
PAGES["cambio"] = {
 "es": dict(title="Qué cambió con la ley de vivienda", desc="Los cambios de la Ley 12/2023 por el derecho a la vivienda explicados, con su aplicación en Catalunya.",
  crumbs=[("materias","Materias"),("vivienda","Vivienda")],
  html=ficha("Cambio importante · Vivienda","Qué cambió con la ley de vivienda",
   "La ley estatal de vivienda de 2023 cambió las reglas del alquiler: quién paga la inmobiliaria, cuánto puede subir la renta y qué pasa en las zonas con precios más altos.",
   [("Norma","Ley 12/2023, de 24 de mayo"),("En vigor desde","26 de mayo de 2023"),("Afecta a","Inquilinos y propietarios")],
   '<div class="claro"><span class="label">En 30 segundos</span><p>Los gastos de la inmobiliaria los paga el propietario. Las comunidades autónomas pueden declarar zonas tensionadas, donde se limita la renta de los nuevos contratos. Y la subida anual de la renta ya no va ligada al IPC.</p></div>'
   +'<h2>Los cambios uno a uno</h2>'+table(["Tema","Antes","Ahora"],[
     ["Honorarios de la inmobiliaria","Se los solía cobrar al inquilino","Los paga siempre el propietario"],
     ["Subida anual de la renta","Según el IPC, si se pactaba","Topes del 2 % (2023) y 3 % (2024), y después un índice propio del INE"],
     ["Zonas tensionadas","No existían","La comunidad autónoma puede limitar la renta de los nuevos contratos"],
     ["Grandes tenedores","Sin regla especial","Desde 10 viviendas (o 5 en zona tensionada, si la comunidad lo decide), con más obligaciones"]])
   +'<h2>Cronología</h2>'+tl([("24 may 2023","Se aprueba la ley."),("mar 2024","Catalunya empieza a aplicar los límites de renta en zonas tensionadas."),("2025","Empieza a usarse el nuevo índice del INE para actualizar rentas.")])
   +vig("es","comprobado con el BOE y el DOGC"),
   box("En Catalunya",'<p>Catalunya fue la primera comunidad en aplicar los límites de renta en zonas tensionadas, desde marzo de 2024. La lista de municipios declarados se publica en el DOGC.</p>',"box cc")
   +box("Datos clave",'<dl><dt>Normas que modifica</dt><dd>Ley de Arrendamientos Urbanos y Ley de Enjuiciamiento Civil</dd></dl>')
   +box("Te puede servir",ul(['<a href="{pregunta}">¿Cuánto preaviso para dejar un piso?</a>','<a href="{contrato}">Contrato de préstamo entre particulares</a>'])))),
 "ca": dict(title="Què va canviar amb la llei de l'habitatge", desc="Els canvis de la Ley 12/2023 pel dret a l'habitatge explicats, amb la seva aplicació a Catalunya.",
  crumbs=[("materias","Matèries"),("vivienda","Habitatge")],
  html=ficha("Canvi important · Habitatge","Què va canviar amb la llei de l'habitatge",
   "La llei estatal de l'habitatge del 2023 va canviar les regles del lloguer: qui paga la immobiliària, quant pot pujar la renda i què passa a les zones amb preus més alts.",
   [("Norma","Ley 12/2023, de 24 de mayo"),("En vigor des del","26 de maig de 2023"),("Afecta","Llogaters i propietaris")],
   '<div class="claro"><span class="label">En 30 segons</span><p>Les despeses de la immobiliària les paga el propietari. Les comunitats autònomes poden declarar zones tensionades, on es limita la renda dels contractes nous. I la pujada anual de la renda ja no va lligada a l\'IPC.</p></div>'
   +'<h2>Els canvis un per un</h2>'+table(["Tema","Abans","Ara"],[
     ["Honoraris de la immobiliària","Se solien cobrar al llogater","Els paga sempre el propietari"],
     ["Pujada anual de la renda","Segons l'IPC, si es pactava","Topalls del 2 % (2023) i del 3 % (2024), i després un índex propi de l'INE"],
     ["Zones tensionades","No existien","La comunitat autònoma pot limitar la renda dels contractes nous"],
     ["Grans tenidors","Sense regla especial","A partir de 10 habitatges (o 5 en zona tensionada, si la comunitat ho decideix), amb més obligacions"]])
   +'<h2>Cronologia</h2>'+tl([("24 maig 2023","S'aprova la llei."),("març 2024","Catalunya comença a aplicar els límits de renda a les zones tensionades."),("2025","Es comença a fer servir el nou índex de l'INE per actualitzar rendes.")])
   +vig("ca","comprovat amb el BOE i el DOGC"),
   box("A Catalunya",'<p>Catalunya va ser la primera comunitat a aplicar els límits de renda a les zones tensionades, des del març de 2024. La llista de municipis declarats es publica al DOGC.</p>',"box cc")
   +box("Dades clau",'<dl><dt>Normes que modifica</dt><dd>Ley de Arrendamientos Urbanos i Ley de Enjuiciamiento Civil</dd></dl>')
   +box("Et pot servir",ul(['<a href="{pregunta}">Amb quanta antelació cal avisar per deixar un pis?</a>','<a href="{contrato}">Contracte de préstec entre particulars</a>'])))),
}

# ---------------- PREGUNTA ----------------
PAGES["pregunta"] = {
 "es": dict(title="¿Con cuánta antelación hay que avisar para dejar un piso de alquiler?", desc="Preaviso de 30 días a partir de 6 meses (art. 11 LAU), indemnización y fianza en Catalunya.",
  crumbs=[("materias","Materias"),("vivienda","Vivienda")],
  html=ficha("Pregunta · Alquiler","¿Con cuánta antelación tengo que avisar para dejar un piso de alquiler?",
   "Con 30 días, siempre que lleves al menos 6 meses en la vivienda.",
   [("Base legal",'<span class="mono">Art. 11 LAU</span>'),("Materia","Vivienda · Alquiler")],
   '<h2>La respuesta completa</h2><p>La ley de alquileres permite al inquilino irse antes de que acabe el contrato si se cumplen dos condiciones: haber vivido al menos <b>6 meses</b> en la vivienda y avisar al propietario con <b>30 días</b> de antelación.</p><p>El contrato puede decir que, si te vas antes, pagues una indemnización. Como máximo es <b>una mensualidad por cada año</b> que falte por cumplir, y los periodos más cortos se calculan en proporción.</p>'
   +'<h2>Ejemplo</h2><div class="claro"><span class="label">Caso práctico</span><p>Pagas 900 € al mes, tu contrato es de 5 años y te vas a los 3 años. Faltan 2 años, así que la indemnización máxima, si está en el contrato, sería de 1.800 €.</p></div>'
   +'<h2>Cómo avisar</h2><ol><li>Por escrito y de forma que quede constancia: burofax o email con acuse de recibo.</li><li>Indica la fecha en que dejarás la vivienda.</li><li>Pide fecha para devolver las llaves y revisar el piso, para recuperar la fianza.</li></ol>'
   +'<p class="disc">Información general, no asesoramiento jurídico. Tu contrato concreto puede tener cláusulas distintas.</p>'+vig("es","Ley 29/1994, versión consolidada del BOE"),
   box("En Catalunya",'<p>El preaviso de 30 días es igual en toda España, porque la ley de alquileres es estatal. Lo que cambia es la fianza: en Catalunya el propietario debe depositarla en el INCASÒL.</p>',"box cc")
   +box("Relacionado",ul(['<a href="{cambio}">Qué cambió con la ley de vivienda</a>'])))),
 "ca": dict(title="Amb quanta antelació cal avisar per deixar un pis de lloguer?", desc="Preavís de 30 dies a partir de 6 mesos (art. 11 LAU), indemnització i fiança a Catalunya.",
  crumbs=[("materias","Matèries"),("vivienda","Habitatge")],
  html=ficha("Pregunta · Lloguer","Amb quanta antelació he d'avisar per deixar un pis de lloguer?",
   "Amb 30 dies, sempre que hi hagis viscut com a mínim 6 mesos.",
   [("Base legal",'<span class="mono">Art. 11 LAU</span>'),("Matèria","Habitatge · Lloguer")],
   '<h2>La resposta completa</h2><p>La llei d\'arrendaments permet al llogater marxar abans que acabi el contracte si es compleixen dues condicions: haver viscut com a mínim <b>6 mesos</b> a l\'habitatge i avisar el propietari amb <b>30 dies</b> d\'antelació.</p><p>El contracte pot establir que, si marxes abans, paguis una indemnització. Com a màxim és <b>una mensualitat per cada any</b> que falti per complir, i els períodes més curts es calculen proporcionalment.</p>'
   +'<h2>Exemple</h2><div class="claro"><span class="label">Cas pràctic</span><p>Pagues 900 € al mes, el contracte és de 5 anys i marxes als 3 anys. En falten 2, així que la indemnització màxima, si consta al contracte, seria de 1.800 €.</p></div>'
   +'<h2>Com avisar</h2><ol><li>Per escrit i de manera que en quedi constància: burofax o correu amb justificant de recepció.</li><li>Indica la data en què deixaràs l\'habitatge.</li><li>Demana data per tornar les claus i revisar el pis, per recuperar la fiança.</li></ol>'
   +'<p class="disc">Informació general, no assessorament jurídic. El teu contracte concret pot tenir clàusules diferents.</p>'+vig("ca","Ley 29/1994, versió consolidada del BOE"),
   box("A Catalunya",'<p>El preavís de 30 dies és igual a tot Espanya, perquè la llei d\'arrendaments és estatal. El que canvia és la fiança: a Catalunya el propietari l\'ha de dipositar a l\'INCASÒL.</p>',"box cc")
   +box("Relacionat",ul(['<a href="{cambio}">Què va canviar amb la llei de l\'habitatge</a>'])))),
}

# ---------------- CONTRATO ----------------
FORM_ES = '''<form class="form" id="f" autocomplete="off">
<label for="pr">Quien presta<input id="pr" value="" placeholder="Nombre y apellidos"></label>
<label for="pt">Quien recibe el dinero<input id="pt" value="" placeholder="Nombre y apellidos"></label>
<div class="row2"><label for="im">Importe (€)<input id="im" type="number" min="1" step="50" value="6000"></label><label for="pl">Plazo (meses)<input id="pl" type="number" min="1" max="360" value="24"></label></div>
<div class="row2"><label for="in">Interés anual (%)<input id="in" type="number" min="0" max="20" step="0.25" value="0"></label><label for="ci">Ciudad<input id="ci" value="Girona"></label></div>
<label for="pa">Forma de pago<select id="pa"><option value="m">Cuotas mensuales</option><option value="u">Pago único al final</option></select></label>
<label class="check" for="bl"><input id="bl" type="checkbox"> Dejar los nombres en blanco para rellenarlos a mano</label>
<p class="safe">Tus datos no salen de este navegador: no se envían ni se guardan.</p></form>'''
FORM_CA = '''<form class="form" id="f" autocomplete="off">
<label for="pr">Qui presta<input id="pr" value="" placeholder="Nom i cognoms"></label>
<label for="pt">Qui rep els diners<input id="pt" value="" placeholder="Nom i cognoms"></label>
<div class="row2"><label for="im">Import (€)<input id="im" type="number" min="1" step="50" value="6000"></label><label for="pl">Termini (mesos)<input id="pl" type="number" min="1" max="360" value="24"></label></div>
<div class="row2"><label for="in">Interès anual (%)<input id="in" type="number" min="0" max="20" step="0.25" value="0"></label><label for="ci">Ciutat<input id="ci" value="Girona"></label></div>
<label for="pa">Forma de pagament<select id="pa"><option value="m">Quotes mensuals</option><option value="u">Pagament únic al final</option></select></label>
<label class="check" for="bl"><input id="bl" type="checkbox"> Deixar els noms en blanc per omplir-los a mà</label>
<p class="safe">Les teves dades no surten d'aquest navegador: no s'envien ni es desen.</p></form>'''

def contrato_page(lang):
    es = lang=="es"
    head = f'''<div class="wrap"><div class="fhead"><span class="label">{"Contrato · Gratis" if es else "Contracte · Gratuït"}</span>
<h1>{"Contrato de préstamo entre particulares" if es else "Contracte de préstec entre particulars"}</h1>
<p class="lead">{"Rellena los datos y el contrato se escribe solo. Todo ocurre en tu navegador: los datos no se envían ni se guardan en ningún servidor." if es else "Omple les dades i el contracte s'escriu sol. Tot passa al teu navegador: les dades no s'envien ni es desen a cap servidor."}</p>
<div class="meta"><div><span class="status">{"Precio" if es else "Preu"}</span><b>{"Gratis" if es else "Gratuït"}</b></div><div><span class="status">{"Trámite" if es else "Tràmit"}</span><b>{"Modelo 600 en 30 días hábiles" if es else "Model 600 en 30 dies hàbils"}</b></div></div></div>
<div class="gen" style="padding-block:24px 46px">{FORM_ES if es else FORM_CA}
<div style="min-width:0"><article class="doc" id="doc" aria-live="polite" data-lang="{lang}"></article>
<div class="actions"><button type="button" id="copiar">{"Copiar texto" if es else "Copiar el text"}</button><button type="button" class="ghost" id="borrar">{"Borrar datos" if es else "Esborrar les dades"}</button><span class="status" id="cmsg"></span></div>
<div class="box cc" style="margin-top:16px"><h3>{"En Catalunya" if es else "A Catalunya"}</h3><p>{"El modelo 600 se presenta ante la Agència Tributària de Catalunya. El préstamo está exento del impuesto, pero hay que declararlo." if es else "El model 600 es presenta davant l'Agència Tributària de Catalunya. El préstec està exempt de l'impost, però cal declarar-lo."}</p></div>
<p class="disc">{"Plantilla orientativa. Revísala con un profesional si el importe es alto o el caso tiene particularidades." if es else "Plantilla orientativa. Revisa-la amb un professional si l'import és alt o el cas té particularitats."}</p>
{vig(lang, "Ley del ITP y AJD" if es else "Ley del ITP y AJD")}</div></div></div>'''
    return head

PAGES["contrato"] = {
 "es": dict(title="Contrato de préstamo entre particulares", desc="Modelo gratuito de contrato de préstamo entre particulares que se rellena en el navegador, con el trámite del modelo 600 en Catalunya.", crumbs=[("contrato","Contratos")], html=contrato_page("es")),
 "ca": dict(title="Contracte de préstec entre particulars", desc="Model gratuït de contracte de préstec entre particulars que s'omple al navegador, amb el tràmit del model 600 a Catalunya.", crumbs=[("contrato","Contractes")], html=contrato_page("ca")),
}

# ---------------- HITO: SIETE PARTIDAS ----------------
PAGES["hito"] = {
 "es": dict(title="Las Siete Partidas", desc="El código de Alfonso X el Sabio: qué eran, sus siete partes y su influencia hasta América.",
  crumbs=[("historia","Historia y ética")],
  html=ficha("Historia del derecho · Edad Media","Las Siete Partidas","El código que Alfonso X mandó escribir para ordenar el derecho de Castilla. Estuvo vigente durante siglos y viajó hasta América.",
   [("Época","c. 1256–1265"),("Impulsor","Alfonso X el Sabio"),("Lugar","Reino de Castilla")],
   '<h2>Qué eran</h2><p>Una gran obra jurídica dividida en siete partes que recogía el derecho romano, el derecho de la Iglesia y las costumbres del reino. Se escribió en castellano y no en latín, algo poco habitual para un texto legal de la época.</p>'
   +'<h2>Las siete partes</h2>'+table(["Partida","Trata de"],[["Primera","Las fuentes del derecho y la Iglesia"],["Segunda","El rey, el reino y la guerra"],["Tercera","La justicia y los juicios"],["Cuarta","El matrimonio y la familia"],["Quinta","Los contratos"],["Sexta","Los testamentos y las herencias"],["Séptima","Los delitos y las penas"]])
   +'<h2>Su recorrido</h2>'+tl([("c. 1256","Comienza la redacción."),("1348","El Ordenamiento de Alcalá les da fuerza de ley como derecho supletorio."),("s. XVI–XIX","Se aplican en la América española."),("1889","El Código Civil las sustituye en España.")])
   +'<div class="claro"><span class="label">Curiosidad</span><p>La primera letra de cada una de las siete partidas forma el nombre de su autor: A-L-F-O-N-S-O.</p></div>',
   box("¿Y en Catalunya?",'<p>Catalunya no seguía las Partidas: tenía su propio derecho, con los <i>Usatges de Barcelona</i> y las Constitucions de Catalunya. De ahí viene que hoy tenga un Código civil propio.</p>',"box cc")
   +box("Relacionado",ul(['<a href="{bio}">Clara Campoamor</a>','<a href="{juicio}">Los juicios de Núremberg</a>','<a href="{etica}">La pena de muerte en España</a>'])))),
 "ca": dict(title="Les Siete Partidas", desc="El codi d'Alfons X el Savi: què eren, les seves set parts i la seva influència fins a Amèrica.",
  crumbs=[("historia","Història i ètica")],
  html=ficha("Història del dret · Edat Mitjana","Les Siete Partidas","El codi que Alfons X va fer escriure per ordenar el dret de Castella. Va ser vigent durant segles i va arribar fins a Amèrica.",
   [("Època","c. 1256–1265"),("Impulsor","Alfons X el Savi"),("Lloc","Regne de Castella")],
   '<h2>Què eren</h2><p>Una gran obra jurídica dividida en set parts que recollia el dret romà, el dret de l\'Església i els costums del regne. Es va escriure en castellà i no en llatí, una cosa poc habitual per a un text legal de l\'època.</p>'
   +'<h2>Les set parts</h2>'+table(["Partida","Tracta de"],[["Primera","Les fonts del dret i l'Església"],["Segona","El rei, el regne i la guerra"],["Tercera","La justícia i els judicis"],["Quarta","El matrimoni i la família"],["Cinquena","Els contractes"],["Sisena","Els testaments i les herències"],["Setena","Els delictes i les penes"]])
   +'<h2>El seu recorregut</h2>'+tl([("c. 1256","Comença la redacció."),("1348","L'Ordenament d'Alcalá els dona força de llei com a dret supletori."),("s. XVI–XIX","S'apliquen a l'Amèrica espanyola."),("1889","El Código Civil les substitueix a Espanya.")])
   +'<div class="claro"><span class="label">Curiositat</span><p>La primera lletra de cadascuna de les set partides forma el nom del seu autor: A-L-F-O-N-S-O.</p></div>',
   box("I a Catalunya?",'<p>Catalunya no seguia les Partides: tenia el seu propi dret, amb els <i>Usatges de Barcelona</i> i les Constitucions de Catalunya. D\'aquí ve que avui tingui un Codi civil propi.</p>',"box cc")
   +box("Relacionat",ul(['<a href="{bio}">Clara Campoamor</a>','<a href="{juicio}">Els judicis de Nuremberg</a>','<a href="{etica}">La pena de mort a Espanya</a>'])))),
}

# ---------------- BIO ----------------
PAGES["bio"] = {
 "es": dict(title="Clara Campoamor", desc="Biografía de Clara Campoamor, la abogada y diputada que defendió el voto femenino en las Cortes de 1931.",
  crumbs=[("historia","Historia y ética")],
  html=ficha("Biografía","Clara Campoamor","Abogada y diputada. Defendió en las Cortes de 1931 que las mujeres pudieran votar, casi sola y en contra de buena parte de su propio campo político.",
   [("Nació","Madrid, 12 feb 1888"),("Murió","Lausana (Suiza), 30 abr 1972"),("Profesión","Abogada y política")],
   '<h2>Su vida</h2>'+tl([("1888","Nace en Madrid en una familia modesta. Trabaja desde joven como modista, telegrafista y profesora."),("1924","Se licencia en Derecho y abre su propio despacho."),("1931","Es elegida diputada, cuando las mujeres podían ser elegidas pero aún no votar."),("1 oct 1931","Las Cortes aprueban el voto femenino por 161 votos a favor y 121 en contra."),("1933","Las mujeres votan por primera vez en unas elecciones generales."),("1936","Se exilia. Muere en Suiza sin volver a vivir en España.")])
   +'<h2>El gran debate</h2><p>Su principal rival en el debate fue otra mujer, Victoria Kent, que pedía aplazar el voto femenino porque temía que las mujeres votaran lo que les dijera la Iglesia. Campoamor respondió que un derecho no se concede según cómo se vaya a usar.</p>',
   box("Su obra",ul(["<i>El voto femenino y yo</i> (1935)"]))+box("Relacionado",ul(['<a href="{hito}">Las Siete Partidas</a>','<a href="{etica}">La pena de muerte en España</a>'])))),
 "ca": dict(title="Clara Campoamor", desc="Biografia de Clara Campoamor, l'advocada i diputada que va defensar el vot femení a les Corts del 1931.",
  crumbs=[("historia","Història i ètica")],
  html=ficha("Biografia","Clara Campoamor","Advocada i diputada. Va defensar a les Corts del 1931 que les dones poguessin votar, gairebé sola i en contra de bona part del seu propi camp polític.",
   [("Va néixer","Madrid, 12 febr. 1888"),("Va morir","Lausana (Suïssa), 30 abr. 1972"),("Professió","Advocada i política")],
   '<h2>La seva vida</h2>'+tl([("1888","Neix a Madrid en una família modesta. Treballa des de jove com a modista, telegrafista i professora."),("1924","Es llicencia en Dret i obre el seu propi despatx."),("1931","És elegida diputada, quan les dones podien ser elegides però encara no votar."),("1 oct. 1931","Les Corts aproven el vot femení per 161 vots a favor i 121 en contra."),("1933","Les dones voten per primera vegada en unes eleccions generals."),("1936","S'exilia. Mor a Suïssa sense tornar a viure a Espanya.")])
   +'<h2>El gran debat</h2><p>La seva principal rival en el debat va ser una altra dona, Victoria Kent, que demanava ajornar el vot femení perquè temia que les dones votessin el que els digués l\'Església. Campoamor va respondre que un dret no es concedeix segons com es farà servir.</p>',
   box("La seva obra",ul(["<i>El voto femenino y yo</i> (1935)"]))+box("Relacionat",ul(['<a href="{hito}">Les Siete Partidas</a>','<a href="{etica}">La pena de mort a Espanya</a>'])))),
}

# ---------------- JUICIO ----------------
PAGES["juicio"] = {
 "es": dict(title="Los juicios de Núremberg", desc="El primer tribunal internacional que juzgó a dirigentes de un Estado: cargos, sentencias y legado.",
  crumbs=[("historia","Historia y ética")],
  html=ficha("Juicio célebre","Los juicios de Núremberg","Por primera vez, un tribunal internacional juzgó a dirigentes de un Estado por lo que hicieron desde el poder. De ahí nace el derecho penal internacional actual.",
   [("Fechas","20 nov 1945 – 1 oct 1946"),("Tribunal","Tribunal Militar Internacional"),("Países","EE. UU., Reino Unido, URSS y Francia")],
   '<h2>Los cargos</h2>'+ul(["<b>Crímenes contra la paz:</b> planear y hacer una guerra de agresión.","<b>Crímenes de guerra:</b> violar las leyes de la guerra.","<b>Crímenes contra la humanidad:</b> exterminio, deportación y persecución de civiles.","<b>Conspiración</b> para cometer los anteriores."])
   +'<h2>El resultado</h2>'+table(["Sentencia","Acusados"],[["Pena de muerte","12"],["Prisión","7"],["Absueltos","3"]])
   +'<h2>Por qué importa hoy</h2><p>Dejó claro que «cumplir órdenes» no libra de responsabilidad. Sus principios inspiraron la Corte Penal Internacional (2002) y, en medicina, el Código de Núremberg de 1947 sobre experimentos con personas.</p><div class="claro"><span class="label">Debate</span><p>Se le critica que fuera una «justicia de vencedores»: los crímenes de los aliados no se juzgaron.</p></div>',
   box("Relacionado",ul(['<a href="{etica}">La pena de muerte en España</a>','<a href="{hito}">Las Siete Partidas</a>'])))),
 "ca": dict(title="Els judicis de Nuremberg", desc="El primer tribunal internacional que va jutjar dirigents d'un Estat: càrrecs, sentències i llegat.",
  crumbs=[("historia","Història i ètica")],
  html=ficha("Judici cèlebre","Els judicis de Nuremberg","Per primera vegada, un tribunal internacional va jutjar dirigents d'un Estat pel que van fer des del poder. D'aquí neix el dret penal internacional actual.",
   [("Dates","20 nov. 1945 – 1 oct. 1946"),("Tribunal","Tribunal Militar Internacional"),("Països","EUA, Regne Unit, URSS i França")],
   '<h2>Els càrrecs</h2>'+ul(["<b>Crims contra la pau:</b> planejar i fer una guerra d'agressió.","<b>Crims de guerra:</b> violar les lleis de la guerra.","<b>Crims contra la humanitat:</b> extermini, deportació i persecució de civils.","<b>Conspiració</b> per cometre els anteriors."])
   +'<h2>El resultat</h2>'+table(["Sentència","Acusats"],[["Pena de mort","12"],["Presó","7"],["Absolts","3"]])
   +'<h2>Per què importa avui</h2><p>Va deixar clar que «complir ordres» no allibera de responsabilitat. Els seus principis van inspirar la Cort Penal Internacional (2002) i, en medicina, el Codi de Nuremberg del 1947 sobre experiments amb persones.</p><div class="claro"><span class="label">Debat</span><p>Se li critica que fos una «justícia de vencedors»: els crims dels aliats no es van jutjar.</p></div>',
   box("Relacionat",ul(['<a href="{etica}">La pena de mort a Espanya</a>','<a href="{hito}">Les Siete Partidas</a>'])))),
}

# ---------------- ÉTICA ----------------
PAGES["etica"] = {
 "es": dict(title="La pena de muerte en España", desc="Cómo cambió la idea de castigo justo: de Beccaria y el garrote vil a la abolición total en 1995.",
  crumbs=[("historia","Historia y ética")],
  html=ficha("Ética y moral","La pena de muerte en España","Durante siglos fue el castigo más común para los delitos graves. Su historia muestra cómo cambió la idea de lo que es un castigo justo.",
   [("Últimas ejecuciones","27 sep 1975"),("Abolición en tiempo de paz","Constitución Española de 1978"),("Abolición total","Ley Orgánica 11/1995")],
   '<h2>La evolución</h2>'+tl([("1764","Beccaria publica <i>Dei delitti e delle pene</i> (De los delitos y las penas): el castigo debe ser útil y proporcionado, no cruel."),("1811","Las Cortes de Cádiz abolieron la tortura en los juicios."),("1932","El Código Penal de la República la suprime. Se recupera poco después."),("1974","Últimas ejecuciones con garrote vil."),("1975","Últimos fusilamientos, el 27 de septiembre."),("1978","La Constitución la abole, salvo lo que dispongan las leyes militares en tiempo de guerra (art. 15)."),("1995","Se elimina también del Código Penal Militar.")])
   +'<h2>Las dos posturas</h2><div class="pos"><div><h3>A favor, según sus defensores</h3><ul><li>Castigo proporcional a los crímenes más graves</li><li>Efecto disuasorio</li></ul></div><div><h3>En contra, según sus críticos</h3><ul><li>Un error judicial no tiene remedio</li><li>No hay pruebas claras de que disuada más que la cárcel</li><li>Va contra la dignidad humana</li></ul></div></div>'
   +'<div class="claro"><span class="label">Para pensar</span><p>¿Por qué algo que se consideró justo durante siglos hoy lo prohíben todos los países de la Unión Europea?</p></div>',
   box("Pensadores",ul(["Cesare Beccaria","Concepción Arenal","Immanuel Kant"]))+box("Relacionado",ul(['<a href="{juicio}">Los juicios de Núremberg</a>','<a href="{bio}">Clara Campoamor</a>'])))),
 "ca": dict(title="La pena de mort a Espanya", desc="Com va canviar la idea de càstig just: de Beccaria i el garrot vil a l'abolició total el 1995.",
  crumbs=[("historia","Història i ètica")],
  html=ficha("Ètica i moral","La pena de mort a Espanya","Durant segles va ser el càstig més habitual per als delictes greus. La seva història mostra com va canviar la idea del que és un càstig just.",
   [("Últimes execucions","27 set. 1975"),("Abolició en temps de pau","Constitución Española de 1978"),("Abolició total","Ley Orgánica 11/1995")],
   '<h2>L\'evolució</h2>'+tl([("1764","Beccaria publica <i>Dei delitti e delle pene</i> (Dels delictes i de les penes): el càstig ha de ser útil i proporcionat, no cruel."),("1811","Les Corts de Cadis van abolir la tortura en els judicis."),("1932","El Código Penal de 1932, de la República, la suprimeix. Es recupera poc després."),("1974","Últimes execucions amb garrot vil."),("1975","Últims afusellaments, el 27 de setembre."),("1978","La Constitución Española l'aboleix, llevat del que disposin les lleis militars en temps de guerra (art. 15)."),("1995","S'elimina també del Código Penal Militar.")])
   +'<h2>Les dues postures</h2><div class="pos"><div><h3>A favor, segons els seus defensors</h3><ul><li>Càstig proporcional als crims més greus</li><li>Efecte dissuasiu</li></ul></div><div><h3>En contra, segons els seus crítics</h3><ul><li>Un error judicial no té remei</li><li>No hi ha proves clares que dissuadeixi més que la presó</li><li>Va contra la dignitat humana</li></ul></div></div>'
   +'<div class="claro"><span class="label">Per pensar-hi</span><p>Per què una cosa que es va considerar justa durant segles avui la prohibeixen tots els països de la Unió Europea?</p></div>',
   box("Pensadors",ul(["Cesare Beccaria","Concepción Arenal","Immanuel Kant"]))+box("Relacionat",ul(['<a href="{juicio}">Els judicis de Nuremberg</a>','<a href="{bio}">Clara Campoamor</a>'])))),
}
