# -*- coding: utf-8 -*-
from content import *

def mats_grid(lang):
    out=[]
    for se,sc,ne,nc,de,dc,var in MATERIAS:
        n = ne if lang=="es" else nc; d = de if lang=="es" else dc
        v = ("Varía en Catalunya" if lang=="es" else "Varia a Catalunya") if var else ("Igual en toda España" if lang=="es" else "Igual a tot Espanya")
        pr = "" if se=="vivienda" else ('<span class="var" style="color:var(--muted)">'+("Próximamente" if lang=="es" else "Properament")+'</span>')
        tag = "a" if se=="vivienda" else "div"
        href = ' href="{vivienda}"' if se=="vivienda" else ""
        out.append(f'<{tag} class="mat"{href}><b>{n}</b><span>{d}</span><span class="var"{"" if var else " style=\"color:var(--muted)\""}>{v}</span>{pr}</{tag}>')
    return '<div class="mats">'+"".join(out)+'</div>'

# ---------------- HOME ----------------
def home(lang):
    es = lang=="es"
    return f'''<div class="hero"><div class="wrap">
<div><span class="label">{"Legislación española y catalana" if es else "Legislació espanyola i catalana"}</span>
<h1>{"Comprende la ley. <em>Resuelve tus dudas.</em> Prepara tus documentos." if es else "Comprèn la llei. <em>Resol els teus dubtes.</em> Prepara els teus documents."}</h1>
<p>{"Legislación española, catalana y europea explicada con claridad, con fuentes y fechas de actualización." if es else "Legislació espanyola, catalana i europea explicada amb claredat, amb fonts i dates d'actualització."}</p></div>
<aside class="panel" id="boe-panel" data-lang="{lang}"><div class="label">{"Último BOE" if es else "Últim BOE"} · <span id="boe-fecha">—</span></div>
<div class="big num" id="boe-total">—</div><div class="status">{"disposiciones publicadas" if es else "disposicions publicades"}</div>
<ul id="boe-secs"><li><span>{"Se carga desde el BOE al abrir la web publicada." if es else "Es carrega des del BOE en obrir la web publicada."}</span></li></ul>
<p style="margin:12px 0 0"><a href="{{novedades}}">{"Ver las disposiciones generales" if es else "Veure les disposicions generals"}</a></p></aside>
</div></div>
<div class="home-block"><div class="wrap"><h2>{"Materias" if es else "Matèries"}</h2>
<p>{"Toda la parte práctica se organiza por materias, con la ley estatal y lo que cambia en Catalunya." if es else "Tota la part pràctica s'organitza per matèries, amb la llei estatal i el que canvia a Catalunya."}</p>{mats_grid(lang)}</div></div>
<div class="home-block"><div class="wrap"><h2>{"Para empezar" if es else "Per començar"}</h2><p>{"Las primeras fichas de cada tipo." if es else "Les primeres fitxes de cada tipus."}</p>
<div class="cols">
<a class="card" href="{{cambio}}"><span class="label">{"Cambio importante · Vivienda" if es else "Canvi important · Habitatge"}</span><h3>{"Qué cambió con la ley de vivienda" if es else "Què va canviar amb la llei de l'habitatge"}</h3><p>{"Zonas tensionadas, honorarios de inmobiliaria y límites a la renta." if es else "Zones tensionades, honoraris d'immobiliària i límits a la renda."}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>
<a class="card" href="{{pregunta}}"><span class="label">{"Pregunta · Alquiler" if es else "Pregunta · Lloguer"}</span><h3>{"¿Cuánto preaviso para dejar un piso?" if es else "Amb quanta antelació cal avisar per deixar un pis?"}</h3><p>{"Desde los 6 meses, con 30 días de aviso." if es else "A partir dels 6 mesos, amb 30 dies d'avís."}</p><span class="go">{"Ver la respuesta" if es else "Veure la resposta"}</span></a>
<a class="card" href="{{contrato}}"><span class="label">{"Contrato · Gratis" if es else "Contracte · Gratuït"}</span><h3>{"Préstamo entre particulares" if es else "Préstec entre particulars"}</h3><p>{"Se rellena en tu navegador. Tus datos no salen de tu ordenador." if es else "S'omple al teu navegador. Les teves dades no surten del teu ordinador."}</p><span class="go">{"Crear el contrato" if es else "Crear el contracte"}</span></a>
</div></div></div>
<div class="home-block"><div class="wrap"><h2>{"Historia y ética del derecho" if es else "Història i ètica del dret"}</h2><p>{"De dónde vienen nuestras leyes y cómo ha cambiado lo que consideramos justo." if es else "D'on vénen les nostres lleis i com ha canviat el que considerem just."}</p>
<div class="cols">
<a class="card" href="{{hito}}"><span class="label">{"Historia" if es else "Història"}</span><h3>{"Las Siete Partidas" if es else "Les Siete Partidas"}</h3><p>{"El código de Alfonso X que llegó hasta América." if es else "El codi d'Alfons X que va arribar fins a Amèrica."}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>
<a class="card" href="{{bio}}"><span class="label">{"Biografía" if es else "Biografia"}</span><h3>Clara Campoamor</h3><p>{"La diputada que defendió el voto de la mujer en 1931." if es else "La diputada que va defensar el vot de la dona el 1931."}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>
<a class="card" href="{{etica}}"><span class="label">{"Ética y moral" if es else "Ètica i moral"}</span><h3>{"La pena de muerte en España" if es else "La pena de mort a Espanya"}</h3><p>{"Del garrote vil a su abolición total en 1995." if es else "Del garrot vil a la seva abolició total el 1995."}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>
</div></div></div>'''

PAGES["home"] = {
 "es": dict(title="Leypedia · Comprende la ley. Resuelve tus dudas. Prepara tus documentos.", desc="Legislación española, catalana y europea explicada con claridad, con fuentes y fechas de actualización.", crumbs=None, html=home("es"), plain_title=True),
 "ca": dict(title="Leypedia · Comprèn la llei. Resol els teus dubtes. Prepara els teus documents.", desc="Legislació espanyola, catalana i europea explicada amb claredat, amb fonts i dates d'actualització.", crumbs=None, html=home("ca"), plain_title=True),
}

def simple(label,h1,lead,body):
    return f'<div class="wrap"><div class="fhead"><span class="label">{label}</span><h1>{h1}</h1><p class="lead">{lead}</p></div><div style="padding-block:24px 46px" class="prose-wide">{body}</div></div>'

PAGES["materias"] = {
 "es": dict(title="Materias", desc="Las once materias de Leypedia, con la ley estatal y lo que cambia en Catalunya.", crumbs=[], html=simple("Parte práctica","Materias","Once grandes materias. Las marcadas «varía en Catalunya» tienen normas catalanas propias, y cada ficha te las muestra.",mats_grid("es"))),
 "ca": dict(title="Matèries", desc="Les onze matèries de Leypedia, amb la llei estatal i el que canvia a Catalunya.", crumbs=[], html=simple("Part pràctica","Matèries","Onze grans matèries. Les marcades «varia a Catalunya» tenen normes catalanes pròpies, i cada fitxa te les mostra.",mats_grid("ca"))),
}

def hub(lang):
    es = lang=="es"
    sub = ["Alquiler","Compraventa","Comunidad de vecinos","Hipotecas","Ayudas"] if es else ["Lloguer","Compravenda","Comunitat de veïns","Hipoteques","Ajuts"]
    return f'''<div class="subt">{"".join(f"<span>{x}</span>" for x in sub)}</div>
<div class="box cc" style="margin-bottom:16px"><h3>{"En Catalunya" if es else "A Catalunya"}</h3><p>{"La ley básica del alquiler es estatal, pero Catalunya tiene competencia en vivienda: decide las zonas tensionadas, gestiona el depósito de fianzas en el INCASÒL, convoca ayudas y fija el tipo del impuesto de la compraventa (ITP)." if es else "La llei bàsica del lloguer és estatal, però Catalunya té competència en habitatge: decideix les zones tensionades, gestiona el dipòsit de fiances a l'INCASÒL, convoca ajuts i fixa el tipus de l'impost de la compravenda (ITP)."}</p></div>
<div class="hub">
<div class="box"><h3>{"Cambios importantes" if es else "Canvis importants"}</h3>{ul(['<a href="{cambio}">'+("Qué cambió con la ley de vivienda" if es else "Què va canviar amb la llei de l'habitatge")+'</a>'])}</div>
<div class="box"><h3>{"Preguntas" if es else "Preguntes"}</h3>{ul(['<a href="{pregunta}">'+("¿Cuánto preaviso para dejar un piso?" if es else "Amb quanta antelació cal avisar per deixar un pis?")+'</a>'])}</div>
</div>'''

PAGES["vivienda"] = {
 "es": dict(title="Vivienda", desc="Alquiler, compraventa, comunidad de vecinos e hipotecas, con lo que cambia en Catalunya.", crumbs=[("materias","Materias")], html=simple("Materia","Vivienda","Alquiler, compraventa, comunidad de vecinos e hipotecas.",hub("es"))),
 "ca": dict(title="Habitatge", desc="Lloguer, compravenda, comunitat de veïns i hipoteques, amb el que canvia a Catalunya.", crumbs=[("materias","Matèries")], html=simple("Matèria","Habitatge","Lloguer, compravenda, comunitat de veïns i hipoteques.",hub("ca"))),
}

def nov(lang):
    es = lang=="es"
    f = ["Qué se ha publicado","Qué cambia","A quién afecta","Desde cuándo","Qué hay que hacer","Régimen transitorio","Fuente"] if es else ["Què s'ha publicat","Què canvia","A qui afecta","Des de quan","Què cal fer","Règim transitori","Font"]
    return f'''<div class="fbody" style="padding-block:0"><div class="prose" style="max-width:none">
<h2>{"Disposiciones generales del último BOE" if es else "Disposicions generals de l'últim BOE"}</h2>
<p class="status" id="boe-info">{"Se cargan directamente del Boletín Oficial del Estado cuando la web está publicada." if es else "Es carreguen directament del Boletín Oficial del Estado quan la web està publicada."}</p>
<ul class="dispo" id="boe-list" data-lang="{lang}"></ul>
<p class="status">{"Los títulos se muestran tal como los publica el BOE, sin traducir." if es else "Els títols es mostren tal com els publica el BOE, sense traduir."}</p></div>
<aside class="side"><div class="box"><h3>{"Cada novedad explicada responde a" if es else "Cada novetat explicada respon a"}</h3><ol style="margin:0;padding-left:20px;font-size:14px">{"".join(f"<li>{x}</li>" for x in f)}</ol></div>
<div class="box cc"><h3>DOGC</h3><p>{"Las novedades del Diari Oficial de la Generalitat de Catalunya se añaden a esta sección con el mismo formato." if es else "Les novetats del Diari Oficial de la Generalitat de Catalunya s'afegeixen a aquesta secció amb el mateix format."}</p></div></aside></div>'''

PAGES["novedades"] = {
 "es": dict(title="Novedades del BOE", desc="Las disposiciones generales del último Boletín Oficial del Estado, con enlace al texto oficial.", crumbs=[], html=simple("Novedades","Novedades del BOE y del DOGC","Lo que se ha publicado en los diarios oficiales, con enlace al texto original.",nov("es"))),
 "ca": dict(title="Novetats del BOE", desc="Les disposicions generals de l'últim Boletín Oficial del Estado, amb enllaç al text oficial.", crumbs=[], html=simple("Novetats","Novetats del BOE i del DOGC","El que s'ha publicat als diaris oficials, amb enllaç al text original.",nov("ca"))),
}

def hist(lang):
    es = lang=="es"
    items = [("hito","Historia del derecho" if es else "Història del dret","Las Siete Partidas" if es else "Les Siete Partidas"),("bio","Biografía" if es else "Biografia","Clara Campoamor"),("juicio","Juicio célebre" if es else "Judici cèlebre","Los juicios de Núremberg" if es else "Els judicis de Nuremberg"),("etica","Ética y moral" if es else "Ètica i moral","La pena de muerte en España" if es else "La pena de mort a Espanya")]
    return '<div class="cols two">'+"".join(f'<a class="card" href="{{{k}}}"><span class="label">{l}</span><h3>{t}</h3><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>' for k,l,t in items)+'</div>'

PAGES["historia"] = {
 "es": dict(title="Historia y ética del derecho", desc="Hitos, biografías, juicios célebres y la evolución de las ideas de justicia.", crumbs=[], html=simple("Historia y ética","Historia y ética del derecho","De dónde vienen nuestras leyes, quién las hizo y cómo ha cambiado lo que consideramos justo.",hist("es"))),
 "ca": dict(title="Història i ètica del dret", desc="Fites, biografies, judicis cèlebres i l'evolució de les idees de justícia.", crumbs=[], html=simple("Història i ètica","Història i ètica del dret","D'on vénen les nostres lleis, qui les va fer i com ha canviat el que considerem just.",hist("ca"))),
}

def cat(lang):
    es = lang=="es"
    rows = [
      (["Derecho civil","Codi civil de Catalunya","Herencias, familia, propiedad y contratos se rigen por el derecho catalán si tienes vecindad civil catalana."] if es else ["Dret civil","Codi civil de Catalunya","Herències, família, propietat i contractes es regeixen pel dret català si tens veïnatge civil català."]),
      (["Vivienda","DOGC · INCASÒL","Zonas tensionadas, depósito de fianzas y ayudas."] if es else ["Habitatge","DOGC · INCASÒL","Zones tensionades, dipòsit de fiances i ajuts."]),
      (["Impuestos cedidos","Agència Tributària de Catalunya","Sucesiones, donaciones, transmisiones patrimoniales y tramo autonómico del IRPF."] if es else ["Impostos cedits","Agència Tributària de Catalunya","Successions, donacions, transmissions patrimonials i tram autonòmic de l'IRPF."]),
      (["Consumo","Codi de consum de Catalunya","Derechos de los consumidores que se suman a la ley estatal."] if es else ["Consum","Codi de consum de Catalunya","Drets dels consumidors que se sumen a la llei estatal."]),
      (["Igual en toda España","Leyes estatales","Trabajo, Seguridad Social, extranjería y protección de datos."] if es else ["Igual a tot Espanya","Lleis estatals","Treball, Seguretat Social, estrangeria i protecció de dades."]),
    ]
    steps = (["Cada mañana se leen el BOE y el DOGC.","Se detecta qué fichas afecta cada disposición nueva.","Esas fichas se revisan y se actualizan con la versión consolidada.","Cada ficha muestra la fecha de vigencia y la fuente con la que se comprobó."] if es else ["Cada matí es llegeixen el BOE i el DOGC.","Es detecta a quines fitxes afecta cada disposició nova.","Aquestes fitxes es revisen i s'actualitzen amb la versió consolidada.","Cada fitxa mostra la data de vigència i la font amb què es va comprovar."])
    return (table(["Ámbito" if es else "Àmbit","Fuente catalana" if es else "Font catalana","Qué cambia" if es else "Què canvia"],rows)
      +f'<h2 style="font-family:var(--f-display);font-size:23px;margin:26px 0 12px">{"Cómo se mantiene actualizado" if es else "Com es manté actualitzat"}</h2><ol class="steps" style="grid-template-columns:repeat(4,1fr)">'+"".join(f"<li>{s}</li>" for s in steps)+'</ol>')

PAGES["catalunya"] = {
 "es": dict(title="Derecho en Catalunya", desc="Qué normas son catalanas y cuáles estatales, y cómo se mantiene actualizada la información.", crumbs=[], html=simple("Catalunya","Ley estatal y ley catalana","Catalunya tiene derecho civil propio y competencias en vivienda, consumo e impuestos cedidos. Cada ficha te dice qué parte es estatal y qué parte es catalana.",cat("es"))),
 "ca": dict(title="Dret a Catalunya", desc="Quines normes són catalanes i quines estatals, i com es manté actualitzada la informació.", crumbs=[], html=simple("Catalunya","Llei estatal i llei catalana","Catalunya té dret civil propi i competències en habitatge, consum i impostos cedits. Cada fitxa et diu quina part és estatal i quina és catalana.",cat("ca"))),
}

TIT = "[Nombre y apellidos o razón social] · NIF [pendiente] · [domicilio] · [email de contacto]"
PAGES["aviso"] = {
 "es": dict(title="Aviso legal", desc="Aviso legal de Leypedia.", crumbs=[], html=simple("Legal","Aviso legal","Información del titular y condiciones de uso.",
   f'<div class="prose"><h2>Titular</h2><p>{TIT}</p><h2>Qué es Leypedia</h2><p>Leypedia ofrece información jurídica general y divulgativa. No presta asesoramiento legal, no es un despacho de abogados y no sustituye la consulta con un profesional colegiado.</p><h2>Fuentes</h2><p>Los textos legales proceden del Boletín Oficial del Estado y del Diari Oficial de la Generalitat de Catalunya. La versión con valor jurídico es siempre la publicada en el diario oficial. Cada ficha indica la fecha en que se comprobó.</p><h2>Plantillas de contratos</h2><p>Las plantillas son orientativas. Quien las use es responsable de adaptarlas a su caso.</p><h2>Responsabilidad</h2><p>Leypedia revisa su contenido con regularidad, pero no garantiza que esté libre de errores ni actualizado en todo momento.</p></div>')),
 "ca": dict(title="Avís legal", desc="Avís legal de Leypedia.", crumbs=[], html=simple("Legal","Avís legal","Informació del titular i condicions d'ús.",
   f'<div class="prose"><h2>Titular</h2><p>{TIT}</p><h2>Què és Leypedia</h2><p>Leypedia ofereix informació jurídica general i divulgativa. No presta assessorament legal, no és un despatx d\'advocats i no substitueix la consulta amb un professional col·legiat.</p><h2>Fonts</h2><p>Els textos legals provenen del Boletín Oficial del Estado i del Diari Oficial de la Generalitat de Catalunya. La versió amb valor jurídic és sempre la publicada al diari oficial. Cada fitxa indica la data en què es va comprovar.</p><h2>Plantilles de contractes</h2><p>Les plantilles són orientatives. Qui les faci servir és responsable d\'adaptar-les al seu cas.</p><h2>Responsabilitat</h2><p>Leypedia revisa el seu contingut regularment, però no garanteix que estigui lliure d\'errors ni actualitzat en tot moment.</p></div>')),
}
PAGES["privacidad"] = {
 "es": dict(title="Privacidad", desc="Política de privacidad de Leypedia.", crumbs=[], html=simple("Legal","Política de privacidad","Leypedia no te pide datos personales ni los guarda.",
   f'<div class="prose"><h2>Responsable</h2><p>{TIT}</p><h2>Qué datos tratamos</h2><p>Ninguno que tú nos des: la web no tiene registro, formularios de contacto ni boletines por ahora.</p><h2>Contratos</h2><p>Los datos que escribes en el generador de contratos se procesan solo en tu navegador. No se envían a ningún servidor ni se guardan. Al cerrar o recargar la página desaparecen.</p><h2>Registros del servidor</h2><p>Como cualquier web, el servidor de alojamiento (Hostinger) registra datos técnicos de acceso, como la dirección IP, por seguridad. Hostinger actúa como encargado del tratamiento.</p><h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo al email del responsable, y reclamar ante la Agencia Española de Protección de Datos.</p></div>')),
 "ca": dict(title="Privacitat", desc="Política de privacitat de Leypedia.", crumbs=[], html=simple("Legal","Política de privacitat","Leypedia no et demana dades personals ni les desa.",
   f'<div class="prose"><h2>Responsable</h2><p>{TIT}</p><h2>Quines dades tractem</h2><p>Cap que ens donis tu: de moment la web no té registre, formularis de contacte ni butlletins.</p><h2>Contractes</h2><p>Les dades que escrius al generador de contractes es processen només al teu navegador. No s\'envien a cap servidor ni es desen. Quan tanques o recarregues la pàgina desapareixen.</p><h2>Registres del servidor</h2><p>Com qualsevol web, el servidor d\'allotjament (Hostinger) registra dades tècniques d\'accés, com l\'adreça IP, per seguretat. Hostinger actua com a encarregat del tractament.</p><h2>Els teus drets</h2><p>Pots exercir els drets d\'accés, rectificació, supressió, oposició, limitació i portabilitat escrivint al correu del responsable, i reclamar davant la Agencia Española de Protección de Datos o l\'Autoritat Catalana de Protecció de Dades.</p></div>')),
}
PAGES["cookies"] = {
 "es": dict(title="Cookies", desc="Leypedia no usa cookies.", crumbs=[], html=simple("Legal","Cookies","Leypedia no usa cookies.",'<div class="prose"><p>Esta web no instala cookies propias ni de terceros, no usa herramientas de estadísticas ni publicidad y no carga tipografías ni scripts de otros servidores. Por eso no te mostramos ningún aviso de cookies.</p><p>Si en el futuro se añade publicidad o estadísticas, esta página se actualizará y se te pedirá permiso antes.</p></div>')),
 "ca": dict(title="Galetes", desc="Leypedia no fa servir galetes.", crumbs=[], html=simple("Legal","Galetes","Leypedia no fa servir galetes.",'<div class="prose"><p>Aquesta web no instal·la galetes pròpies ni de tercers, no fa servir eines d\'estadístiques ni publicitat i no carrega tipografies ni scripts d\'altres servidors. Per això no et mostrem cap avís de galetes.</p><p>Si en el futur s\'hi afegeix publicitat o estadístiques, aquesta pàgina s\'actualitzarà i se\'t demanarà permís abans.</p></div>')),
}
