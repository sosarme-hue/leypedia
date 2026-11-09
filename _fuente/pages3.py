# -*- coding: utf-8 -*-
# UE e internacional + ampliación de Historia y ética
from pages2 import *

ROUTES.update({
  "internacional": ("ue-e-internacional/", "ca/ue-i-internacional/"),
  "ue": ("ue-e-internacional/reglamento-de-inteligencia-artificial/", "ca/ue-i-internacional/reglament-d-intelligencia-artificial/"),
  "transfronterizo": ("ue-e-internacional/herencias-entre-varios-paises/", "ca/ue-i-internacional/herencies-entre-diversos-paisos/"),
})
for L, t in (("es", "UE e internacional"), ("ca", "UE i internacional")):
    nav = UI[L]["nav"]
    if not any(k == "internacional" for k, _ in nav):
        nav.insert(5, ("internacional", t))

def intl(lang):
    es = lang == "es"
    rows = ([["<b>Derecho de la Unión Europea</b>","Reglamentos, directivas y derechos de ciudadanos y empresas",'<span class="ok">Sí</span>'],
             ["<b>Derecho internacional privado</b>","Herencias, matrimonios o contratos vinculados a España y a otro país",'<span class="ok">Sí: sucesiones, familia, consumo, residencia y contratación</span>'],
             ["<b>Derecho internacional público</b>","Tratados, organizaciones internacionales y derechos humanos","Lo básico, ligado a la historia y la ética"],
             ["<b>Derecho interno extranjero</b>","Leyes propias de Francia, Alemania, Estados Unidos…",'<span class="no">No, por ahora</span>']] if es else
            [["<b>Dret de la Unió Europea</b>","Reglaments, directives i drets de ciutadans i empreses",'<span class="ok">Sí</span>'],
             ["<b>Dret internacional privat</b>","Herències, matrimonis o contractes vinculats a Espanya i a un altre país",'<span class="ok">Sí: successions, família, consum, residència i contractació</span>'],
             ["<b>Dret internacional públic</b>","Tractats, organitzacions internacionals i drets humans","El bàsic, lligat a la història i l'ètica"],
             ["<b>Dret intern estranger</b>","Lleis pròpies de França, Alemanya, els Estats Units…",'<span class="no">No, de moment</span>']])
    cards = [("transfronterizo", "Caso transfronterizo · Sucesiones" if es else "Cas transfronterer · Successions",
              "Heredar cuando hay dos países de por medio" if es else "Heretar quan hi ha dos països pel mig",
              "Qué ley se aplica si el fallecido vivía en otro país o tenía otra nacionalidad." if es else "Quina llei s'aplica si el difunt vivia en un altre país o tenia una altra nacionalitat."),
             ("ue", "Norma europea · Tecnología" if es else "Norma europea · Tecnologia",
              "Reglamento europeo de inteligencia artificial" if es else "Reglament europeu d'intel·ligència artificial",
              "Niveles de riesgo y calendario de aplicación." if es else "Nivells de risc i calendari d'aplicació.")]
    proximos = (["Divorcio de un matrimonio de distinta nacionalidad","Comprar online a una tienda de otro país de la UE","Trabajar o jubilarse en otro país de la UE","Residencia de familiares de ciudadanos de la UE","Contratos con una empresa extranjera","Reclamar una deuda en otro país de la UE","El RGPD y tus datos","Roaming y derechos de los viajeros"] if es else
                ["Divorci d'un matrimoni de nacionalitats diferents","Comprar en línia a una botiga d'un altre país de la UE","Treballar o jubilar-se en un altre país de la UE","Residència de familiars de ciutadans de la UE","Contractes amb una empresa estrangera","Reclamar un deute en un altre país de la UE","El RGPD i les teves dades","Itinerància i drets dels viatgers"])
    return (table(["Área" if es else "Àrea", "Ejemplos" if es else "Exemples", "En Leypedia"], rows)
      + '<div class="hub" style="margin-top:8px">' + "".join(f'<a class="card" href="{{{k}}}"><span class="label">{l}</span><h3>{t}</h3><p>{d}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>' for k, l, t, d in cards) + '</div>'
      + f'<h2 style="font-family:var(--f-display);font-size:23px;margin:28px 0 8px">{"Próximas fichas" if es else "Properes fitxes"}</h2><div class="subt">' + "".join(f"<span>{x}</span>" for x in proximos) + '</div>'
      + f'<p class="status">{"Fuente principal: EUR-Lex, el portal oficial del derecho de la UE, que permite descargar los actos vigentes por idioma. Las normas europeas no están publicadas en catalán, así que se citan con su título oficial en castellano." if es else "Font principal: EUR-Lex, el portal oficial del dret de la UE, que permet descarregar els actes vigents per idioma. Les normes europees no es publiquen en català, de manera que se citen amb el títol oficial en castellà."}</p>')

PAGES["internacional"] = {
 "es": dict(title="UE e internacional", desc="Derecho de la Unión Europea y casos que conectan España con otros países: herencias, familia, consumo, residencia y contratos.", crumbs=[],
   html=simple("UE e internacional", "La Unión Europea y los casos con otros países", "No se cubren las leyes internas de todos los países. Esta sección se centra en el derecho de la Unión Europea y en los casos que conectan España con otro país.", intl("es"))),
 "ca": dict(title="UE i internacional", desc="Dret de la Unió Europea i casos que connecten Espanya amb altres països: herències, família, consum, residència i contractes.", crumbs=[],
   html=simple("UE i internacional", "La Unió Europea i els casos amb altres països", "No es cobreixen les lleis internes de tots els països. Aquesta secció se centra en el dret de la Unió Europea i en els casos que connecten Espanya amb un altre país.", intl("ca"))),
}

PAGES["ue"] = {
 "es": dict(title="Reglamento europeo de inteligencia artificial", desc="El Reglamento (UE) 2024/1689: niveles de riesgo, obligaciones y calendario.", crumbs=[("internacional", "UE e internacional")],
  html=ficha("Norma europea · Tecnología", "Reglamento europeo de inteligencia artificial", "La primera gran ley sobre IA del mundo. Clasifica los sistemas de IA por su nivel de riesgo y pone más obligaciones cuanto mayor es el riesgo.",
   [("Norma", "Reglamento (UE) 2024/1689"), ("Tipo", "Reglamento: se aplica directamente"), ("En vigor", "1 de agosto de 2024")],
   '<div class="claro"><span class="label">Reglamento o directiva</span><p>Un reglamento se aplica igual en toda la UE desde el primer día. Una directiva fija un objetivo y cada país la traslada a su propia ley.</p></div>'
   + '<h2>Los cuatro niveles de riesgo</h2>' + table(["Nivel", "Ejemplos", "Qué exige"], [
       ["Inaceptable", "Puntuación social de ciudadanos, manipulación de personas vulnerables", "Prohibido"],
       ["Alto", "IA para seleccionar personal, conceder créditos o usada en la justicia", "Controles, registro y supervisión humana"],
       ["Limitado", "Chatbots, imágenes generadas por IA", "Avisar de que es IA"],
       ["Mínimo", "Filtros de spam, videojuegos", "Sin obligaciones nuevas"]])
   + '<h2>Calendario</h2>' + tl([("2 feb 2025", "Se aplican las prohibiciones."), ("2 ago 2025", "Obligaciones para los modelos de IA de uso general."), ("2 ago 2026", "Se aplica la mayor parte del reglamento, incluido el aviso de que hablas con una IA."), ("2 ago 2027", "Últimas obligaciones para algunos sistemas de alto riesgo.")])
   + '<p class="status">La UE ha propuesto aplazar parte de las obligaciones de alto riesgo. Esta ficha se revisará cuando se apruebe el cambio.</p>' + vig("es", "versión consolidada de EUR-Lex"),
   box("En España", '<p>Lo supervisa la Agencia Española de Supervisión de la Inteligencia Artificial (AESIA), con sede en A Coruña.</p>', "box cc")
   + box("Fuente", ul(["Reglamento (UE) 2024/1689, en EUR-Lex", "Diario Oficial de la Unión Europea, 12 de julio de 2024"])))),
 "ca": dict(title="Reglament europeu d'intel·ligència artificial", desc="El Reglamento (UE) 2024/1689: nivells de risc, obligacions i calendari.", crumbs=[("internacional", "UE i internacional")],
  html=ficha("Norma europea · Tecnologia", "Reglament europeu d'intel·ligència artificial", "La primera gran llei sobre IA del món. Classifica els sistemes d'IA segons el nivell de risc i hi posa més obligacions com més alt és el risc.",
   [("Norma", "Reglamento (UE) 2024/1689"), ("Tipus", "Reglament: s'aplica directament"), ("En vigor", "1 d'agost de 2024")],
   '<div class="claro"><span class="label">Reglament o directiva</span><p>Un reglament s\'aplica igual a tota la UE des del primer dia. Una directiva fixa un objectiu i cada país la trasllada a la seva pròpia llei.</p></div>'
   + '<h2>Els quatre nivells de risc</h2>' + table(["Nivell", "Exemples", "Què exigeix"], [
       ["Inacceptable", "Puntuació social de ciutadans, manipulació de persones vulnerables", "Prohibit"],
       ["Alt", "IA per seleccionar personal, concedir crèdits o utilitzada en la justícia", "Controls, registre i supervisió humana"],
       ["Limitat", "Xatbots, imatges generades per IA", "Avisar que és IA"],
       ["Mínim", "Filtres de correu brossa, videojocs", "Sense obligacions noves"]])
   + '<h2>Calendari</h2>' + tl([("2 febr. 2025", "S'apliquen les prohibicions."), ("2 ag. 2025", "Obligacions per als models d'IA d'ús general."), ("2 ag. 2026", "S'aplica la major part del reglament, inclòs l'avís que parles amb una IA."), ("2 ag. 2027", "Darreres obligacions per a alguns sistemes d'alt risc.")])
   + '<p class="status">La UE ha proposat ajornar part de les obligacions d\'alt risc. Aquesta fitxa es revisarà quan s\'aprovi el canvi.</p>' + vig("ca", "versió consolidada d'EUR-Lex"),
   box("A Espanya", '<p>El supervisa la Agencia Española de Supervisión de la Inteligencia Artificial (AESIA), amb seu a la Corunya.</p>', "box cc")
   + box("Font", ul(["Reglamento (UE) 2024/1689, a EUR-Lex", "Diario Oficial de la Unión Europea, 12 de juliol de 2024"])))),
}

PAGES["transfronterizo"] = {
 "es": dict(title="Heredar cuando hay dos países de por medio", desc="Qué ley se aplica a una herencia internacional según el Reglamento (UE) 650/2012, y qué pasa si el fallecido vivía en Catalunya.", crumbs=[("internacional", "UE e internacional")],
  html=ficha("Caso transfronterizo · Sucesiones", "Heredar cuando hay dos países de por medio", "Si alguien muere viviendo en un país de la UE distinto al de su nacionalidad, o con bienes en varios países, una norma europea decide qué ley se aplica a toda la herencia.",
   [("Norma", "Reglamento (UE) 650/2012"), ("Se aplica desde", "17 de agosto de 2015"), ("No participan", "Dinamarca e Irlanda")],
   '<div class="claro"><span class="label">La regla básica</span><p>Se aplica la ley del país donde el fallecido tenía su <b>residencia habitual</b> al morir, aunque fuera extranjero. Pero en el testamento puede elegir la ley de su <b>nacionalidad</b>.</p></div>'
   + '<h2>Ejemplos</h2>' + table(["Situación", "Ley que se aplica"], [
       ["Alemán que vive en Girona, sin testamento", "Ley española y, por vivir en Catalunya, el Codi civil de Catalunya"],
       ["Alemán que vive en Girona y en su testamento elige la ley alemana", "Ley alemana"],
       ["Española que vive en Francia, con un piso en Madrid", "Ley francesa para toda la herencia, incluido el piso"]])
   + '<h2>Qué hay que hacer</h2>' + ul(["Si vives en otro país, valora elegir en tu testamento la ley de tu nacionalidad.", "Los herederos pueden pedir el <b>certificado sucesorio europeo</b>, que demuestra su condición de herederos en cualquier país participante."])
   + '<h2>Fuente</h2>' + ul(["Reglamento (UE) 650/2012, en EUR-Lex.", "Cuando se aplica la ley española, el Código Civil decide entre el derecho común y los derechos civiles propios, como el catalán, según la vecindad civil."])
   + vig("es", "versión consolidada de EUR-Lex"),
   box("En Catalunya", '<p>Si se aplica la ley española y el fallecido tenía vecindad civil catalana, rige el Codi civil de Catalunya. Allí la legítima de los hijos es una cuarta parte de la herencia, menos que en el Código Civil.</p>', "box cc")
   + box("Relacionado", ul(['<a href="{internacional}">UE e internacional</a>'])))),
 "ca": dict(title="Heretar quan hi ha dos països pel mig", desc="Quina llei s'aplica a una herència internacional segons el Reglamento (UE) 650/2012, i què passa si el difunt vivia a Catalunya.", crumbs=[("internacional", "UE i internacional")],
  html=ficha("Cas transfronterer · Successions", "Heretar quan hi ha dos països pel mig", "Si algú mor vivint en un país de la UE diferent del de la seva nacionalitat, o amb béns en diversos països, una norma europea decideix quina llei s'aplica a tota l'herència.",
   [("Norma", "Reglamento (UE) 650/2012"), ("S'aplica des del", "17 d'agost de 2015"), ("No hi participen", "Dinamarca i Irlanda")],
   '<div class="claro"><span class="label">La regla bàsica</span><p>S\'aplica la llei del país on el difunt tenia la <b>residència habitual</b> quan va morir, encara que fos estranger. Però en el testament pot triar la llei de la seva <b>nacionalitat</b>.</p></div>'
   + '<h2>Exemples</h2>' + table(["Situació", "Llei que s'aplica"], [
       ["Alemany que viu a Girona, sense testament", "Llei espanyola i, com que viu a Catalunya, el Codi civil de Catalunya"],
       ["Alemany que viu a Girona i en el testament tria la llei alemanya", "Llei alemanya"],
       ["Espanyola que viu a França, amb un pis a Madrid", "Llei francesa per a tota l'herència, inclòs el pis"]])
   + '<h2>Què cal fer</h2>' + ul(["Si vius en un altre país, valora triar en el testament la llei de la teva nacionalitat.", "Els hereus poden demanar el <b>certificat successori europeu</b>, que acredita la condició d'hereu a qualsevol país participant."])
   + '<h2>Font</h2>' + ul(["Reglamento (UE) 650/2012, a EUR-Lex.", "Quan s'aplica la llei espanyola, el Código Civil decideix entre el dret comú i els drets civils propis, com el català, segons el veïnatge civil."])
   + vig("ca", "versió consolidada d'EUR-Lex"),
   box("A Catalunya", '<p>Si s\'aplica la llei espanyola i el difunt tenia veïnatge civil català, regeix el Codi civil de Catalunya. Allà la llegítima dels fills és una quarta part de l\'herència, menys que al Código Civil.</p>', "box cc")
   + box("Relacionat", ul(['<a href="{internacional}">UE i internacional</a>'])))),
}

# ---------- Historia y ética ampliada ----------
TL_ES = [("c. 1750 a. C.","Código de Hammurabi: una de las primeras leyes escritas."),("c. 450 a. C.","Ley de las XII Tablas: Roma pone sus leyes por escrito."),("529–534","Justiniano recopila el derecho romano en el Corpus Iuris Civilis."),("c. 1256–1265","Alfonso X ordena las Siete Partidas."),("1215","Carta Magna: el rey inglés acepta límites a su poder."),("1512","Leyes de Burgos: primeras normas sobre el trato a los indígenas de América."),("1789","<i>Déclaration des droits de l'homme et du citoyen</i> (Declaración de los Derechos del Hombre y del Ciudadano)."),("1804","<i>Code civil</i> de Napoleón, modelo de los códigos civiles europeos."),("1812","Constitución de Cádiz, la primera española."),("1889","Código Civil español, vigente hoy con muchas reformas."),("1931","La Constitución de la II República reconoce el voto de la mujer."),("1948","Declaración Universal de Derechos Humanos."),("1978","Constitución Española."),("1986","España entra en la Comunidad Económica Europea."),("2024","Reglamento europeo de inteligencia artificial.")]
TL_CA = [("c. 1750 aC","Codi d'Hammurabi: una de les primeres lleis escrites."),("c. 450 aC","Llei de les XII Taules: Roma posa les seves lleis per escrit."),("529–534","Justinià recopila el dret romà al Corpus Iuris Civilis."),("c. 1256–1265","Alfons X ordena les Siete Partidas."),("1215","Carta Magna: el rei anglès accepta límits al seu poder."),("1512","Leyes de Burgos: primeres normes sobre el tracte als indígenes d'Amèrica."),("1789","<i>Déclaration des droits de l'homme et du citoyen</i> (Declaració dels Drets de l'Home i del Ciutadà)."),("1804","<i>Code civil</i> de Napoleó, model dels codis civils europeus."),("1812","Constitución de Cádiz, la primera espanyola."),("1889","Código Civil espanyol, vigent avui amb moltes reformes."),("1931","La Constitució de la II República reconeix el vot de la dona."),("1948","Declaració Universal dels Drets Humans."),("1978","Constitución Española."),("1986","Espanya entra a la Comunitat Econòmica Europea."),("2024","Reglament europeu d'intel·ligència artificial.")]
TL_ES.sort(key=lambda x: int(''.join(c for c in x[0].split('–')[0] if c.isdigit())) * (-1 if 'a. C.' in x[0] else 1))
TL_CA.sort(key=lambda x: int(''.join(c for c in x[0].split('–')[0] if c.isdigit())) * (-1 if 'aC' in x[0] else 1))

def hist2(lang):
    es = lang == "es"
    antes = ([("La tortura en los juicios","Se usaba para obtener confesiones hasta que las Cortes de Cádiz la abolieron en 1811."),("La esclavitud","España la abolió en Puerto Rico en 1873 y en Cuba en 1886, de las últimas en Europa."),("El adulterio como delito","Se castigaba con cárcel, sobre todo a las mujeres, hasta su despenalización en 1978.")] if es else
             [("La tortura en els judicis","S'utilitzava per obtenir confessions fins que les Corts de Cadis la van abolir el 1811."),("L'esclavitud","Espanya la va abolir a Puerto Rico el 1873 i a Cuba el 1886, de les últimes d'Europa."),("L'adulteri com a delicte","Es castigava amb presó, sobretot les dones, fins que es va despenalitzar el 1978.")])
    return (hist(lang)
      + f'<h2 style="font-family:var(--f-display);font-size:23px;margin:30px 0 12px">{"Línea del tiempo" if es else "Línia del temps"}</h2>' + tl(TL_ES if es else TL_CA)
      + f'<h2 style="font-family:var(--f-display);font-size:23px;margin:30px 0 12px">{"Lo que antes era legal (o delito) en España" if es else "El que abans era legal (o delicte) a Espanya"}</h2><div class="cols">'
      + "".join(f'<div class="card" style="background:var(--accent-soft);border-color:transparent"><h3>{t}</h3><p>{d}</p></div>' for t, d in antes) + '</div>'
      + f'<div class="box" style="margin-top:20px"><h3>{"Debate" if es else "Debat"}</h3><p style="margin:0 0 6px;font-family:var(--f-display);font-size:20px">{"¿Lo legal es siempre justo?" if es else "El que és legal és sempre just?"}</p><p style="margin:0">{"De Antígona a Rosa Parks, la historia está llena de personas que desobedecieron leyes que consideraban injustas. Las fichas de debate presentan los argumentos de cada postura, sin dar la respuesta hecha." if es else "D\'Antígona a Rosa Parks, la història és plena de persones que van desobeir lleis que consideraven injustes. Les fitxes de debat presenten els arguments de cada postura, sense donar la resposta feta."}</p></div>')

PAGES["historia"]["es"]["html"] = simple("Historia y ética", "Historia y ética del derecho", "De dónde vienen nuestras leyes, quién las hizo y cómo ha cambiado lo que consideramos justo.", hist2("es"))
PAGES["historia"]["ca"]["html"] = simple("Història i ètica", "Història i ètica del dret", "D'on vénen les nostres lleis, qui les va fer i com ha canviat el que considerem just.", hist2("ca"))

# Portada: bloque UE
for L in ("es", "ca"):
    es = L == "es"
    blk = (f'<div class="home-block"><div class="wrap"><h2>{"UE e internacional" if es else "UE i internacional"}</h2><p>{"Las normas europeas que te afectan y los casos con otros países." if es else "Les normes europees que t\'afecten i els casos amb altres països."}</p><div class="cols two">'
           f'<a class="card" href="{{transfronterizo}}"><span class="label">{"Sucesiones" if es else "Successions"}</span><h3>{"Heredar cuando hay dos países de por medio" if es else "Heretar quan hi ha dos països pel mig"}</h3><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>'
           f'<a class="card" href="{{ue}}"><span class="label">{"Tecnología" if es else "Tecnologia"}</span><h3>{"Reglamento europeo de inteligencia artificial" if es else "Reglament europeu d\'intel·ligència artificial"}</h3><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a></div></div></div>')
    h = PAGES["home"][L]["html"]
    i = h.rfind('<div class="home-block">')
    PAGES["home"][L]["html"] = h[:i] + blk + h[i:]
