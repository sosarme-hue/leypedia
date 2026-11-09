# -*- coding: utf-8 -*-
# Enciclopedia de historia del derecho en España y Catalunya: épocas y personajes
from pages3 import *

# Créditos de imágenes (todas de Wikimedia Commons, guardadas en assets/img/)
C = "https://commons.wikimedia.org/wiki/File:"
IMG = {
 "home-congreso": ("Columnas y fachada del Congreso de los Diputados de España.JPG", "Diliff", "CC BY 3.0"),
 "home-parlament": ("Palace of the Parliament of Catalonia IMG 1634.JPG", "Wistula", "CC BY-SA 3.0"),
 "home-cortes-cadiz": ("Cortes de cadiz.jpg", "Salvador Viniegra", "Dominio público"),
 "home-berlaymont": ("Berlaymont building (DSCF7542-DSCF7548).jpg", "Trougnouf", "CC BY 4.0"),
 "home-constitucion": ("Constitucion espanola 1978.JPG", "miguelazo84", "CC BY-SA 3.0"),
 "doc-usatges": ("Usatici Barchinonae-Usatges de Barcelona-AMLL.Ms-1378-co.jpg", "Mestre de l'Escrivà", "Dominio público"),
 "doc-liber": ("Liber Iudiciorum visigòtic.png", "Abadia de Montserrat", "Dominio público"),
 "doc-fuero-juzgo": ("Fuero Juzgo.jpg", "Scriptorium de Fernando III", "Dominio público"),
 "doc-nueva-planta": ("Nova planta Catalunya 1.jpg", "Imprenta de Joseph Teixidó", "Dominio público"),
 "p-alfonso-x": ("Alfonso X el Sabio en El libro de los juegos.jpg", "Autor desconocido, s. XIII", "Dominio público"),
 "p-jaime-i": ("El rey Jaime I el Conquistador, por Jaume Mateu.jpg", "Gonçal Peris y Jaume Mateu", "Dominio público"),
 "p-ramon-berenguer-i": ("RamonBerenguel1prijimatribut.jpg", "Autor desconocido, s. XII", "Dominio público"),
 "p-isidoro": ("Isidor von Sevilla.jpeg", "Bartolomé Esteban Murillo", "Dominio público"),
 "p-recesvinto": ("Reyes visigodos Codex Vigilanus - Recesvinto.jpg", "Codex Vigilanus, s. X", "Dominio público"),
 "p-felipe-v": ("Felipe V de España.jpg", "Jean Ranc", "Dominio público"),
 "p-arguelles": ("Agustín de Argüelles Álvarez (Congreso de los Diputados de España).jpg", "Ignacio Suárez Llanos", "Dominio público"),
 "p-jovellanos": ("Francisco de Goya y Lucientes - Gaspar Melchor de Jovellanos.jpg", "Francisco de Goya", "Dominio público"),
 "p-alonso-martinez": ("Manuel Alonso Martínez.jpg", "Autor desconocido", "Dominio público"),
 "p-duran-i-bas": ("Manuel Durán y Bas, de Audouard.jpg", "Pau Audouard", "Dominio público"),
 "p-concepcion-arenal": ("Concepcion Arenal 1.jpg", "Autor desconocido", "Dominio público"),
 "p-clara-campoamor": ("Clara Campoamor-2.jpg", "Virgilio Muro", "Dominio público"),
 "p-victoria-kent": ("Victoria Kent.png", "Autor desconocido", "Dominio público"),
 "p-macia": ("Macia 2a tongada scans 003 editora 8 44 1.jpg", "Arxiu Espai Macià", "Dominio público"),
 "p-tarradellas": ("(Josep Tarradellas) Adolfo Suárez junto al presidente de la Generalitat de Cataluña a su llegada a Barcelona. Pool Moncloa. 24 de febrero de 1979 (cropped).jpeg", "Pool Moncloa", "Atribución"),
 "p-peces-barba": ("(Peces-Barba) Felipe González junto al presidente del Senado y el presidente del Congreso (cropped).jpeg", "Pool Moncloa", "Atribución"),
 "p-joaquin-costa": ("Joaquín Costa, de Compañy (cropped).jpg", "Manuel Compañy", "Dominio público"),
 "p-fernando-vii": ("Fernando VII - Vicente López.jpg", "Vicente López Portaña", "Dominio público"),
 "p-azana": ("Manuel Azaña cropped.jpg", "Autor desconocido", "Dominio público"),
}
import os as _os
IMG_OK = {f[:-4] for f in _os.listdir(_os.path.join(_os.path.dirname(__file__), "img")) if f.endswith(".jpg")}

def foto(slug, alt, lang, cls="foto"):
    if slug not in IMG or slug not in IMG_OK:
        return ""
    f, a, l = IMG[slug]
    if lang == "ca":
        l = {"Dominio público": "Domini públic", "Atribución": "Atribució"}.get(l, l)
        a = a.replace("Autor desconocido", "Autor desconegut")
    return (f'<figure class="{cls}"><img src="{{img}}{slug}.jpg" alt="{alt}" loading="lazy">'
            f'<figcaption>{a} · {l} · <a href="{C}{f.replace(" ", "_")}" rel="noopener">Wikimedia Commons</a></figcaption></figure>')

def k(slug):  # clave de ruta: solo letras minúsculas
    return "".join(c for c in slug if c.isalpha())

# ---------------- PERSONAJES ----------------
# slug: (nombre, nace, muere, epoca, papel_es, papel_ca, texto_es, texto_ca, anecdota_es, anecdota_ca)
P = {
 "isidoro": ("Isidoro de Sevilla", "c. 560", "636", "visigodo",
   "Obispo de Sevilla y sabio", "Bisbe de Sevilla i savi",
   "<p>Fue el gran sabio de la Hispania visigoda. En sus <i>Etimologías</i> recogió todo el saber de su tiempo, incluido el derecho, y definió qué debía ser una buena ley: justa, posible, adecuada a las costumbres del lugar y escrita con claridad para que todos la entendieran.</p><p>Presidió el IV Concilio de Toledo (633), donde se fijaron reglas sobre la elección del rey y sus límites.</p>",
   "<p>Va ser el gran savi de la Hispània visigoda. A les <i>Etimologías</i> va recollir tot el saber del seu temps, inclòs el dret, i va definir com havia de ser una bona llei: justa, possible, adequada als costums del lloc i escrita amb claredat perquè tothom l'entengués.</p><p>Va presidir el IV Concili de Toledo (633), on es van fixar regles sobre l'elecció del rei i els seus límits.</p>",
   "Su frase más citada sobre el poder: «Serás rey si obras con rectitud; si no, no lo serás».",
   "La seva frase més citada sobre el poder: «Seràs rei si obres amb rectitud; si no, no ho seràs»."),
 "recesvinto": ("Recesvinto", "?", "672", "visigodo",
   "Rey visigodo", "Rei visigot",
   "<p>Hacia el año 654 promulgó el <i>Liber Iudiciorum</i>, un código que se aplicaba por igual a godos e hispanorromanos. Hasta entonces cada pueblo tenía su propio derecho. Fue la primera vez que en la península rigió una única ley para todos.</p>",
   "<p>Cap a l'any 654 va promulgar el <i>Liber Iudiciorum</i>, un codi que s'aplicava igual a gots i hispanoromans. Fins aleshores cada poble tenia el seu propi dret. Va ser la primera vegada que a la península va regir una única llei per a tothom.</p>",
   "Su corona votiva de oro y piedras preciosas apareció en 1858 en el tesoro de Guarrazar (Toledo) y hoy se expone en el Museo Arqueológico Nacional.",
   "La seva corona votiva d'or i pedres precioses va aparèixer el 1858 al tresor de Guarrazar (Toledo) i avui s'exposa al Museo Arqueológico Nacional."),
 "ramon-berenguer-i": ("Ramon Berenguer I", "c. 1023", "1076", "catalunya-medieval",
   "Conde de Barcelona", "Comte de Barcelona",
   "<p>La tradición le atribuye los <i>Usatges de Barcelona</i>, las costumbres jurídicas del condado puestas por escrito. En realidad el texto se fue completando durante el siglo XII, pero se convirtió en la base del derecho catalán durante siglos.</p>",
   "<p>La tradició li atribueix els <i>Usatges de Barcelona</i>, els costums jurídics del comtat posats per escrit. En realitat el text es va anar completant durant el segle XII, però es va convertir en la base del dret català durant segles.</p>",
   "Fue excomulgado por el papa por casarse con Almodis de la Marca, que seguía casada con otro hombre.",
   "Va ser excomunicat pel papa per casar-se amb Almodis de la Marca, que encara estava casada amb un altre home."),
 "jaime-i": ("Jaime I el Conquistador", "1208", "1276", "catalunya-medieval",
   "Rey de Aragón, de Mallorca y de Valencia, y conde de Barcelona", "Rei d'Aragó, de Mallorca i de València, i comte de Barcelona",
   "<p>Dio leyes a los territorios que conquistó: los <i>Furs de València</i> y la carta de franquicia de Mallorca. En Aragón impulsó los Fueros de Aragón de 1247, aprobados en Huesca. En Barcelona organizó el gobierno municipal, origen del Consell de Cent.</p>",
   "<p>Va donar lleis als territoris que va conquerir: els <i>Furs de València</i> i la carta de franquesa de Mallorca. A l'Aragó va impulsar els Furs d'Aragó del 1247, aprovats a Osca. A Barcelona va organitzar el govern municipal, origen del Consell de Cent.</p>",
   "Dictó su propia autobiografía, el <i>Llibre dels fets</i>, en catalán: una de las primeras memorias de un rey en Europa.",
   "Va dictar la seva pròpia autobiografia, el <i>Llibre dels fets</i>, en català: una de les primeres memòries d'un rei a Europa."),
 "alfonso-x": ("Alfonso X el Sabio", "1221", "1284", "castilla",
   "Rey de Castilla y de León", "Rei de Castella i de Lleó",
   "<p>Quiso unificar el derecho de sus reinos. Mandó redactar el Fuero Real y, sobre todo, las Siete Partidas, escritas en castellano. Las Partidas estuvieron vigentes como derecho supletorio hasta el Código Civil de 1889 y se aplicaron en toda la América española.</p>",
   "<p>Va voler unificar el dret dels seus regnes. Va fer redactar el Fuero Real i, sobretot, les Siete Partidas, escrites en castellà. Les Partidas van ser vigents com a dret supletori fins al Código Civil del 1889 i es van aplicar a tota l'Amèrica espanyola.</p>",
   "Su retrato más conocido procede del <i>Libro de los juegos</i>, un tratado sobre ajedrez, dados y tablas que él mismo encargó.",
   "El seu retrat més conegut prové del <i>Libro de los juegos</i>, un tractat sobre escacs, daus i taules que ell mateix va encarregar."),
 "felipe-v": ("Felipe V", "1683", "1746", "nueva-planta",
   "Rey de España, primero de la dinastía Borbón", "Rei d'Espanya, primer de la dinastia Borbó",
   "<p>Tras ganar la Guerra de Sucesión, aprobó los Decretos de Nueva Planta: Aragón y Valencia en 1707, Mallorca en 1715 y Catalunya en 1716. Suprimió las Corts, la Generalitat y las instituciones propias de la Corona de Aragón, pero en Catalunya se mantuvo el derecho civil catalán.</p>",
   "<p>Després de guanyar la Guerra de Successió, va aprovar els Decrets de Nova Planta: Aragó i València el 1707, Mallorca el 1715 i Catalunya el 1716. Va suprimir les Corts, la Generalitat i les institucions pròpies de la Corona d'Aragó, però a Catalunya es va mantenir el dret civil català.</p>",
   "Reinó dos veces: abdicó en su hijo Luis I en 1724 y volvió al trono pocos meses después, cuando Luis murió de viruela.",
   "Va regnar dues vegades: va abdicar en el seu fill Lluís I el 1724 i va tornar al tron pocs mesos després, quan Lluís va morir de verola."),
 "jovellanos": ("Gaspar Melchor de Jovellanos", "1744", "1811", "cadiz",
   "Jurista, escritor y político ilustrado", "Jurista, escriptor i polític il·lustrat",
   "<p>Magistrado y ministro de Gracia y Justicia, fue la gran figura de la Ilustración española. Su <i>Informe sobre la ley agraria</i> (1795) pedía reformar la propiedad de la tierra. Durante la guerra contra Napoleón formó parte de la Junta Central, que preparó la convocatoria de las Cortes de Cádiz.</p>",
   "<p>Magistrat i ministre de Gracia y Justicia, va ser la gran figura de la Il·lustració espanyola. El seu <i>Informe sobre la ley agraria</i> (1795) demanava reformar la propietat de la terra. Durant la guerra contra Napoleó va formar part de la Junta Central, que va preparar la convocatòria de les Corts de Cadis.</p>",
   "Pasó siete años preso en Mallorca, en el castillo de Bellver, por sus ideas. Goya lo retrató en 1798.",
   "Va passar set anys pres a Mallorca, al castell de Bellver, per les seves idees. Goya el va retratar el 1798."),
 "arguelles": ("Agustín Argüelles", "1776", "1844", "cadiz",
   "Diputado en las Cortes de Cádiz", "Diputat a les Corts de Cadis",
   "<p>Fue uno de los principales autores de la Constitución de 1812 y redactó buena parte de su <i>Discurso preliminar</i>, que explica sus principios: soberanía nacional, separación de poderes y derechos de los ciudadanos. Defendió en las Cortes la abolición de la tortura.</p>",
   "<p>Va ser un dels principals autors de la Constitució del 1812 i va redactar bona part del seu <i>Discurso preliminar</i>, que n'explica els principis: sobirania nacional, separació de poders i drets dels ciutadans. Va defensar a les Corts l'abolició de la tortura.</p>",
   "Le llamaban «el Divino» por su manera de hablar en público. Años después fue tutor de la reina Isabel II cuando era niña.",
   "L'anomenaven «el Diví» per la seva manera de parlar en públic. Anys després va ser tutor de la reina Isabel II quan era una nena."),
 "fernando-vii": ("Fernando VII", "1784", "1833", "cadiz",
   "Rey de España", "Rei d'Espanya",
   "<p>Al volver a España en 1814 anuló la Constitución de Cádiz y persiguió a los liberales. Tuvo que jurarla en 1820 y la volvió a suprimir en 1823 con ayuda de un ejército francés. Su Pragmática Sanción de 1830 permitió reinar a su hija Isabel, lo que provocó las guerras carlistas.</p>",
   "<p>Quan va tornar a Espanya el 1814 va anul·lar la Constitució de Cadis i va perseguir els liberals. La va haver de jurar el 1820 i la va tornar a suprimir el 1823 amb l'ajuda d'un exèrcit francès. La seva Pragmàtica Sanció del 1830 va permetre regnar a la seva filla Isabel, cosa que va provocar les guerres carlines.</p>",
   "Al jurar la Constitución en 1820 dijo: «Marchemos francamente, y yo el primero, por la senda constitucional». Tres años después la abolió.",
   "Quan va jurar la Constitució el 1820 va dir: «Marchemos francamente, y yo el primero, por la senda constitucional». Tres anys després la va abolir."),
 "alonso-martinez": ("Manuel Alonso Martínez", "1827", "1891", "codificacion",
   "Ministro de Gracia y Justicia", "Ministre de Gracia y Justicia",
   "<p>Impulsó las dos grandes leyes que aún hoy nos rigen: la Ley de Enjuiciamiento Criminal de 1882, cuya exposición de motivos firmó, y el Código Civil de 1889. Para sacar adelante el Código pactó una fórmula con los territorios forales: el Código se aplicaría en ellos solo como derecho supletorio.</p>",
   "<p>Va impulsar les dues grans lleis que encara avui ens regeixen: la Ley de Enjuiciamiento Criminal del 1882, l'exposició de motius de la qual va signar, i el Código Civil del 1889. Per tirar endavant el Codi va pactar una fórmula amb els territoris forals: el Codi s'hi aplicaria només com a dret supletori.</p>",
   "La plaza y la estación de metro de Alonso Martínez, en Madrid, llevan su nombre.",
   "La plaça i l'estació de metro d'Alonso Martínez, a Madrid, porten el seu nom."),
 "duran-i-bas": ("Manuel Duran i Bas", "1823", "1907", "codificacion",
   "Jurista y político catalán", "Jurista i polític català",
   "<p>Catedrático en Barcelona y principal defensor del derecho civil catalán frente a la codificación uniforme. Su <i>Memoria acerca de las instituciones del derecho civil de Cataluña</i> (1883) recogía las instituciones catalanas que había que conservar. Fue ministro de Gracia y Justicia en 1899.</p>",
   "<p>Catedràtic a Barcelona i principal defensor del dret civil català davant la codificació uniforme. La seva <i>Memoria acerca de las instituciones del derecho civil de Cataluña</i> (1883) recollia les institucions catalanes que calia conservar. Va ser ministre de Gracia y Justicia el 1899.</p>",
   "Defendía que el derecho nace de las costumbres de cada pueblo y no de la voluntad de un legislador, una idea de la escuela histórica alemana.",
   "Defensava que el dret neix dels costums de cada poble i no de la voluntat d'un legislador, una idea de l'escola històrica alemanya."),
 "concepcion-arenal": ("Concepción Arenal", "1820", "1893", "codificacion",
   "Jurista, escritora y reformadora de las cárceles", "Jurista, escriptora i reformadora de les presons",
   "<p>Pionera del derecho penitenciario. Fue visitadora de prisiones de mujeres y defendió que la cárcel debía servir para reeducar y no solo para castigar. Escribió sobre la situación de las presas, los pobres y la educación de la mujer.</p>",
   "<p>Pionera del dret penitenciari. Va ser visitadora de presons de dones i va defensar que la presó havia de servir per reeducar i no només per castigar. Va escriure sobre la situació de les preses, els pobres i l'educació de la dona.</p>",
   "Como las mujeres no podían ir a la universidad, asistió a clases de Derecho en Madrid vestida de hombre. Su lema: «Odia el delito y compadece al delincuente».",
   "Com que les dones no podien anar a la universitat, va assistir a classes de Dret a Madrid vestida d'home. El seu lema: «Odia el delito y compadece al delincuente»."),
 "joaquin-costa": ("Joaquín Costa", "1846", "1911", "codificacion",
   "Jurista, historiador y regeneracionista", "Jurista, historiador i regeneracionista",
   "<p>Estudió el derecho de las costumbres populares, el que se aplicaba en los pueblos sin estar escrito en ninguna ley. Tras la crisis de 1898 se convirtió en la voz del regeneracionismo, que pedía modernizar el país con escuelas y obras públicas.</p>",
   "<p>Va estudiar el dret dels costums populars, el que s'aplicava als pobles sense estar escrit en cap llei. Després de la crisi del 1898 es va convertir en la veu del regeneracionisme, que demanava modernitzar el país amb escoles i obres públiques.</p>",
   "Su lema era «escuela y despensa» y pidió cerrar «con doble llave el sepulcro del Cid» para dejar de vivir de glorias pasadas.",
   "El seu lema era «escuela y despensa» i va demanar tancar «con doble llave el sepulcro del Cid» per deixar de viure de glòries passades."),
 "clara-campoamor": ("Clara Campoamor", "1888", "1972", "republica",
   "Abogada y diputada", "Advocada i diputada", "", "", "", ""),
 "victoria-kent": ("Victoria Kent", "1891", "1987", "republica",
   "Abogada, diputada y directora general de Prisiones", "Advocada, diputada i directora general de Presons",
   "<p>Fue una de las primeras mujeres abogadas de España y la primera en actuar ante un tribunal militar, en 1930. Como directora general de Prisiones (1931–1932) mandó retirar los grilletes y las cadenas de los presos y creó una nueva cárcel de mujeres.</p>",
   "<p>Va ser una de les primeres dones advocades d'Espanya i la primera a actuar davant un tribunal militar, el 1930. Com a directora general de Presons (1931–1932) va fer retirar els grillons i les cadenes dels presos i va crear una nova presó de dones.</p>",
   "En el debate sobre el voto femenino de 1931 se opuso a Clara Campoamor: pedía aplazarlo, no por estar en contra, sino porque temía su efecto en las elecciones.",
   "En el debat sobre el vot femení del 1931 es va oposar a Clara Campoamor: demanava ajornar-lo, no perquè hi estigués en contra, sinó perquè en temia l'efecte a les eleccions."),
 "macia": ("Francesc Macià", "1859", "1933", "republica",
   "Presidente de la Generalitat de Catalunya", "President de la Generalitat de Catalunya",
   "<p>El 14 de abril de 1931 proclamó la República Catalana. Tras negociar con el Gobierno de la República, se restableció la Generalitat y él fue su primer presidente. Impulsó el Estatuto de Autonomía de 1932, el primero de Catalunya.</p>",
   "<p>El 14 d'abril de 1931 va proclamar la República Catalana. Després de negociar amb el Govern de la República, es va restablir la Generalitat i ell en va ser el primer president. Va impulsar l'Estatut d'Autonomia del 1932, el primer de Catalunya.</p>",
   "Le llamaban «l'Avi» (el abuelo). El proyecto de Estatuto se redactó en 1931 en el santuario de Núria, por eso se conoce como Estatut de Núria.",
   "L'anomenaven «l'Avi». El projecte d'Estatut es va redactar el 1931 al santuari de Núria, per això es coneix com a Estatut de Núria."),
 "azana": ("Manuel Azaña", "1880", "1940", "republica",
   "Presidente del Gobierno y de la República", "President del Govern i de la República",
   "<p>Fue presidente del Gobierno entre 1931 y 1933 y presidente de la República desde 1936. Defendió en las Cortes el Estatuto de Catalunya de 1932 y las grandes reformas de la República: la separación entre Iglesia y Estado, el divorcio y la reforma del ejército.</p>",
   "<p>Va ser president del Govern entre 1931 i 1933 i president de la República des del 1936. Va defensar a les Corts l'Estatut de Catalunya del 1932 i les grans reformes de la República: la separació entre l'Església i l'Estat, el divorci i la reforma de l'exèrcit.</p>",
   "Murió en el exilio, en Montauban (Francia), en 1940. Su último gran discurso pedía «paz, piedad y perdón».",
   "Va morir a l'exili, a Montauban (França), el 1940. El seu últim gran discurs demanava «paz, piedad y perdón»."),
 "tarradellas": ("Josep Tarradellas", "1899", "1988", "democracia",
   "Presidente de la Generalitat en el exilio y a su regreso", "President de la Generalitat a l'exili i en el seu retorn",
   "<p>Presidió la Generalitat en el exilio desde 1954. En 1977, antes incluso de la Constitución, el Gobierno de Adolfo Suárez restableció provisionalmente la Generalitat y Tarradellas volvió a Barcelona como su presidente.</p>",
   "<p>Va presidir la Generalitat a l'exili des del 1954. El 1977, fins i tot abans de la Constitució, el Govern d'Adolfo Suárez va restablir provisionalment la Generalitat i Tarradellas va tornar a Barcelona com a president.</p>",
   "Su primera frase desde el balcón de la Generalitat, el 23 de octubre de 1977, se hizo famosa: «Ciutadans de Catalunya, ja sóc aquí!».",
   "La seva primera frase des del balcó de la Generalitat, el 23 d'octubre de 1977, es va fer famosa: «Ciutadans de Catalunya, ja sóc aquí!»."),
 "peces-barba": ("Gregorio Peces-Barba", "1938", "2012", "democracia",
   "Uno de los siete «padres de la Constitución»", "Un dels set «pares de la Constitució»",
   "<p>Catedrático de Filosofía del Derecho y diputado, formó parte de la ponencia de siete diputados que redactó la Constitución de 1978. Fue presidente del Congreso entre 1982 y 1986 y fundó la Universidad Carlos III de Madrid.</p>",
   "<p>Catedràtic de Filosofia del Dret i diputat, va formar part de la ponència de set diputats que va redactar la Constitució del 1978. Va ser president del Congrés entre el 1982 i el 1986 i va fundar la Universidad Carlos III de Madrid.</p>",
   "La ponencia trabajó en secreto, pero el borrador se filtró a la prensa en noviembre de 1977, antes de terminarlo.",
   "La ponència treballava en secret, però l'esborrany es va filtrar a la premsa el novembre de 1977, abans d'acabar-lo."),
}
for s in P:
    ROUTES["p" + k(s)] = (f"historia/personajes/{s}/", f"ca/historia/personatges/{s}/")
ROUTES["pclaracampoamor"] = ROUTES["bio"]

# ---------------- ÉPOCAS ----------------
# id, slug_es, slug_ca, años, título es, título ca, imagen, resumen es/ca, cambios es/ca, anécdota es/ca, curiosidad es/ca
E = [
 ("romana", "hispania-romana", "hispania-romana", "s. II a. C. – s. V",
  "Hispania romana", "Hispània romana", "",
  "Roma trajo a la península su derecho, que es la base de casi todo el derecho civil actual: propiedad, contratos, herencias y familia.",
  "Roma va portar a la península el seu dret, que és la base de gairebé tot el dret civil actual: propietat, contractes, herències i família.",
  ["Las ciudades reciben leyes municipales escritas en bronce.", "En el año 74 el emperador Vespasiano extiende el derecho latino a toda Hispania.", "En el 212 casi todos los habitantes libres pasan a ser ciudadanos romanos."],
  ["Les ciutats reben lleis municipals escrites en bronze.", "L'any 74 l'emperador Vespasià estén el dret llatí a tota la Hispània.", "El 212 gairebé tots els habitants lliures passen a ser ciutadans romans."],
  "En 1981 unos agricultores encontraron en El Saucejo (Sevilla) las tablas de bronce de la <i>Lex Irnitana</i>, la ley municipal romana más completa que se conoce.",
  "El 1981 uns pagesos van trobar a El Saucejo (Sevilla) les taules de bronze de la <i>Lex Irnitana</i>, la llei municipal romana més completa que es coneix.",
  "Palabras que usamos cada día, como «usufructo», «servidumbre» o «patrimonio», vienen directamente del derecho romano.",
  "Paraules que fem servir cada dia, com «usdefruit», «servitud» o «patrimoni», vénen directament del dret romà.", []),
 ("visigodo", "reino-visigodo", "regne-visigot", "s. V – 711",
  "El reino visigodo", "El regne visigot", "doc-liber",
  "Los visigodos empezaron aplicando un derecho para ellos y otro para los hispanorromanos. En el siglo VII unificaron ambos en un solo código.",
  "Els visigots van començar aplicant un dret per a ells i un altre per als hispanoromans. Al segle VII els van unificar en un sol codi.",
  ["Código de Eurico (c. 475), para los godos.", "Breviario de Alarico (506), para los hispanorromanos.", "<i>Liber Iudiciorum</i> (c. 654), una sola ley para todos."],
  ["Codi d'Euric (c. 475), per als gots.", "Breviari d'Alaric (506), per als hispanoromans.", "<i>Liber Iudiciorum</i> (c. 654), una sola llei per a tothom."],
  "El <i>Liber Iudiciorum</i> sobrevivió a la caída del reino: se siguió usando durante siglos y en el siglo XIII se tradujo al castellano como Fuero Juzgo.",
  "El <i>Liber Iudiciorum</i> va sobreviure a la caiguda del regne: es va continuar fent servir durant segles i al segle XIII es va traduir al castellà com a Fuero Juzgo.",
  "Los concilios de Toledo eran a la vez asambleas religiosas y políticas: en ellos se elegía al rey y se aprobaban normas del reino.",
  "Els concilis de Toledo eren alhora assemblees religioses i polítiques: s'hi escollia el rei i s'hi aprovaven normes del regne.", ["isidoro", "recesvinto"]),
 ("fueros", "al-andalus-y-fueros", "al-andalus-i-furs", "711 – s. XIII",
  "Al-Ándalus y los fueros", "Al-Àndalus i els furs", "doc-fuero-juzgo",
  "Durante siglos convivieron el derecho islámico de al-Ándalus, el derecho judío y el de los reinos cristianos, donde cada villa recibía su propio fuero.",
  "Durant segles van conviure el dret islàmic d'al-Àndalus, el dret jueu i el dels regnes cristians, on cada vila rebia el seu propi fur.",
  ["Al-Ándalus aplica el derecho islámico de la escuela malikí.", "Los reyes cristianos conceden fueros a las villas para atraer pobladores.", "1241: Fernando III da a Córdoba el Fuero Juzgo en castellano."],
  ["Al-Àndalus aplica el dret islàmic de l'escola malikita.", "Els reis cristians concedeixen furs a les viles per atreure pobladors.", "1241: Ferran III dona a Còrdova el Fuero Juzgo en castellà."],
  "En las Cortes de León de 1188 el rey Alfonso IX convocó también a representantes de las ciudades. La UNESCO considera sus decretos el testimonio documental más antiguo del parlamentarismo europeo.",
  "A les Corts de Lleó del 1188 el rei Alfons IX també va convocar representants de les ciutats. La UNESCO considera els seus decrets el testimoni documental més antic del parlamentarisme europeu.",
  "Algunos fueros castigaban con multas la ofensa de llamar «cornudo» o «gafo» (leproso) a un vecino.",
  "Alguns furs castigaven amb multes l'ofensa de dir «cornut» o «gafo» (leprós) a un veí.", []),
 ("catalunya-medieval", "catalunya-medieval", "catalunya-medieval", "s. XI – s. XV",
  "Catalunya medieval: Usatges y Constitucions", "Catalunya medieval: Usatges i Constitucions", "doc-usatges",
  "Catalunya creó un derecho propio y un sistema en el que el rey no podía hacer leyes solo: necesitaba el acuerdo de las Corts.",
  "Catalunya va crear un dret propi i un sistema en què el rei no podia fer lleis sol: necessitava l'acord de les Corts.",
  ["<i>Usatges de Barcelona</i> (s. XI–XII), las costumbres del condado por escrito.", "1283: las Corts de Barcelona establecen que las leyes generales se aprueban con las Corts.", "1359: nace la Diputació del General, origen de la Generalitat.", "<i>Llibre del Consolat de Mar</i> (s. XIV), derecho marítimo usado en todo el Mediterráneo."],
  ["<i>Usatges de Barcelona</i> (s. XI–XII), els costums del comtat per escrit.", "1283: les Corts de Barcelona estableixen que les lleis generals s'aproven amb les Corts.", "1359: neix la Diputació del General, origen de la Generalitat.", "<i>Llibre del Consolat de Mar</i> (s. XIV), dret marítim utilitzat a tot el Mediterrani."],
  "Las leyes catalanas se recopilaron en las <i>Constitucions i altres drets de Catalunya</i>. La última edición, de 1704, se imprimió pocos años antes de que la Nueva Planta las suprimiera.",
  "Les lleis catalanes es van recopilar a les <i>Constitucions i altres drets de Catalunya</i>. L'última edició, del 1704, es va imprimir pocs anys abans que la Nova Planta les suprimís.",
  "El jurista Pere Albert escribió en el siglo XIII las <i>Commemoracions</i>, un tratado sobre las relaciones feudales que todavía se cita.",
  "El jurista Pere Albert va escriure al segle XIII les <i>Commemoracions</i>, un tractat sobre les relacions feudals que encara se cita.", ["ramon-berenguer-i", "jaime-i"]),
 ("castilla", "alfonso-x-y-castilla", "alfons-x-i-castella", "s. XIII – s. XV",
  "Alfonso X y el derecho de Castilla", "Alfons X i el dret de Castella", "",
  "Castilla intentó sustituir los fueros locales por un derecho común para todo el reino, inspirado en el derecho romano.",
  "Castella va intentar substituir els furs locals per un dret comú per a tot el regne, inspirat en el dret romà.",
  ["Fuero Real (c. 1255), para las villas sin fuero.", "Siete Partidas (c. 1256–1265).", "1348: el Ordenamiento de Alcalá fija el orden de aplicación de las leyes y da valor a las Partidas."],
  ["Fuero Real (c. 1255), per a les viles sense fur.", "Siete Partidas (c. 1256–1265).", "1348: l'Ordenament d'Alcalá fixa l'ordre d'aplicació de les lleis i dona valor a les Partidas."],
  "Las Partidas se escribieron en castellano y no en latín, para que se entendieran mejor. Todavía se citan en sentencias de tribunales de Estados Unidos sobre tierras que fueron españolas.",
  "Les Partidas es van escriure en castellà i no en llatí, perquè s'entenguessin millor. Encara se citen en sentències de tribunals dels Estats Units sobre terres que van ser espanyoles.",
  "La primera letra de cada una de las siete partidas forma el nombre ALFONSO.",
  "La primera lletra de cadascuna de les set partides forma el nom ALFONSO.", ["alfonso-x"]),
 ("monarquia", "monarquia-hispanica", "monarquia-hispanica", "s. XVI – s. XVII",
  "La Monarquía Hispánica y América", "La Monarquia Hispànica i Amèrica", "",
  "La llegada a América planteó una pregunta nueva: ¿qué derechos tenían los pueblos indígenas? De ese debate nació el derecho internacional moderno.",
  "L'arribada a Amèrica va plantejar una pregunta nova: quins drets tenien els pobles indígenes? D'aquest debat va néixer el dret internacional modern.",
  ["1512: Leyes de Burgos, primeras normas sobre el trato a los indígenas.", "1542: Leyes Nuevas, que prohíben esclavizar a los indígenas.", "La Escuela de Salamanca, con Francisco de Vitoria, desarrolla el derecho de gentes.", "1567: Nueva Recopilación de las leyes de Castilla."],
  ["1512: Leyes de Burgos, primeres normes sobre el tracte als indígenes.", "1542: Leyes Nuevas, que prohibeixen esclavitzar els indígenes.", "L'Escola de Salamanca, amb Francisco de Vitoria, desenvolupa el dret de gents.", "1567: Nueva Recopilación de les lleis de Castella."],
  "En la Junta de Valladolid (1550–1551) Bartolomé de las Casas y Juan Ginés de Sepúlveda debatieron ante el emperador si era legítimo conquistar a los indígenas. Fue uno de los primeros grandes debates públicos sobre derechos humanos.",
  "A la Junta de Valladolid (1550–1551) Bartolomé de las Casas i Juan Ginés de Sepúlveda van debatre davant l'emperador si era legítim conquerir els indígenes. Va ser un dels primers grans debats públics sobre drets humans.",
  "Cada reino conservaba sus leyes: el rey de Castilla era a la vez conde de Barcelona y debía jurar las Constitucions catalanas.",
  "Cada regne conservava les seves lleis: el rei de Castella era alhora comte de Barcelona i havia de jurar les Constitucions catalanes.", []),
 ("nueva-planta", "nueva-planta", "nova-planta", "1707 – 1716",
  "La Nueva Planta", "La Nova Planta", "doc-nueva-planta",
  "Tras la Guerra de Sucesión, Felipe V suprimió las instituciones y leyes públicas de la Corona de Aragón y extendió el modelo de Castilla.",
  "Després de la Guerra de Successió, Felip V va suprimir les institucions i les lleis públiques de la Corona d'Aragó i va estendre el model de Castella.",
  ["1707: Nueva Planta de Aragón y Valencia. Valencia pierde también su derecho civil.", "1715: Nueva Planta de Mallorca.", "16 de enero de 1716: Nueva Planta de Catalunya. Desaparecen las Corts y la Generalitat, pero se mantiene el derecho civil catalán."],
  ["1707: Nova Planta d'Aragó i València. València perd també el seu dret civil.", "1715: Nova Planta de Mallorca.", "16 de gener de 1716: Nova Planta de Catalunya. Desapareixen les Corts i la Generalitat, però es manté el dret civil català."],
  "Una instrucción reservada de 1717 pedía a los corregidores introducir el castellano en Catalunya con medios suaves, «de modo que se consiga el efecto sin que se note el cuidado».",
  "Una instrucció reservada del 1717 demanava als corregidors introduir el castellà a Catalunya amb mitjans suaus, «de modo que se consiga el efecto sin que se note el cuidado».",
  "Gracias a que se mantuvo el derecho civil, instituciones catalanas como la legítima reducida o el heredamiento han llegado vivas hasta hoy.",
  "Gràcies al fet que es va mantenir el dret civil, institucions catalanes com la llegítima reduïda o l'heretament han arribat vives fins avui.", ["felipe-v"]),
 ("cadiz", "cadiz-y-el-liberalismo", "cadis-i-el-liberalisme", "1808 – 1874",
  "Cádiz y el liberalismo", "Cadis i el liberalisme", "home-cortes-cadiz",
  "Durante la guerra contra Napoleón, las Cortes reunidas en Cádiz aprobaron la primera Constitución española. El siglo XIX fue una lucha constante entre absolutismo y libertades.",
  "Durant la guerra contra Napoleó, les Corts reunides a Cadis van aprovar la primera Constitució espanyola. El segle XIX va ser una lluita constant entre absolutisme i llibertats.",
  ["1811: las Cortes abolen la tortura.", "19 de marzo de 1812: se promulga la Constitución de Cádiz.", "1813: se suprime la Inquisición.", "1814: Fernando VII la anula. Siguen décadas de constituciones que se suceden: 1837, 1845, 1869."],
  ["1811: les Corts aboleixen la tortura.", "19 de març de 1812: es promulga la Constitució de Cadis.", "1813: se suprimeix la Inquisició.", "1814: Ferran VII l'anul·la. Segueixen dècades de constitucions que se succeeixen: 1837, 1845, 1869."],
  "Se promulgó el día de San José, por eso se la conoció como «la Pepa», y el grito liberal pasó a ser «¡Viva la Pepa!».",
  "Es va promulgar el dia de Sant Josep, per això es va conèixer com «la Pepa», i el crit liberal va passar a ser «¡Viva la Pepa!».",
  "Entre los diputados de Cádiz había representantes de América y Filipinas: la Constitución se aplicaba a «los españoles de ambos hemisferios».",
  "Entre els diputats de Cadis hi havia representants d'Amèrica i les Filipines: la Constitució s'aplicava als «españoles de ambos hemisferios».", ["jovellanos", "arguelles", "fernando-vii"]),
 ("codificacion", "la-codificacion", "la-codificacio", "1822 – 1900",
  "La codificación", "La codificació", "",
  "El siglo XIX quiso ordenar todo el derecho en códigos claros, uno por materia. El gran debate fue qué hacer con los derechos civiles propios de Catalunya y otros territorios.",
  "El segle XIX va voler ordenar tot el dret en codis clars, un per matèria. El gran debat va ser què fer amb els drets civils propis de Catalunya i altres territoris.",
  ["1822: primer Código Penal.", "1829 y 1885: Códigos de Comercio.", "1882: Ley de Enjuiciamiento Criminal, todavía vigente.", "1889: Código Civil, que respeta los derechos civiles forales."],
  ["1822: primer Código Penal.", "1829 i 1885: Códigos de Comercio.", "1882: Ley de Enjuiciamiento Criminal, encara vigent.", "1889: Código Civil, que respecta els drets civils forals."],
  "La primera edición del Código Civil, de 1888, tenía tantos errores que hubo que publicar una edición corregida en 1889. Esa es la que sigue vigente, con muchas reformas.",
  "La primera edició del Código Civil, del 1888, tenia tants errors que se'n va haver de publicar una edició corregida el 1889. Aquesta és la que continua vigent, amb moltes reformes.",
  "Pasaron casi 80 años desde que la Constitución de 1812 prometía un código civil único hasta que se aprobó.",
  "Van passar gairebé 80 anys des que la Constitució del 1812 prometia un codi civil únic fins que es va aprovar.", ["alonso-martinez", "duran-i-bas", "concepcion-arenal", "joaquin-costa"]),
 ("republica", "republica-y-franquismo", "republica-i-franquisme", "1931 – 1975",
  "La II República y el franquismo", "La II República i el franquisme", "",
  "La República trajo el voto de la mujer, el divorcio y la primera autonomía de Catalunya. La dictadura de Franco suprimió todo ello durante casi cuarenta años.",
  "La República va portar el vot de la dona, el divorci i la primera autonomia de Catalunya. La dictadura de Franco ho va suprimir tot durant gairebé quaranta anys.",
  ["1931: Constitución de la II República y voto femenino.", "1932: Ley de divorcio y Estatuto de Autonomía de Catalunya.", "1938–1939: se suprimen el Estatuto, el divorcio y las libertades.", "1960: Compilación del derecho civil especial de Cataluña."],
  ["1931: Constitució de la II República i vot femení.", "1932: Llei de divorci i Estatut d'Autonomia de Catalunya.", "1938–1939: se suprimeixen l'Estatut, el divorci i les llibertats.", "1960: Compilació del dret civil especial de Catalunya."],
  "En las elecciones de 1931 las mujeres podían ser elegidas diputadas, pero todavía no podían votar. Tres de ellas consiguieron escaño.",
  "A les eleccions del 1931 les dones podien ser elegides diputades, però encara no podien votar. Tres d'elles van aconseguir escó.",
  "Durante el franquismo el derecho civil catalán sobrevivió porque se consideraba derecho privado: la Compilación de 1960 lo recogió por escrito.",
  "Durant el franquisme el dret civil català va sobreviure perquè es considerava dret privat: la Compilació del 1960 el va recollir per escrit.", ["clara-campoamor", "victoria-kent", "macia", "azana"]),
 ("democracia", "transicion-y-democracia", "transicio-i-democracia", "1975 – hoy",
  "Transición y democracia", "Transició i democràcia", "home-constitucion",
  "La Constitución de 1978 organizó España como un Estado de las autonomías. Catalunya recuperó la Generalitat y la capacidad de legislar su derecho civil.",
  "La Constitució del 1978 va organitzar Espanya com un Estat de les autonomies. Catalunya va recuperar la Generalitat i la capacitat de legislar el seu dret civil.",
  ["1976: Ley para la Reforma Política.", "1977: se restablece provisionalmente la Generalitat.", "6 de diciembre de 1978: referéndum de la Constitución.", "1979: Estatut d'Autonomia de Catalunya.", "1986: España entra en la Comunidad Económica Europea.", "2002–2017: se aprueba por libros el Codi civil de Catalunya."],
  ["1976: Ley para la Reforma Política.", "1977: es restableix provisionalment la Generalitat.", "6 de desembre de 1978: referèndum de la Constitució.", "1979: Estatut d'Autonomia de Catalunya.", "1986: Espanya entra a la Comunitat Econòmica Europea.", "2002–2017: s'aprova per llibres el Codi civil de Catalunya."],
  "La Generalitat se restableció en 1977, antes que la Constitución. Fue la única institución de la República que volvió tras la dictadura.",
  "La Generalitat es va restablir el 1977, abans que la Constitució. Va ser l'única institució de la República que va tornar després de la dictadura.",
  "El Estatut de 2006 fue recurrido ante el Tribunal Constitucional, que en 2010 anuló o reinterpretó parte de sus artículos.",
  "L'Estatut del 2006 va ser recorregut davant el Tribunal Constitucional, que el 2010 en va anul·lar o reinterpretar una part dels articles.", ["tarradellas", "peces-barba"]),
]
for e in E:
    ROUTES["e" + k(e[0])] = (f"historia/enciclopedia/{e[1]}/", f"ca/historia/enciclopedia/{e[2]}/")
ROUTES["enciclopedia"] = ("historia/enciclopedia/", "ca/historia/enciclopedia/")
EP = {e[0]: e for e in E}

def pcard(s, lang):
    n, a, b, ep, re_, rc = P[s][:6]
    img = f'<img src="{{img}}p-{s}.jpg" alt="" loading="lazy">' if f"p-{s}" in IMG_OK else '<span class="noimg">' + n[0] + '</span>'
    return f'<a class="pers" href="{{p{k(s)}}}">{img}<b>{n}</b><span>{a} – {b}</span><span>{re_ if lang == "es" else rc}</span></a>'

def epoca_page(e, lang):
    es = lang == "es"
    (eid, _, _, yrs, te, tc, im, re_, rc, ce, cc, ae, ac, cue, cuc, pers) = e
    i = E.index(e)
    prev = E[i - 1] if i else None
    nxt = E[i + 1] if i + 1 < len(E) else None
    body = (f'<div class="claro"><span class="label">{"En pocas palabras" if es else "En poques paraules"}</span><p>{re_ if es else rc}</p></div>'
      + f'<h2>{"Los principales cambios" if es else "Els principals canvis"}</h2>' + ul(ce if es else cc)
      + f'<h2>{"Anécdota" if es else "Anècdota"}</h2><p>{ae if es else ac}</p>'
      + f'<div class="claro"><span class="label">{"Curiosidad" if es else "Curiositat"}</span><p>{cue if es else cuc}</p></div>'
      + (f'<h2>{"Personajes" if es else "Personatges"}</h2><div class="perslist">' + "".join(pcard(s, lang) for s in pers) + '</div>' if pers else "")
      + '<div class="pn">' + (f'<a href="{{e{k(prev[0])}}}">‹ {prev[4] if es else prev[5]}</a>' if prev else '<span></span>')
      + (f'<a href="{{e{k(nxt[0])}}}">{nxt[4] if es else nxt[5]} ›</a>' if nxt else '') + '</div>')
    side = (foto(im, te if es else tc, lang)
      + (box("Más" if es else "Més", ul(['<a href="{hito}">Las Siete Partidas</a>' if es else '<a href="{hito}">Les Siete Partidas</a>'])) if eid == "castilla" else "")
      + box("Enciclopedia" if es else "Enciclopèdia", '<ol class="eplist">' + "".join(
          f'<li{" class=\"on\"" if x[0] == eid else ""}><a href="{{e{k(x[0])}}}">{x[4] if es else x[5]}</a></li>' for x in E) + '</ol>'))
    return ficha(("Enciclopedia · " if es else "Enciclopèdia · ") + yrs, te if es else tc, re_ if es else rc, [], body, side)

def persona_page(s, lang):
    es = lang == "es"
    n, a, b, ep, re_, rc, te, tc, ae, ac = P[s]
    e = EP[ep]
    body = ((te if es else tc)
      + f'<div class="claro"><span class="label">{"Anécdota" if es else "Anècdota"}</span><p>{ae if es else ac}</p></div>'
      + f'<p>{"Época" if es else "Època"}: <a href="{{e{k(ep)}}}">{e[4] if es else e[5]}</a></p>')
    others = [x for x in e[15] if x != s]
    side = (foto("p-" + s, n, lang, "foto retrato")
      + (box("De la misma época" if es else "De la mateixa època", ul([f'<a href="{{p{k(x)}}}">{P[x][0]}</a>' for x in others])) if others else "")
      + box("Enciclopedia" if es else "Enciclopèdia", ul([f'<a href="{{enciclopedia}}">{"Todas las épocas y personajes" if es else "Totes les èpoques i personatges"}</a>'])))
    return ficha(("Personaje · " if es else "Personatge · ") + (e[4] if es else e[5]), n, re_ if es else rc,
                 [("Nació" if es else "Va néixer", a), ("Murió" if es else "Va morir", b)], body, side)

def enciclo_index(lang):
    es = lang == "es"
    eps = '<ol class="epocas">' + "".join(
        f'<li><a href="{{e{k(e[0])}}}"><span class="yr">{e[3]}</span><b>{e[4] if es else e[5]}</b><span>{e[7] if es else e[8]}</span></a></li>' for e in E) + '</ol>'
    pers = '<div class="perslist">' + "".join(pcard(s, lang) for s in P) + '</div>'
    return (f'<h2 class="sec">{"Las épocas" if es else "Les èpoques"}</h2>' + eps
      + f'<h2 class="sec">{"Los personajes" if es else "Els personatges"}</h2>' + pers
      + f'<p class="status">{"Los retratos proceden de Wikimedia Commons y son de dominio público o tienen licencia libre. Cada imagen indica su autor y licencia." if es else "Els retrats provenen de Wikimedia Commons i són de domini públic o tenen llicència lliure. Cada imatge n’indica l’autor i la llicència."}</p>')

def build_enciclo():
    for e in E:
        PAGES["e" + k(e[0])] = {L: dict(title=(e[4] if L == "es" else e[5]) + (" · Historia del derecho" if L == "es" else " · Història del dret"),
            desc=(e[7] if L == "es" else e[8]),
            crumbs=[("historia", "Historia" if L == "es" else "Història"), ("enciclopedia", "Enciclopedia" if L == "es" else "Enciclopèdia")],
            html=epoca_page(e, L)) for L in ("es", "ca")}
    for s in P:
        if s == "clara-campoamor":
            continue
        PAGES["p" + k(s)] = {L: dict(title=P[s][0], desc=f"{P[s][0]} ({P[s][1]}–{P[s][2]}): {P[s][4] if L == 'es' else P[s][5]}.",
            crumbs=[("historia", "Historia" if L == "es" else "Història"), ("enciclopedia", "Enciclopedia" if L == "es" else "Enciclopèdia")],
            html=persona_page(s, L)) for L in ("es", "ca")}
    PAGES["enciclopedia"] = {L: dict(title="Enciclopedia de historia del derecho" if L == "es" else "Enciclopèdia d'història del dret",
        desc="La historia del derecho en España y Catalunya, de Roma a hoy: épocas, cambios, anécdotas y personajes." if L == "es" else "La història del dret a Espanya i Catalunya, de Roma a avui: èpoques, canvis, anècdotes i personatges.",
        crumbs=[("historia", "Historia" if L == "es" else "Història")],
        html=simple("Enciclopedia" if L == "es" else "Enciclopèdia",
                    "Historia del derecho en España y Catalunya" if L == "es" else "Història del dret a Espanya i Catalunya",
                    "De las leyes de bronce de Roma al Codi civil de Catalunya: once épocas, sus cambios, anécdotas y las personas que los hicieron posibles." if L == "es" else "De les lleis de bronze de Roma al Codi civil de Catalunya: onze èpoques, els seus canvis, anècdotes i les persones que els van fer possibles.",
                    enciclo_index(L))) for L in ("es", "ca")}
    # foto de Clara Campoamor en su biografía
    for L in ("es", "ca"):
        h = PAGES["bio"][L]["html"]
        PAGES["bio"][L]["html"] = h.replace('<aside class="side">', '<aside class="side">' + foto("p-clara-campoamor", "Clara Campoamor", L, "foto retrato"), 1)
        PAGES["bio"][L]["crumbs"] = [("historia", "Historia" if L == "es" else "Història"), ("enciclopedia", "Enciclopedia" if L == "es" else "Enciclopèdia")]

build_enciclo()
