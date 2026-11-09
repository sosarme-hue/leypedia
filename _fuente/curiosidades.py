# -*- coding: utf-8 -*-
# Curiosidades y anécdotas del derecho (España, Catalunya y Europa)
from contratos3 import *

ROUTES["curiosidades"] = ("historia/curiosidades/", "ca/historia/curiositats/")
PARENT["curiosidades"] = "historia"

CCAT = [
 ("palabras", "Palabras con historia", "Paraules amb història"),
 ("antiguas", "Leyes muy antiguas que siguen vigentes", "Lleis molt antigues que continuen vigents"),
 ("constituciones", "Constituciones y boletines", "Constitucions i butlletins"),
 ("catalunya", "Catalunya", "Catalunya"),
 ("mujeres", "Mujeres y derecho", "Dones i dret"),
 ("juicios", "Juicios y tribunales", "Judicis i tribunals"),
 ("europa", "Europa", "Europa"),
]

# (categoría, título es, título ca, texto es, texto ca, enlace opcional)
CU = [
 # --- Palabras
 ("palabras", "Salario viene de la sal", "Salari ve de la sal",
  "La palabra viene del latín <i>salarium</i>, relacionado con la sal. Lo de que a los soldados romanos se les pagaba en sal es una explicación muy repetida, pero los historiadores no han encontrado pruebas claras.",
  "La paraula ve del llatí <i>salarium</i>, relacionat amb la sal. Allò que als soldats romans se'ls pagava amb sal és una explicació molt repetida, però els historiadors no n'han trobat proves clares.", None),
 ("palabras", "El alcalde era un juez", "L'alcalde era un jutge",
  "«Alcalde» viene del árabe <i>al-qadi</i>, el juez. Durante siglos los alcaldes de las villas castellanas sobre todo juzgaban pleitos. «Alguacil» también viene del árabe: <i>al-wazir</i>, el ministro.",
  "«Alcalde» ve de l'àrab <i>al-qadi</i>, el jutge. Durant segles els alcaldes de les viles castellanes sobretot jutjaven plets. «Algutzir» també ve de l'àrab: <i>al-wazir</i>, el ministre.", "efueros"),
 ("palabras", "Testigo y testamento, misma familia", "Testimoni i testament, mateixa família",
  "Las dos palabras vienen del latín <i>testis</i>, testigo. En Roma un testamento era, ante todo, una declaración hecha delante de testigos.",
  "Les dues paraules vénen del llatí <i>testis</i>, testimoni. A Roma un testament era, sobretot, una declaració feta davant de testimonis.", "eromana"),
 ("palabras", "El abogado es el que llamas en tu ayuda", "L'advocat és qui crides en ajuda teva",
  "«Abogado» viene del latín <i>advocatus</i>, «el llamado» para ayudar a alguien en un juicio. Y «notario» viene de <i>notarius</i>, el que tomaba notas rápidas con abreviaturas.",
  "«Advocat» ve del llatí <i>advocatus</i>, «el cridat» per ajudar algú en un judici. I «notari» ve de <i>notarius</i>, el que prenia notes ràpides amb abreviatures.", None),
 ("palabras", "Boicot era un señor", "Boicot era un senyor",
  "Charles Boycott administraba tierras en Irlanda. En 1880 los campesinos, hartos de sus desahucios, dejaron de trabajar para él y de venderle nada. Su apellido se convirtió en verbo en medio mundo.",
  "Charles Boycott administrava terres a Irlanda. El 1880 els pagesos, farts dels seus desnonaments, van deixar de treballar per a ell i de vendre-li res. El seu cognom es va convertir en verb a mig món.", None),
 ("palabras", "Veredicto: dicho con verdad", "Veredicte: dit amb veritat",
  "«Veredicto» viene del latín <i>vere dictum</i>, «dicho con verdad». «Hipoteca» viene del griego <i>hypothēkē</i>, lo que se pone debajo como garantía. Y «quórum» es latín: «de los cuales».",
  "«Veredicte» ve del llatí <i>vere dictum</i>, «dit amb veritat». «Hipoteca» ve del grec <i>hypothēkē</i>, el que es posa a sota com a garantia. I «quòrum» és llatí: «dels quals».", None),
 # --- Leyes antiguas
 ("antiguas", "El Código Civil tiene más de 135 años", "El Código Civil té més de 135 anys",
  "El Código Civil español es de 1889. Con muchas reformas, sigue regulando los contratos, las herencias o la familia en buena parte de España. En Catalunya rige el Codi civil de Catalunya, y el estatal solo se aplica en lo que este no regula.",
  "El Código Civil espanyol és del 1889. Amb moltes reformes, continua regulant els contractes, les herències o la família en bona part d'Espanya. A Catalunya regeix el Codi civil de Catalunya, i l'estatal només s'aplica en allò que aquest no regula.", "ecodificacion"),
 ("antiguas", "Juicios con una ley de 1882", "Judicis amb una llei del 1882",
  "Los juicios penales se siguen tramitando con la Ley de Enjuiciamiento Criminal de 1882. Su exposición de motivos, del ministro Alonso Martínez, todavía se cita por su defensa del acusado frente al Estado.",
  "Els judicis penals es continuen tramitant amb la Ley de Enjuiciamiento Criminal del 1882. La seva exposició de motius, del ministre Alonso Martínez, encara se cita per la seva defensa de l'acusat davant l'Estat.", "palonsomartinez"),
 ("antiguas", "Notarios con una ley de 1862", "Notaris amb una llei del 1862",
  "La Ley del Notariado de 1862 sigue vigente. Y el Código de Comercio de 1885 también, aunque gran parte de su contenido ha pasado a leyes más modernas.",
  "La Ley del Notariado del 1862 continua vigent. I el Código de Comercio del 1885 també, tot i que bona part del seu contingut ha passat a lleis més modernes.", None),
 ("antiguas", "El tribunal que se reúne cada jueves desde hace siglos", "El tribunal que es reuneix cada dijous des de fa segles",
  "El Tribunal de las Aguas de Valencia se reúne cada jueves a mediodía en la puerta de los Apóstoles de la catedral para resolver los conflictos de riego de la huerta. Los juicios son orales, en valenciano y sin abogados. La ley lo reconoce como tribunal y la UNESCO lo declaró patrimonio inmaterial en 2009.",
  "El Tribunal de les Aigües de València es reuneix cada dijous a migdia a la porta dels Apòstols de la catedral per resoldre els conflictes de reg de l'horta. Els judicis són orals, en valencià i sense advocats. La llei el reconeix com a tribunal i la UNESCO el va declarar patrimoni immaterial el 2009.", None),
 ("antiguas", "Las Partidas, citadas en Estados Unidos", "Les Partidas, citades als Estats Units",
  "Las Siete Partidas de Alfonso X, del siglo XIII, todavía aparecen en sentencias de tribunales de Estados Unidos, en pleitos sobre tierras y aguas de territorios que fueron españoles, como Texas, California o Luisiana.",
  "Les Siete Partidas d'Alfons X, del segle XIII, encara apareixen en sentències de tribunals dels Estats Units, en plets sobre terres i aigües de territoris que van ser espanyols, com Texas, Califòrnia o Louisiana.", "hito"),
 # --- Constituciones y boletines
 ("constituciones", "La Constitución más larga y la más corta", "La Constitució més llarga i la més curta",
  "La de Cádiz de 1812 tenía 384 artículos, la más larga de la historia de España. La de 1978 tiene 169. Y la de 1856 nunca llegó a entrar en vigor: se la conoce como la «non nata», la no nacida.",
  "La de Cadis del 1812 tenia 384 articles, la més llarga de la història d'Espanya. La del 1978 en té 169. I la del 1856 no va arribar mai a entrar en vigor: se la coneix com la «non nata», la no nascuda.", "ecadiz"),
 ("constituciones", "El BOE tiene más de 360 años", "El BOE té més de 360 anys",
  "El Boletín Oficial del Estado desciende de la <i>Gazeta</i>, que empezó a publicarse en 1661. Se llama BOE desde 1936. Desde 2009 la única edición oficial es la electrónica: ya no se imprime en papel.",
  "El Boletín Oficial del Estado descendeix de la <i>Gazeta</i>, que es va començar a publicar el 1661. Es diu BOE des del 1936. Des del 2009 l'única edició oficial és l'electrònica: ja no s'imprimeix en paper.", "novedades"),
 ("constituciones", "Las leyes esperan 20 días", "Les lleis esperen 20 dies",
  "Si una ley no dice otra cosa, entra en vigor a los 20 días de publicarse completa en el boletín oficial. Es la <i>vacatio legis</i>, el tiempo para que todos podamos conocerla.",
  "Si una llei no diu una altra cosa, entra en vigor als 20 dies de publicar-se completa al butlletí oficial. És la <i>vacatio legis</i>, el temps perquè tothom la pugui conèixer.", None),
 ("constituciones", "No conocer la ley no te libra de cumplirla", "No conèixer la llei no t'eximeix de complir-la",
  "Lo dice el artículo 6 del Código Civil: «La ignorancia de las leyes no excusa de su cumplimiento». Es una de las razones por las que existe Leypedia.",
  "Ho diu l'article 6 del Código Civil: «La ignorancia de las leyes no excusa de su cumplimiento». És una de les raons per les quals existeix Leypedia.", None),
 ("constituciones", "La mayoría de edad era a los 21", "La majoria d'edat era als 21",
  "Hasta noviembre de 1978 la mayoría de edad en España era a los 21 años. Se rebajó a los 18 justo antes del referéndum de la Constitución, que la fija en esa edad en su artículo 12.",
  "Fins al novembre del 1978 la majoria d'edat a Espanya era als 21 anys. Es va rebaixar als 18 just abans del referèndum de la Constitució, que la fixa en aquesta edat a l'article 12.", "edemocracia"),
 ("constituciones", "La pena de muerte, abolida en dos pasos", "La pena de mort, abolida en dos passos",
  "La Constitución de 1978 abolió la pena de muerte, pero dejó una excepción para tiempos de guerra en las leyes militares. Esa excepción desapareció en 1995.",
  "La Constitució del 1978 va abolir la pena de mort, però va deixar una excepció per a temps de guerra en les lleis militars. Aquella excepció va desaparèixer el 1995.", "eticas"),
 # --- Catalunya
 ("catalunya", "131 presidentes de la Generalitat", "131 presidents de la Generalitat",
  "La lista oficial de presidentes de la Generalitat empieza en 1359 con Berenguer de Cruïlles, presidente de la Diputació del General. Por eso los presidentes actuales llevan un número tan alto.",
  "La llista oficial de presidents de la Generalitat comença el 1359 amb Berenguer de Cruïlles, president de la Diputació del General. Per això els presidents actuals porten un número tan alt.", "ecatalunyamedieval"),
 ("catalunya", "La primera ley del Parlament restaurado", "La primera llei del Parlament restaurat",
  "La Llei 1/1980 del Parlament de Catalunya fue la que declaró el 11 de septiembre Fiesta Nacional de Catalunya. Fue la primera ley aprobada tras recuperar el autogobierno.",
  "La Llei 1/1980 del Parlament de Catalunya va ser la que va declarar l'11 de setembre Festa Nacional de Catalunya. Va ser la primera llei aprovada després de recuperar l'autogovern.", "pcasanova"),
 ("catalunya", "Un contrato que dura lo que viven las cepas", "Un contracte que dura el que viuen els ceps",
  "La <i>rabassa morta</i> era un contrato agrario catalán: el propietario cedía la tierra para plantar viña y el contrato duraba mientras vivieran las cepas. Cuando la filoxera las mató a finales del siglo XIX, estalló un gran conflicto en el campo.",
  "La <i>rabassa morta</i> era un contracte agrari català: el propietari cedia la terra per plantar vinya i el contracte durava mentre visquessin els ceps. Quan la fil·loxera els va matar a finals del segle XIX, va esclatar un gran conflicte al camp.", "pcompanys"),
 ("catalunya", "Una ley aprobada dos veces", "Una llei aprovada dues vegades",
  "La Llei de contractes de conreu de 1934 fue anulada por el Tribunal de Garantías Constitucionales de la República. El Parlament de Catalunya volvió a aprobarla, casi igual, pocos días después.",
  "La Llei de contractes de conreu del 1934 va ser anul·lada pel Tribunal de Garanties Constitucionals de la República. El Parlament de Catalunya la va tornar a aprovar, gairebé igual, pocs dies després.", "erepublica"),
 ("catalunya", "La herencia catalana es distinta", "L'herència catalana és diferent",
  "En Catalunya la legítima de los hijos es solo una cuarta parte de la herencia, mucho menos que en el Código Civil estatal. Viene de una tradición que la Nueva Planta no tocó porque respetó el derecho civil catalán.",
  "A Catalunya la llegítima dels fills és només una quarta part de l'herència, molt menys que al Código Civil estatal. Ve d'una tradició que la Nova Planta no va tocar perquè va respectar el dret civil català.", "enuevaplanta"),
 ("catalunya", "Corridas de toros: prohibidas y anuladas", "Curses de braus: prohibides i anul·lades",
  "El Parlament prohibió las corridas de toros en Catalunya en 2010, a partir de una iniciativa legislativa popular. En 2016 el Tribunal Constitucional anuló la prohibición por invadir competencias del Estado.",
  "El Parlament va prohibir les curses de braus a Catalunya el 2010, a partir d'una iniciativa legislativa popular. El 2016 el Tribunal Constitucional va anul·lar la prohibició per envair competències de l'Estat.", "catalunya"),
 # --- Mujeres
 ("mujeres", "Elegibles antes que votantes", "Elegibles abans que votants",
  "En las elecciones de 1931 las mujeres podían ser elegidas, pero no votar. Clara Campoamor, Victoria Kent y Margarita Nelken fueron diputadas. Las mujeres votaron por primera vez en unas generales en noviembre de 1933.",
  "A les eleccions del 1931 les dones podien ser elegides, però no votar. Clara Campoamor, Victoria Kent i Margarita Nelken van ser diputades. Les dones van votar per primera vegada en unes generals el novembre del 1933.", "bio"),
 ("mujeres", "La licencia marital", "La llicència marital",
  "Hasta 1975 una mujer casada necesitaba el permiso de su marido para trabajar, abrir una cuenta en el banco o vender sus propios bienes. Lo suprimió la Ley 14/1975, gracias en buena parte a las juristas de María Telo.",
  "Fins al 1975 una dona casada necessitava el permís del seu marit per treballar, obrir un compte al banc o vendre els seus propis béns. Ho va suprimir la Ley 14/1975, gràcies en bona part a les juristes de María Telo.", "pmariatelo"),
 ("mujeres", "El adulterio fue delito hasta 1978", "L'adulteri va ser delicte fins al 1978",
  "Hasta 1978 el adulterio era delito, y la ley lo castigaba de forma más dura para las mujeres que para los hombres. Ese año se despenalizó, junto con la venta de anticonceptivos.",
  "Fins al 1978 l'adulteri era delicte, i la llei el castigava de manera més dura per a les dones que per als homes. Aquell any es va despenalitzar, juntament amb la venda d'anticonceptius.", "moral"),
 ("mujeres", "Juezas desde 1977", "Jutgesses des del 1977",
  "Una ley de 1966 abrió a las mujeres la carrera judicial, pero la primera jueza, Josefina Triguero, no tomó posesión hasta 1977.",
  "Una llei del 1966 va obrir a les dones la carrera judicial, però la primera jutgessa, Josefina Triguero, no va prendre possessió fins al 1977.", None),
 ("mujeres", "Estudiar Derecho vestida de hombre", "Estudiar Dret vestida d'home",
  "En el siglo XIX las mujeres no podían matricularse en la universidad. Concepción Arenal asistió como oyente a clases de Derecho en Madrid vestida de hombre.",
  "Al segle XIX les dones no es podien matricular a la universitat. Concepción Arenal va assistir com a oient a classes de Dret a Madrid vestida d'home.", "pconcepcionarenal"),
 ("mujeres", "Un artículo de periódico que cambió el Código Civil", "Un article de diari que va canviar el Código Civil",
  "En 1953 la abogada Mercedes Formica publicó en ABC «El domicilio conyugal», sobre una mujer apuñalada por su marido que, según la ley, no podía quedarse en su casa. La reforma de 1958 se conoció como «la reformica».",
  "El 1953 l'advocada Mercedes Formica va publicar a l'ABC «El domicilio conyugal», sobre una dona apunyalada pel seu marit que, segons la llei, no es podia quedar a casa seva. La reforma del 1958 es va conèixer com «la reformica».", "pmercedesformica"),
 # --- Juicios
 ("juicios", "El muerto que volvió: el crimen de Cuenca", "El mort que va tornar: el crim de Conca",
  "En 1913 dos hombres fueron condenados por matar a un pastor desaparecido en Osa de la Vega (Cuenca). Habían confesado bajo torturas. En 1926 el «muerto» reapareció vivo. El Tribunal Supremo anuló la condena y el caso se convirtió en el gran ejemplo de error judicial en España.",
  "El 1913 dos homes van ser condemnats per matar un pastor desaparegut a Osa de la Vega (Conca). Havien confessat sota tortures. El 1926 el «mort» va reaparèixer viu. El Tribunal Suprem va anul·lar la condemna i el cas es va convertir en el gran exemple d'error judicial a Espanya.", None),
 ("juicios", "El jurado ha ido y venido", "El jurat ha anat i vingut",
  "Los juicios con jurado popular existieron en España de 1888 a 1923 y durante la República. Volvieron con la Ley del Jurado de 1995, que hoy se aplica a delitos como el homicidio o la malversación.",
  "Els judicis amb jurat popular van existir a Espanya del 1888 al 1923 i durant la República. Van tornar amb la Ley del Jurado del 1995, que avui s'aplica a delictes com l'homicidi o la malversació.", None),
 ("juicios", "Un duelo que nunca fue", "Un duel que no va ser mai",
  "En 1283 Pere el Gran y Carlos de Anjou acordaron decidir la guerra de Sicilia en un combate de cien caballeros por bando en Burdeos. Ninguno de los dos se encontró con el otro en el campo, y cada uno acusó al otro de cobardía.",
  "El 1283 Pere el Gran i Carles d'Anjou van acordar decidir la guerra de Sicília en un combat de cent cavallers per bàndol a Bordeus. Cap dels dos no es va trobar amb l'altre al camp, i cadascun va acusar l'altre de covardia.", "ppedroiii"),
 ("juicios", "Núremberg y la palabra genocidio", "Nuremberg i la paraula genocidi",
  "La palabra «genocidio» la inventó el jurista Raphael Lemkin en 1944. En los juicios de Núremberg se usó en la acusación, pero el delito de genocidio no se definió en un tratado hasta la Convención de la ONU de 1948.",
  "La paraula «genocidi» la va inventar el jurista Raphael Lemkin el 1944. Als judicis de Nuremberg es va fer servir en l'acusació, però el delicte de genocidi no es va definir en un tractat fins a la Convenció de l'ONU del 1948.", "juicio"),
 ("juicios", "Tortura en el derecho: abolida en 1811", "Tortura en el dret: abolida el 1811",
  "La tortura era un medio legal para obtener confesiones. Las Cortes de Cádiz la abolieron en 1811, aunque Fernando VII restauró parte del viejo sistema al volver en 1814.",
  "La tortura era un mitjà legal per obtenir confessions. Les Corts de Cadis la van abolir el 1811, tot i que Ferran VII va restaurar part del vell sistema en tornar el 1814.", "ecadiz"),
 # --- Europa
 ("europa", "España entró en Europa un 1 de enero", "Espanya va entrar a Europa un 1 de gener",
  "España y Portugal firmaron el tratado de adhesión a la Comunidad Económica Europea el 12 de junio de 1985 y entraron el 1 de enero de 1986. Desde entonces, buena parte de nuestras leyes nacen en Bruselas.",
  "Espanya i Portugal van signar el tractat d'adhesió a la Comunitat Econòmica Europea el 12 de juny de 1985 i hi van entrar l'1 de gener de 1986. Des de llavors, bona part de les nostres lleis neixen a Brussel·les.", "internacional"),
 ("europa", "Un mismo texto en 24 idiomas", "Un mateix text en 24 idiomes",
  "Cada ley europea se publica en las 24 lenguas oficiales de la Unión, y todas las versiones valen lo mismo. El catalán no es lengua oficial de la UE, aunque desde 2005 se puede escribir en catalán a algunas instituciones y recibir respuesta.",
  "Cada llei europea es publica en les 24 llengües oficials de la Unió, i totes les versions valen el mateix. El català no és llengua oficial de la UE, tot i que des del 2005 es pot escriure en català a algunes institucions i rebre'n resposta.", "internacional"),
 ("europa", "El fin del roaming", "La fi del roaming",
  "Desde el 15 de junio de 2017 usar el móvil en otro país de la Unión cuesta lo mismo que en casa. Lo decidió un reglamento europeo, que se aplica directamente sin necesidad de ley española.",
  "Des del 15 de juny de 2017 fer servir el mòbil en un altre país de la Unió costa el mateix que a casa. Ho va decidir un reglament europeu, que s'aplica directament sense necessitat de llei espanyola.", None),
 ("europa", "El 112 funciona en toda Europa", "El 112 funciona a tot Europa",
  "Desde 1991 el 112 es el número de emergencias común en la Unión Europea: es gratis y funciona desde cualquier teléfono, también sin saldo.",
  "Des del 1991 el 112 és el número d'emergències comú a la Unió Europea: és gratuït i funciona des de qualsevol telèfon, també sense saldo.", None),
 ("europa", "Por qué hay tantos avisos de cookies", "Per què hi ha tants avisos de galetes",
  "Las normas europeas obligan a pedir permiso antes de guardar cookies que no son imprescindibles, y el Reglamento General de Protección de Datos se aplica desde el 25 de mayo de 2018. Leypedia no usa cookies.",
  "Les normes europees obliguen a demanar permís abans de desar galetes que no són imprescindibles, i el Reglament General de Protecció de Dades s'aplica des del 25 de maig de 2018. Leypedia no fa servir galetes.", None),
]

def cu_card(c, lang):
    es = lang == "es"
    cat, te, tc, xe, xc, lk = c
    name = dict((a, (b, d)) for a, b, d in CCAT)[cat][0 if es else 1]
    more = f'<a class="go" href="{{{lk}}}">{"Saber más" if es else "Saber-ne més"}</a>' if lk else ""
    return f'<article class="cu"><span class="label">{name}</span><h3>{te if es else tc}</h3><p>{xe if es else xc}</p>{more}</article>'

def cu_index(lang):
    es = lang == "es"
    i = 0 if es else 1
    nav = '<div class="subt">' + "".join(f'<a href="#{c}">{t if es else u}</a>' for c, t, u in CCAT) + '</div>'
    out = f'<p class="status" style="margin-top:14px">{len(CU)} {"curiosidades y anécdotas" if es else "curiositats i anècdotes"}</p>'
    for c, t, u in CCAT:
        out += f'<section class="cgroup" id="{c}"><h2>{t if es else u}</h2><div class="cugrid">' + "".join(cu_card(x, lang) for x in CU if x[0] == c) + '</div></section>'
    out += ('<div class="box cc" style="margin-top:28px"><h3>' + ("Más anécdotas en la enciclopedia" if es else "Més anècdotes a l'enciclopèdia") + '</h3><p>'
            + ("Cada época y cada personaje de la enciclopedia tiene su propia anécdota." if es else "Cada època i cada personatge de l'enciclopèdia té la seva pròpia anècdota.")
            + f' <a href="{{enciclopedia}}">{"Abrir la enciclopedia" if es else "Obrir l&#39;enciclopèdia"}</a></p></div>')
    return nav + out

PAGES["curiosidades"] = {L: dict(
    title="Curiosidades y anécdotas del derecho" if L == "es" else "Curiositats i anècdotes del dret",
    desc=("Curiosidades y anécdotas de la historia del derecho en España, Catalunya y Europa: palabras, leyes antiguas, juicios célebres y mujeres que cambiaron la ley." if L == "es"
          else "Curiositats i anècdotes de la història del dret a Espanya, Catalunya i Europa: paraules, lleis antigues, judicis cèlebres i dones que van canviar la llei."),
    crumbs=[("historia", "Historia" if L == "es" else "Història")],
    html=simple("Historia" if L == "es" else "Història",
                "Curiosidades y anécdotas" if L == "es" else "Curiositats i anècdotes",
                ("Lo que no suele contarse de las leyes: de dónde vienen las palabras, qué normas del siglo XIX siguen vigentes y qué juicios cambiaron la historia." if L == "es"
                 else "El que no s'acostuma a explicar de les lleis: d'on vénen les paraules, quines normes del segle XIX continuen vigents i quins judicis van canviar la història."),
                cu_index(L))) for L in ("es", "ca")}

# Enlaces desde Historia y desde la portada
_pick = [CU[i] for i in (13, 29, 1)]
for L in ("es", "ca"):
    es = L == "es"
    blk = (f'<h2 class="sec">{"Curiosidades y anécdotas" if es else "Curiositats i anècdotes"}</h2><div class="cugrid">' + "".join(cu_card(x, L) for x in _pick) + '</div>'
           f'<p style="margin-top:14px"><a class="btn" href="{{curiosidades}}">{"Ver las " if es else "Veure les "}{len(CU)} {"curiosidades" if es else "curiositats"}</a></p>')
    h = PAGES["historia"][L]["html"]
    tag = '<h2 class="sec">' + ("Línea del tiempo" if es else "Línia del temps")
    PAGES["historia"][L]["html"] = h.replace(tag, blk + tag, 1)
    hh = PAGES["home"][L]["html"]
    end = f'{"Abrir la enciclopedia" if es else "Obrir l&#39;enciclopèdia"}</a></p>'
    assert end in hh
    PAGES["home"][L]["html"] = hh.replace(end, end[:-4] + f' <a class="btn ghost" href="{{curiosidades}}">{"Curiosidades y anécdotas" if es else "Curiositats i anècdotes"}</a></p>', 1)
