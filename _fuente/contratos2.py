# -*- coding: utf-8 -*-
# Contratos más usados por el ciudadano: el texto se genera en el navegador (assets/app.js)
from etimoral import *

ROUTES.update({
 "contratos": ("contratos/", "ca/contractes/"),
 "calquiler": ("contratos/alquiler-de-vivienda/", "ca/contractes/lloguer-d-habitatge/"),
 "chabitacion": ("contratos/alquiler-de-habitacion/", "ca/contractes/lloguer-d-habitacio/"),
 "ccoche": ("contratos/compraventa-de-coche/", "ca/contractes/compravenda-de-cotxe/"),
 "cgaraje": ("contratos/alquiler-de-garaje/", "ca/contractes/lloguer-de-garatge/"),
})

N_ES, N_CA = "Nombre y apellidos", "Nom i cognoms"
# (id, etiqueta es, etiqueta ca, tipo, valor, atributos)
F = {
 "prestamo": [("pr", "Quien presta", "Qui presta", "name"), ("pt", "Quien recibe el dinero", "Qui rep els diners", "name"),
   [("im", "Importe (€)", "Import (€)", "number", "6000", 'min="1" step="50"'), ("pl", "Plazo (meses)", "Termini (mesos)", "number", "24", 'min="1" max="360"')],
   [("in", "Interés anual (%)", "Interès anual (%)", "number", "0", 'min="0" max="20" step="0.25"'), ("ci", "Ciudad", "Ciutat", "text", "Barcelona")],
   ("pa", "Forma de pago", "Forma de pagament", "select", [("m", "Cuotas mensuales", "Quotes mensuals"), ("u", "Pago único al final", "Pagament únic al final")])],
 "alquiler": [("ar", "Propietario (arrendador)", "Propietari (arrendador)", "name"), ("at", "Inquilino (arrendatario)", "Llogater (arrendatari)", "name"),
   ("di", "Dirección de la vivienda", "Adreça de l'habitatge", "text", "", 'placeholder="Calle, número, piso, ciudad"'),
   [("re", "Renta mensual (€)", "Renda mensual (€)", "number", "900", 'min="1" step="10"'), ("dp", "Día de pago (1 a 7)", "Dia de pagament (1 a 7)", "number", "5", 'min="1" max="7"')],
   [("du", "Duración (años)", "Durada (anys)", "number", "5", 'min="1" max="20"'), ("ga", "Garantía extra (meses, máx. 2)", "Garantia extra (mesos, màx. 2)", "number", "0", 'min="0" max="2"')],
   ("ci", "Ciudad", "Ciutat", "text", "Barcelona"),
   ("pj", "El propietario es una empresa (duración mínima de 7 años)", "El propietari és una empresa (durada mínima de 7 anys)", "check")],
 "habitacion": [("ar", "Quien alquila la habitación", "Qui lloga l'habitació", "name"), ("at", "Quien la ocupa", "Qui l'ocupa", "name"),
   ("di", "Dirección del piso", "Adreça del pis", "text", "", 'placeholder="Calle, número, piso, ciudad"'),
   ("hb", "Habitación", "Habitació", "text", "", 'placeholder="Ej.: la del fondo, con ventana al patio"'),
   [("re", "Precio mensual (€)", "Preu mensual (€)", "number", "450", 'min="1" step="10"'), ("du", "Duración (meses)", "Durada (mesos)", "number", "11", 'min="1" max="60"')],
   [("fi", "Fianza (meses)", "Fiança (mesos)", "number", "1", 'min="0" max="2"'), ("pv", "Preaviso para irse (días)", "Preavís per marxar (dies)", "number", "30", 'min="7" max="60"')],
   ("gs", "Gastos de luz, agua, gas e internet", "Despeses de llum, aigua, gas i internet", "select", [("i", "Incluidos en el precio", "Inclosos al preu"), ("p", "Se reparten a partes iguales", "Es reparteixen a parts iguals")]),
   ("ci", "Ciudad", "Ciutat", "text", "Barcelona")],
 "coche": [("ve", "Vendedor", "Venedor", "name"), ("co", "Comprador", "Comprador", "name"),
   ("mm", "Marca y modelo", "Marca i model", "text", "", 'placeholder="Ej.: Seat Ibiza 1.0"'),
   [("mt", "Matrícula", "Matrícula", "text", "", 'placeholder="0000 XXX"'), ("km", "Kilómetros", "Quilòmetres", "number", "90000", 'min="0" step="1000"')],
   ("bt", "Número de bastidor", "Número de bastidor", "text", "", 'placeholder="17 caracteres"'),
   [("pr", "Precio (€)", "Preu (€)", "number", "6000", 'min="1" step="50"'), ("ci", "Ciudad", "Ciutat", "text", "Barcelona")]],
 "garaje": [("ar", "Propietario de la plaza", "Propietari de la plaça", "name"), ("at", "Quien la alquila", "Qui la lloga", "name"),
   ("di", "Dirección del garaje y número de plaza", "Adreça del garatge i número de plaça", "text", "", 'placeholder="Calle, número, plaza 12"'),
   [("re", "Renta mensual (€)", "Renda mensual (€)", "number", "80", 'min="1" step="5"'), ("fi", "Fianza (meses)", "Fiança (mesos)", "number", "1", 'min="0" max="3"')],
   [("du", "Duración (meses)", "Durada (mesos)", "number", "12", 'min="1" max="60"'), ("ci", "Ciudad", "Ciutat", "text", "Barcelona")]],
}

def field(f, es):
    i, le, lc, t = f[:4]
    lab = le if es else lc
    if t == "name":
        return f'<label for="{i}">{lab}<input id="{i}" data-name value="" placeholder="{N_ES if es else N_CA}"></label>'
    if t == "check":
        return f'<label class="check" for="{i}"><input id="{i}" type="checkbox"> {lab}</label>'
    if t == "area":
        ph = f[5] if len(f) > 5 else ""
        return f'<label for="{i}">{lab}<textarea id="{i}" rows="4" placeholder="{ph}"></textarea></label>'
    if t == "select":
        return f'<label for="{i}">{lab}<select id="{i}">' + "".join(f'<option value="{v}">{a if es else b}</option>' for v, a, b in f[4]) + '</select></label>'
    attrs = f[5] if len(f) > 5 else ""
    if not es:
        attrs = attrs.replace("Calle, número, piso, ciudad", "Carrer, número, pis, ciutat").replace("Calle, número, plaza 12", "Carrer, número, plaça 12").replace("Ej.: la del fondo, con ventana al patio", "Ex.: la del fons, amb finestra al pati").replace("Ej.:", "Ex.:").replace("17 caracteres", "17 caràcters")
    return f'<label for="{i}">{lab}<input id="{i}" type="{t}" value="{f[4]}" {attrs}></label>'

def form(tipo, es):
    rows = "".join(('<div class="row2">' + "".join(field(x, es) for x in f) + '</div>') if isinstance(f, list) else field(f, es) for f in F[tipo])
    return (f'<form class="form" id="f" autocomplete="off">{rows}'
            f'<label class="check" for="bl"><input id="bl" type="checkbox"> {"Dejar los nombres en blanco para rellenarlos a mano" if es else "Deixar els noms en blanc per omplir-los a mà"}</label>'
            f'<p class="safe">{"Tus datos no salen de este navegador: no se envían ni se guardan." if es else "Les teves dades no surten d&#39;aquest navegador: no s&#39;envien ni es desen."}</p></form>')

# tipo: (título es, título ca, lead es, lead ca, meta es, meta ca, catalunya es, catalunya ca, fuente es, fuente ca, consejos es, consejos ca)
CT = {
 "prestamo": ("Contrato de préstamo entre particulares", "Contracte de préstec entre particulars",
   "Para dejar dinero a un familiar o amigo y que quede claro cuánto y cuándo se devuelve.", "Per deixar diners a un familiar o amic i que quedi clar quant i quan es torna.",
   [("Trámite", "Modelo 600 en 30 días hábiles")], [("Tràmit", "Model 600 en 30 dies hàbils")],
   "El modelo 600 se presenta ante la Agència Tributària de Catalunya. El préstamo está exento del impuesto, pero hay que declararlo.",
   "El model 600 es presenta davant l'Agència Tributària de Catalunya. El préstec està exempt de l'impost, però cal declarar-lo.",
   "Ley del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados", "Ley del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados",
   ["Haz las transferencias por banco, con el concepto «préstamo», para que quede rastro.", "Si no hay interés, Hacienda puede pedir que se justifique."],
   ["Fes les transferències pel banc, amb el concepte «préstec», perquè en quedi rastre.", "Si no hi ha interès, Hisenda pot demanar que es justifiqui."]),
 "alquiler": ("Contrato de alquiler de vivienda", "Contracte de lloguer d'habitatge",
   "El contrato más habitual: alquilar un piso como vivienda habitual, con las condiciones mínimas que exige la ley.", "El contracte més habitual: llogar un pis com a habitatge habitual, amb les condicions mínimes que exigeix la llei.",
   [("Ley", "Ley de Arrendamientos Urbanos"), ("Fianza", "1 mes de renta")], [("Llei", "Ley de Arrendamientos Urbanos"), ("Fiança", "1 mes de renda")],
   "La fianza debe depositarse en el INCASÒL. Además, la vivienda necesita cédula de habitabilidad, y si está en una zona tensionada la renta no puede superar el índice de referencia de precios.",
   "La fiança s'ha de dipositar a l'INCASÒL. A més, l'habitatge necessita cèdula d'habitabilitat, i si és en una zona tensionada la renda no pot superar l'índex de referència de preus.",
   "Ley 29/1994, de Arrendamientos Urbanos, y Ley 12/2023, por el derecho a la vivienda", "Ley 29/1994, de Arrendamientos Urbanos, i Ley 12/2023, por el derecho a la vivienda",
   ["Haced un inventario con fotos del estado del piso el día de la entrega.", "El propietario debe darte el certificado de eficiencia energética.", "Los honorarios de la inmobiliaria los paga siempre el propietario."],
   ["Feu un inventari amb fotos de l'estat del pis el dia de l'entrega.", "El propietari t'ha de donar el certificat d'eficiència energètica.", "Els honoraris de la immobiliària els paga sempre el propietari."]),
 "habitacion": ("Contrato de alquiler de habitación", "Contracte de lloguer d'habitació",
   "Para alquilar una habitación en un piso compartido, con uso de la cocina, el baño y las zonas comunes.", "Per llogar una habitació en un pis compartit, amb ús de la cuina, el bany i les zones comunes.",
   [("Ley", "Código Civil y lo pactado")], [("Llei", "Código Civil i el que s'ha pactat")],
   "Las normas catalanas recientes extienden algunas reglas del alquiler de vivienda, como los límites de renta en zonas tensionadas, a ciertos alquileres de habitaciones. Compruébalo antes de firmar.",
   "Les normes catalanes recents estenen algunes regles del lloguer d'habitatge, com els límits de renda en zones tensionades, a certs lloguers d'habitacions. Comprova-ho abans de signar.",
   "Código Civil, artículos 1542 y siguientes", "Código Civil, articles 1542 i següents",
   ["Escribid las normas de la casa (visitas, limpieza, ruidos) para evitar conflictos.", "Si el piso entero se alquila por habitaciones, el propietario debe tener permiso del dueño o de la comunidad si así lo exigen los estatutos."],
   ["Escriviu les normes de la casa (visites, neteja, sorolls) per evitar conflictes.", "Si el pis sencer es lloga per habitacions, el propietari ha de tenir permís de l'amo o de la comunitat si ho exigeixen els estatuts."]),
 "coche": ("Contrato de compraventa de coche usado", "Contracte de compravenda de cotxe usat",
   "Para vender o comprar un coche de segunda mano entre particulares, con la entrega de papeles y el cambio de titular.", "Per vendre o comprar un cotxe de segona mà entre particulars, amb l'entrega de papers i el canvi de titular.",
   [("Impuesto", "Modelo 620, lo paga el comprador")], [("Impost", "Model 620, el paga el comprador")],
   "El modelo 620 se presenta ante la Agència Tributària de Catalunya. Además, la compraventa se rige por el libro sexto del Codi civil de Catalunya, con reglas propias sobre la conformidad del bien.",
   "El model 620 es presenta davant l'Agència Tributària de Catalunya. A més, la compravenda es regeix pel llibre sisè del Codi civil de Catalunya, amb regles pròpies sobre la conformitat del bé.",
   "Código Civil y Reglamento General de Vehículos", "Código Civil i Reglamento General de Vehículos",
   ["Pide un informe del vehículo a la DGT para ver cargas, embargos y titulares anteriores.", "Apunta la hora de la entrega: desde ese momento las multas son del comprador.", "El vendedor puede notificar la venta a la DGT para no responder de lo que pase después."],
   ["Demana un informe del vehicle a la DGT per veure càrregues, embargaments i titulars anteriors.", "Apunta l'hora de l'entrega: des d'aquell moment les multes són del comprador.", "El venedor pot notificar la venda a la DGT per no respondre del que passi després."]),
 "garaje": ("Contrato de alquiler de plaza de garaje", "Contracte de lloguer de plaça de garatge",
   "Para alquilar una plaza de aparcamiento suelta, sin vivienda.", "Per llogar una plaça d'aparcament solta, sense habitatge.",
   [("Ley", "Código Civil y lo pactado")], [("Llei", "Código Civil i el que s'ha pactat")],
   "Las reglas son las mismas que en el resto de España. Si la plaza se alquila junto con la vivienda, va en el contrato de alquiler de vivienda.",
   "Les regles són les mateixes que a la resta d'Espanya. Si la plaça es lloga juntament amb l'habitatge, va al contracte de lloguer d'habitatge.",
   "Código Civil, artículos 1542 y siguientes", "Código Civil, articles 1542 i següents",
   ["Indica qué mando o llave se entrega y cuánto cuesta reponerlo.", "Si la plaza tiene trastero, menciónalo en la dirección."],
   ["Indica quin comandament o clau s'entrega i quant costa reposar-lo.", "Si la plaça té traster, esmenta-ho a l'adreça."]),
}
CKEY = {"prestamo": "contrato", "alquiler": "calquiler", "habitacion": "chabitacion", "coche": "ccoche", "garaje": "cgaraje"}

def cpage(tipo, lang):
    es = lang == "es"
    t = CT[tipo]
    meta = [("Precio" if es else "Preu", "Gratis" if es else "Gratuït")] + (t[4] if es else t[5])
    m = "".join(f'<div><span class="status">{a}</span><b>{b}</b></div>' for a, b in meta)
    return f'''<div class="wrap"><div class="fhead"><span class="label">{"Contrato · Gratis" if es else "Contracte · Gratuït"}</span>
<h1>{t[0] if es else t[1]}</h1>
<p class="lead">{t[2] if es else t[3]} {"Rellena los datos y el contrato se escribe solo, en tu navegador." if es else "Omple les dades i el contracte s&#39;escriu sol, al teu navegador."}</p>
<div class="meta">{m}</div></div>
<div class="gen" style="padding-block:24px 46px">{form(tipo, es)}
<div style="min-width:0"><article class="doc" id="doc" aria-live="polite" data-tipo="{tipo}"></article>
<div class="actions"><button type="button" id="copiar">{"Copiar texto" if es else "Copiar el text"}</button><button type="button" class="ghost" id="imprimir">{"Imprimir o guardar en PDF" if es else "Imprimir o desar en PDF"}</button><button type="button" class="ghost" id="borrar">{"Borrar datos" if es else "Esborrar les dades"}</button><span class="status" id="cmsg"></span></div>
<div class="box" style="margin-top:16px"><h3>{"Consejos" if es else "Consells"}</h3>{ul(t[10] if es else t[11])}</div>
<div class="box cc" style="margin-top:16px"><h3>{"En Catalunya" if es else "A Catalunya"}</h3><p>{t[6] if es else t[7]}</p></div>
<p class="disc">{"Plantilla orientativa. Revísala con un profesional si el caso tiene particularidades." if es else "Plantilla orientativa. Revisa-la amb un professional si el cas té particularitats."}</p>
{vig(lang, t[8] if es else t[9])}</div></div></div>'''

for tipo, key in CKEY.items():
    PAGES[key] = {L: dict(title=CT[tipo][0 if L == "es" else 1],
        desc=("Modelo gratuito de " if L == "es" else "Model gratuït de ") + CT[tipo][0 if L == "es" else 1][0].lower() + CT[tipo][0 if L == "es" else 1][1:] + (" que se rellena en el navegador, sin enviar tus datos." if L == "es" else " que s'omple al navegador, sense enviar les teves dades."),
        crumbs=[("contratos", "Contratos" if L == "es" else "Contractes")], html=cpage(tipo, L)) for L in ("es", "ca")}

def cidx(lang):
    es = lang == "es"
    items = [(CKEY[t], CT[t][0] if es else CT[t][1], CT[t][2] if es else CT[t][3]) for t in ("alquiler", "habitacion", "coche", "garaje", "prestamo")]
    proximos = (["Arras para comprar una vivienda", "Carta de desistimiento de un alquiler", "Autorización para recoger documentos", "Reclamación a una empresa", "Contrato de trabajo doméstico", "Recibo de pago entre particulares"] if es else
                ["Arres per comprar un habitatge", "Carta de desistiment d'un lloguer", "Autorització per recollir documents", "Reclamació a una empresa", "Contracte de treball domèstic", "Rebut de pagament entre particulars"])
    return ('<div class="hub">' + "".join(f'<a class="card" href="{{{k_}}}"><span class="label">{"Contrato" if es else "Contracte"}</span><h3>{t}</h3><p>{d}</p><span class="go">{"Crear el contrato" if es else "Crear el contracte"}</span></a>' for k_, t, d in items) + '</div>'
      + f'<div class="box cc" style="margin-top:20px"><h3>{"Tus datos están seguros" if es else "Les teves dades estan segures"}</h3><p>{"Los contratos se escriben en tu propio navegador. Los nombres y datos que pongas no se envían a ningún servidor, no se guardan y se borran al cerrar la página. Si lo prefieres, puedes dejar los nombres en blanco y escribirlos a mano después de imprimir." if es else "Els contractes s&#39;escriuen al teu propi navegador. Els noms i les dades que hi posis no s&#39;envien a cap servidor, no es desen i s&#39;esborren en tancar la pàgina. Si ho prefereixes, pots deixar els noms en blanc i escriure&#39;ls a mà després d&#39;imprimir."}</p></div>'
      + f'<h2 class="sec">{"Próximos modelos" if es else "Propers models"}</h2><div class="subt">' + "".join(f"<span>{x}</span>" for x in proximos) + '</div>')

PAGES["contratos"] = {
 "es": dict(title="Contratos", desc="Modelos gratuitos de los contratos más usados: alquiler de vivienda y de habitación, compraventa de coche, garaje y préstamo.", crumbs=[],
   html=simple("Contratos", "Los contratos más usados", "Modelos claros y gratuitos para el día a día. Se rellenan en tu navegador y tus datos no salen de tu ordenador.", cidx("es"))),
 "ca": dict(title="Contractes", desc="Models gratuïts dels contractes més utilitzats: lloguer d'habitatge i d'habitació, compravenda de cotxe, garatge i préstec.", crumbs=[],
   html=simple("Contractes", "Els contractes més utilitzats", "Models clars i gratuïts per al dia a dia. S'omplen al teu navegador i les teves dades no surten del teu ordinador.", cidx("ca"))),
}
