# -*- coding: utf-8 -*-
# Ética y Moral: dos secciones separadas
from enciclo import *

ROUTES.update({
 "eticas": ("etica/", "ca/etica/"),
 "eutanasia": ("etica/eutanasia/", "ca/etica/eutanasia/"),
 "moral": ("moral/", "ca/moral/"),
 "divorcio": ("moral/divorcio/", "ca/moral/divorci/"),
 "matrimonio": ("moral/matrimonio-igualitario/", "ca/moral/matrimoni-igualitari/"),
})

def cards(items, lang):
    es = lang == "es"
    return '<div class="cols">' + "".join(
        f'<a class="card" href="{{{key}}}"><span class="label">{l}</span><h3>{t}</h3><p>{d}</p><span class="go">{"Leer la ficha" if es else "Llegir la fitxa"}</span></a>' for key, l, t, d in items) + '</div>'

def etica_idx(lang):
    es = lang == "es"
    intro = ('<div class="claro"><span class="label">Qué es la ética</span><p>La ética es la reflexión sobre lo que está bien y lo que está mal, y sobre por qué. Se pregunta si una ley es justa, no solo si es válida. En esta sección presentamos los grandes debates con los argumentos de cada postura, sin dar la respuesta hecha.</p></div>' if es else
             '<div class="claro"><span class="label">Què és l\'ètica</span><p>L\'ètica és la reflexió sobre el que està bé i el que està malament, i sobre per què. Es pregunta si una llei és justa, no només si és vàlida. En aquesta secció presentem els grans debats amb els arguments de cada postura, sense donar la resposta feta.</p></div>')
    items = [("etica", "Debate · Derecho penal" if es else "Debat · Dret penal", "La pena de muerte en España" if es else "La pena de mort a Espanya", "Del garrote vil a su abolición total en 1995." if es else "Del garrot vil a la seva abolició total el 1995."),
             ("eutanasia", "Debate · Salud" if es else "Debat · Salut", "La eutanasia" if es else "L'eutanàsia", "¿Tenemos derecho a decidir cómo morir? La ley de 2021 y los argumentos de cada lado." if es else "Tenim dret a decidir com morir? La llei del 2021 i els arguments de cada banda."),
             ("ue", "Debate · Tecnología" if es else "Debat · Tecnologia", "Ética de la inteligencia artificial" if es else "Ètica de la intel·ligència artificial", "Qué decisiones no deberían tomar las máquinas, según la ley europea." if es else "Quines decisions no haurien de prendre les màquines, segons la llei europea.")]
    debate = (f'<div class="box" style="margin-top:20px"><h3>{"Gran pregunta" if es else "Gran pregunta"}</h3><p style="margin:0 0 6px;font-family:var(--f-display);font-size:20px">{"¿Lo legal es siempre justo?" if es else "El que és legal és sempre just?"}</p>'
              f'<p style="margin:0">{"De Antígona a Rosa Parks, la historia está llena de personas que desobedecieron leyes que consideraban injustas. Hay quien defiende que la ley debe cumplirse siempre, porque sin ella no hay convivencia, y quien sostiene que una ley injusta no obliga en conciencia." if es else "D&#39;Antígona a Rosa Parks, la història és plena de persones que van desobeir lleis que consideraven injustes. Hi ha qui defensa que la llei s&#39;ha de complir sempre, perquè sense ella no hi ha convivència, i qui sosté que una llei injusta no obliga en consciència."}</p></div>')
    hist = (f'<h2 class="sec">{"Momentos de la historia de la ética" if es else "Moments de la història de l&#39;ètica"}</h2>' + tl(
        [("s. IV a. C.", "Aristóteles distingue la justicia de la ley: la ley puede equivocarse."), ("s. XVI", "La Escuela de Salamanca defiende que los indígenas de América tienen derechos naturales."), ("1764", "Cesare Beccaria publica <i>Dei delitti e delle pene</i> contra la tortura y la pena de muerte."), ("1785", "Kant: las personas son un fin en sí mismas, nunca solo un medio."), ("1948", "Declaración Universal de Derechos Humanos."), ("1979", "Informe Belmont: principios éticos para la investigación con personas.")] if es else
        [("s. IV aC", "Aristòtil distingeix la justícia de la llei: la llei es pot equivocar."), ("s. XVI", "L'Escola de Salamanca defensa que els indígenes d'Amèrica tenen drets naturals."), ("1764", "Cesare Beccaria publica <i>Dei delitti e delle pene</i> contra la tortura i la pena de mort."), ("1785", "Kant: les persones són un fi en si mateixes, mai només un mitjà."), ("1948", "Declaració Universal dels Drets Humans."), ("1979", "Informe Belmont: principis ètics per a la recerca amb persones.")]))
    return intro + cards(items, lang) + debate + hist

def moral_idx(lang):
    es = lang == "es"
    intro = ('<div class="claro"><span class="label">Qué es la moral</span><p>La moral es el conjunto de costumbres y valores que una sociedad considera buenos en cada momento. Cambia con el tiempo, y las leyes cambian con ella: lo que en una época era delito, en otra es un derecho. Aquí verás cómo ha evolucionado la moral en España a través de sus leyes.</p></div>' if es else
             '<div class="claro"><span class="label">Què és la moral</span><p>La moral és el conjunt de costums i valors que una societat considera bons en cada moment. Canvia amb el temps, i les lleis canvien amb ella: el que en una època era delicte, en una altra és un dret. Aquí veuràs com ha evolucionat la moral a Espanya a través de les seves lleis.</p></div>')
    items = [("divorcio", "Familia" if es else "Família", "El divorcio en España" if es else "El divorci a Espanya", "Permitido en 1932, prohibido en 1939 y recuperado en 1981." if es else "Permès el 1932, prohibit el 1939 i recuperat el 1981."),
             ("matrimonio", "Familia" if es else "Família", "Matrimonio entre personas del mismo sexo" if es else "Matrimoni entre persones del mateix sexe", "De la ley de peligrosidad social a la ley de 2005." if es else "De la llei de perillositat social a la llei del 2005."),
             ("bio", "Derechos" if es else "Drets", "El voto de la mujer" if es else "El vot de la dona", "Clara Campoamor y el debate de 1931." if es else "Clara Campoamor i el debat del 1931.")]
    antes = ([("La tortura en los juicios", "Se usaba para obtener confesiones hasta que las Cortes de Cádiz la abolieron en 1811."), ("La esclavitud", "España la abolió en Puerto Rico en 1873 y en Cuba en 1886, de las últimas en Europa."), ("El adulterio como delito", "Se castigaba con cárcel, sobre todo a las mujeres, hasta su despenalización en 1978."), ("La licencia marital", "Hasta 1975 la mujer casada necesitaba el permiso de su marido para trabajar, abrir una cuenta o firmar un contrato."), ("Los anticonceptivos", "Venderlos o anunciarlos fue delito hasta 1978."), ("La mayoría de edad a los 21", "Hasta 1978 no se era mayor de edad hasta los 21 años; desde entonces, a los 18.")] if es else
             [("La tortura en els judicis", "S'utilitzava per obtenir confessions fins que les Corts de Cadis la van abolir el 1811."), ("L'esclavitud", "Espanya la va abolir a Puerto Rico el 1873 i a Cuba el 1886, de les últimes d'Europa."), ("L'adulteri com a delicte", "Es castigava amb presó, sobretot les dones, fins que es va despenalitzar el 1978."), ("La llicència marital", "Fins al 1975 la dona casada necessitava el permís del marit per treballar, obrir un compte o signar un contracte."), ("Els anticonceptius", "Vendre'ls o anunciar-los va ser delicte fins al 1978."), ("La majoria d'edat als 21", "Fins al 1978 no s'era major d'edat fins als 21 anys; des d'aleshores, als 18.")])
    return (intro + cards(items, lang)
      + f'<h2 class="sec">{"Lo que antes era legal (o delito) en España" if es else "El que abans era legal (o delicte) a Espanya"}</h2><div class="cols">'
      + "".join(f'<div class="card soft"><h3>{t}</h3><p>{d}</p></div>' for t, d in antes) + '</div>')

def debate(pro_t, pro, con_t, con):
    return f'<div class="cols two"><div class="box"><h3>{pro_t}</h3>{ul(pro)}</div><div class="box"><h3>{con_t}</h3>{ul(con)}</div></div>'

PAGES["eticas"] = {
 "es": dict(title="Ética", desc="Los grandes debates éticos del derecho: pena de muerte, eutanasia, inteligencia artificial y la pregunta de si lo legal es siempre justo.", crumbs=[],
   html=simple("Ética", "Ética y derecho", "Qué es justo y por qué. Los grandes debates, con los argumentos de cada postura.", etica_idx("es"))),
 "ca": dict(title="Ètica", desc="Els grans debats ètics del dret: pena de mort, eutanàsia, intel·ligència artificial i la pregunta de si el que és legal és sempre just.", crumbs=[],
   html=simple("Ètica", "Ètica i dret", "Què és just i per què. Els grans debats, amb els arguments de cada postura.", etica_idx("ca"))),
}
PAGES["moral"] = {
 "es": dict(title="Moral", desc="Cómo ha cambiado la moral en España a través de sus leyes: divorcio, matrimonio, voto de la mujer y lo que antes era delito.", crumbs=[],
   html=simple("Moral", "La moral y su evolución", "Las costumbres y valores de cada época, y cómo han cambiado las leyes con ellos.", moral_idx("es"))),
 "ca": dict(title="Moral", desc="Com ha canviat la moral a Espanya a través de les seves lleis: divorci, matrimoni, vot de la dona i el que abans era delicte.", crumbs=[],
   html=simple("Moral", "La moral i la seva evolució", "Els costums i valors de cada època, i com han canviat les lleis amb ells.", moral_idx("ca"))),
}

PAGES["eutanasia"] = {
 "es": dict(title="La eutanasia", desc="La Ley Orgánica 3/2021 de regulación de la eutanasia: requisitos, procedimiento y el debate ético.", crumbs=[("eticas", "Ética")],
  html=ficha("Ética · Debate", "La eutanasia", "Desde 2021 España permite que una persona con una enfermedad grave e incurable pida ayuda médica para morir. Es uno de los debates éticos más profundos.",
   [("Norma", "Ley Orgánica 3/2021, de 24 de marzo"), ("En vigor", "25 de junio de 2021")],
   '<h2>Qué permite la ley</h2><p>Una persona mayor de edad, con capacidad para decidir y con una enfermedad grave e incurable, o un padecimiento grave, crónico e imposibilitante, puede pedir la prestación de ayuda para morir. Es una prestación de la sanidad pública.</p>'
   + '<h2>Cómo se pide</h2><ol><li>Dos solicitudes por escrito, separadas al menos 15 días.</li><li>El médico responsable informa de las alternativas, incluidos los cuidados paliativos.</li><li>Un segundo médico, el consultor, revisa el caso.</li><li>La Comisión de Garantía y Evaluación de la comunidad autónoma lo verifica antes de realizarla.</li></ol>'
   + '<h2>Antes de la ley</h2><p>Ayudar a morir a otra persona era delito según el artículo 143 del Código Penal, aunque con una pena reducida si la persona sufría una enfermedad grave y lo pedía expresamente.</p>'
   + '<h2>Los argumentos</h2>' + debate("A favor", ["Cada persona debe poder decidir sobre su propia vida y su final.", "Evita sufrimientos que la persona considera insoportables.", "La ley tiene controles para asegurar que la decisión es libre."],
                                        "En contra", ["La vida tiene un valor que no depende de la voluntad de cada uno.", "Puede presionar a personas vulnerables o que se sienten una carga.", "Lo prioritario debería ser extender los cuidados paliativos."])
   + '<p class="status">El Tribunal Constitucional avaló la ley en 2023 (STC 19/2023). Los profesionales sanitarios pueden ejercer la objeción de conciencia.</p>' + vig("es", "Ley Orgánica 3/2021, versión consolidada del BOE"),
   box("En Catalunya", '<p>La solicitud la revisa la Comissió de Garantia i Avaluació de Catalunya, que depende del Departament de Salut.</p>', "box cc")
   + box("Fuente", ul(["Ley Orgánica 3/2021, de 24 de marzo, de regulación de la eutanasia", "Boletín Oficial del Estado, 25 de marzo de 2021"]))
   + box("Relacionado", ul(['<a href="{etica}">La pena de muerte en España</a>', '<a href="{eticas}">Todos los debates éticos</a>'])))),
 "ca": dict(title="L'eutanàsia", desc="La Ley Orgánica 3/2021 de regulación de la eutanasia: requisits, procediment i el debat ètic.", crumbs=[("eticas", "Ètica")],
  html=ficha("Ètica · Debat", "L'eutanàsia", "Des del 2021 Espanya permet que una persona amb una malaltia greu i incurable demani ajuda mèdica per morir. És un dels debats ètics més profunds.",
   [("Norma", "Ley Orgánica 3/2021, de 24 de marzo"), ("En vigor", "25 de juny de 2021")],
   '<h2>Què permet la llei</h2><p>Una persona major d\'edat, amb capacitat per decidir i amb una malaltia greu i incurable, o un patiment greu, crònic i impossibilitant, pot demanar la prestació d\'ajuda per morir. És una prestació de la sanitat pública.</p>'
   + '<h2>Com es demana</h2><ol><li>Dues sol·licituds per escrit, separades almenys 15 dies.</li><li>El metge responsable informa de les alternatives, incloses les cures pal·liatives.</li><li>Un segon metge, el consultor, revisa el cas.</li><li>La Comissió de Garantia i Avaluació de la comunitat autònoma ho verifica abans de fer-la.</li></ol>'
   + '<h2>Abans de la llei</h2><p>Ajudar a morir una altra persona era delicte segons l\'article 143 del Código Penal, tot i que amb una pena reduïda si la persona patia una malaltia greu i ho demanava expressament.</p>'
   + '<h2>Els arguments</h2>' + debate("A favor", ["Cada persona ha de poder decidir sobre la seva pròpia vida i el seu final.", "Evita patiments que la persona considera insuportables.", "La llei té controls per assegurar que la decisió és lliure."],
                                         "En contra", ["La vida té un valor que no depèn de la voluntat de cadascú.", "Pot pressionar persones vulnerables o que se senten una càrrega.", "El prioritari hauria de ser estendre les cures pal·liatives."])
   + '<p class="status">El Tribunal Constitucional va avalar la llei el 2023 (STC 19/2023). Els professionals sanitaris poden exercir l\'objecció de consciència.</p>' + vig("ca", "Ley Orgánica 3/2021, versió consolidada del BOE"),
   box("A Catalunya", '<p>La sol·licitud la revisa la Comissió de Garantia i Avaluació de Catalunya, que depèn del Departament de Salut.</p>', "box cc")
   + box("Font", ul(["Ley Orgánica 3/2021, de 24 de marzo, de regulación de la eutanasia", "Boletín Oficial del Estado, 25 de març de 2021"]))
   + box("Relacionat", ul(['<a href="{etica}">La pena de mort a Espanya</a>', '<a href="{eticas}">Tots els debats ètics</a>'])))),
}

PAGES["divorcio"] = {
 "es": dict(title="El divorcio en España", desc="Historia del divorcio en España: la ley de 1932, su prohibición en 1939, la ley de 1981 y el divorcio exprés de 2005.", crumbs=[("moral", "Moral")],
  html=ficha("Moral · Familia", "El divorcio en España", "Pocas leyes muestran tan bien cómo cambia la moral de una sociedad. En menos de un siglo, el divorcio pasó de ser imposible a poder hacerse ante notario.",
   [("Primera ley", "1932"), ("Ley actual", "Ley 15/2005")],
   '<h2>Su historia</h2>' + tl([("1932", "La II República aprueba la primera ley de divorcio."), ("1939", "El franquismo la deroga. Los divorcios ya hechos se anulan."), ("1981", "La Ley 30/1981 vuelve a permitirlo, con separación previa y causas."), ("2005", "La Ley 15/2005, el «divorcio exprés»: no hace falta alegar causa, basta con que hayan pasado tres meses desde la boda."), ("2015", "Se puede divorciar ante notario si hay acuerdo y no hay hijos menores.")])
   + '<div class="claro"><span class="label">Curiosidad</span><p>La ley de 1981 se aprobó con una fuerte oposición: el ministro de Justicia que la impulsó, Francisco Fernández Ordóñez, fue muy criticado dentro de su propio partido.</p></div>'
   + '<h2>Qué ha cambiado en la moral</h2><p>El matrimonio ha pasado de entenderse como un vínculo para toda la vida a basarse en la voluntad de los cónyuges: basta con que uno de los dos no quiera seguir casado.</p>' + vig("es", "Código Civil, versión consolidada del BOE"),
   box("En Catalunya", '<p>Los efectos del divorcio (custodia de los hijos, uso de la vivienda, pensiones) los regula el libro segundo del Codi civil de Catalunya, que exige un plan de parentalidad cuando hay hijos.</p>', "box cc")
   + box("Fuente", ul(["Código Civil, artículos 85 a 89", "Ley 15/2005, de 8 de julio", "Codi civil de Catalunya, llibre segon"]))
   + box("Relacionado", ul(['<a href="{matrimonio}">Matrimonio entre personas del mismo sexo</a>', '<a href="{moral}">La moral y su evolución</a>'])))),
 "ca": dict(title="El divorci a Espanya", desc="Història del divorci a Espanya: la llei del 1932, la seva prohibició el 1939, la llei del 1981 i el divorci exprés del 2005.", crumbs=[("moral", "Moral")],
  html=ficha("Moral · Família", "El divorci a Espanya", "Poques lleis mostren tan bé com canvia la moral d'una societat. En menys d'un segle, el divorci va passar de ser impossible a poder-se fer davant notari.",
   [("Primera llei", "1932"), ("Llei actual", "Ley 15/2005")],
   '<h2>La seva història</h2>' + tl([("1932", "La II República aprova la primera llei de divorci."), ("1939", "El franquisme la deroga. Els divorcis ja fets s'anul·len."), ("1981", "La Ley 30/1981 torna a permetre'l, amb separació prèvia i causes."), ("2005", "La Ley 15/2005, el «divorci exprés»: no cal al·legar cap causa, n'hi ha prou que hagin passat tres mesos des del casament."), ("2015", "Es pot divorciar davant notari si hi ha acord i no hi ha fills menors.")])
   + '<div class="claro"><span class="label">Curiositat</span><p>La llei del 1981 es va aprovar amb una forta oposició: el ministre de Justícia que la va impulsar, Francisco Fernández Ordóñez, va ser molt criticat dins del seu propi partit.</p></div>'
   + '<h2>Què ha canviat en la moral</h2><p>El matrimoni ha passat d\'entendre\'s com un vincle per a tota la vida a basar-se en la voluntat dels cònjuges: n\'hi ha prou que un dels dos no vulgui continuar casat.</p>' + vig("ca", "Código Civil, versió consolidada del BOE"),
   box("A Catalunya", '<p>Els efectes del divorci (custòdia dels fills, ús de l\'habitatge, pensions) els regula el llibre segon del Codi civil de Catalunya, que exigeix un pla de parentalitat quan hi ha fills.</p>', "box cc")
   + box("Font", ul(["Código Civil, artículos 85 a 89", "Ley 15/2005, de 8 de julio", "Codi civil de Catalunya, llibre segon"]))
   + box("Relacionat", ul(['<a href="{matrimonio}">Matrimoni entre persones del mateix sexe</a>', '<a href="{moral}">La moral i la seva evolució</a>'])))),
}

PAGES["matrimonio"] = {
 "es": dict(title="Matrimonio entre personas del mismo sexo", desc="De la persecución legal de la homosexualidad a la Ley 13/2005, que hizo de España el tercer país del mundo en reconocer este matrimonio.", crumbs=[("moral", "Moral")],
  html=ficha("Moral · Familia", "Matrimonio entre personas del mismo sexo", "En 2005 España fue el tercer país del mundo en permitirlo, después de los Países Bajos y Bélgica. Treinta años antes, la homosexualidad todavía podía llevar a prisión.",
   [("Norma", "Ley 13/2005, de 1 de julio"), ("En vigor", "3 de julio de 2005")],
   '<h2>Su historia</h2>' + tl([("1954", "La Ley de Vagos y Maleantes se reforma para incluir a los homosexuales."), ("1970", "La Ley de Peligrosidad y Rehabilitación Social mantiene la persecución."), ("1979", "La homosexualidad deja de estar perseguida por esa ley."), ("2005", "La Ley 13/2005 permite el matrimonio entre personas del mismo sexo, con los mismos derechos, incluida la adopción."), ("2012", "El Tribunal Constitucional confirma la ley (STC 198/2012).")])
   + '<div class="claro"><span class="label">Curiosidad</span><p>Para cambiar la ley bastó con añadir una frase al artículo 44 del Código Civil: «El matrimonio tendrá los mismos requisitos y efectos cuando ambos contrayentes sean del mismo o de diferente sexo».</p></div>'
   + vig("es", "Código Civil, versión consolidada del BOE"),
   box("En Catalunya", '<p>El matrimonio es igual en toda España. Catalunya ya había regulado antes las parejas estables, también del mismo sexo, en su Ley 10/1998; hoy están en el libro segundo del Codi civil de Catalunya.</p>', "box cc")
   + box("Fuente", ul(["Ley 13/2005, de 1 de julio", "Código Civil, artículo 44"]))
   + box("Relacionado", ul(['<a href="{divorcio}">El divorcio en España</a>', '<a href="{moral}">La moral y su evolución</a>'])))),
 "ca": dict(title="Matrimoni entre persones del mateix sexe", desc="De la persecució legal de l'homosexualitat a la Ley 13/2005, que va fer d'Espanya el tercer país del món a reconèixer aquest matrimoni.", crumbs=[("moral", "Moral")],
  html=ficha("Moral · Família", "Matrimoni entre persones del mateix sexe", "El 2005 Espanya va ser el tercer país del món a permetre'l, després dels Països Baixos i Bèlgica. Trenta anys abans, l'homosexualitat encara podia portar a la presó.",
   [("Norma", "Ley 13/2005, de 1 de julio"), ("En vigor", "3 de juliol de 2005")],
   '<h2>La seva història</h2>' + tl([("1954", "La Ley de Vagos y Maleantes es reforma per incloure-hi els homosexuals."), ("1970", "La Ley de Peligrosidad y Rehabilitación Social manté la persecució."), ("1979", "L'homosexualitat deixa d'estar perseguida per aquesta llei."), ("2005", "La Ley 13/2005 permet el matrimoni entre persones del mateix sexe, amb els mateixos drets, inclosa l'adopció."), ("2012", "El Tribunal Constitucional confirma la llei (STC 198/2012).")])
   + '<div class="claro"><span class="label">Curiositat</span><p>Per canviar la llei n\'hi va haver prou d\'afegir una frase a l\'article 44 del Código Civil: «El matrimonio tendrá los mismos requisitos y efectos cuando ambos contrayentes sean del mismo o de diferente sexo».</p></div>'
   + vig("ca", "Código Civil, versió consolidada del BOE"),
   box("A Catalunya", '<p>El matrimoni és igual a tot Espanya. Catalunya ja havia regulat abans les parelles estables, també del mateix sexe, a la seva Llei 10/1998; avui són al llibre segon del Codi civil de Catalunya.</p>', "box cc")
   + box("Font", ul(["Ley 13/2005, de 1 de julio", "Código Civil, artículo 44"]))
   + box("Relacionat", ul(['<a href="{divorcio}">El divorci a Espanya</a>', '<a href="{moral}">La moral i la seva evolució</a>'])))),
}

# La pena de muerte pasa a colgar de Ética
for L in ("es", "ca"):
    PAGES["etica"][L]["crumbs"] = [("eticas", "Ética" if L == "es" else "Ètica")]
