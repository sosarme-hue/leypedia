# Filopedia y enfermeria.si (noviembre de 2026). Se añade a SITIOS desde sitios.py.
from sitios import F0, F1, F2, F3, F4, F5, F6, F7, F8
from sitios_tn import css, A
from plantillas_fe import PLANT

FP, EP = PLANT['filopedia'], PLANT['enfermeria']
COMMONS = 'https://commons.wikimedia.org/wiki/Special:FilePath/'

def E(f, img, es):  # Enfermería: solo español
    return {'fecha': f, 'img': img, 'es': es, 'en': es}

FE = {
 'filopedia': {
  'nombre': 'Filopedia', 'dominio': 'filopedia.com', 'autor': 'Alejandro Rosàs',
  'js_menu': 'assets/busca.js', 'clase_fig': 'blog-fig', 'clase_miga': 'miga',
  'pref': {'a': 'a/', 'o': 'o/', 'c': 'c/', 'g': 'g/'},
  'css': css('var(--marca)', 'var(--suave)', 'var(--tinta)', 'var(--blanco)', 'var(--linea)', '#e8e4da'),
  'head': FP['head'], 'cab': FP['cab'], 'pie': FP['pie'],
  'indice': {'es': ('El blog de Filopedia', 'Historias de filósofos, escritores y libros que cambiaron nuestra forma de pensar. Un artículo nuevo cada martes.'),
             'en': ('The Filopedia blog', 'Stories of philosophers, writers and books that changed the way we think. A new post every Tuesday.')},
  'articulos': {
   'socrates': A(F0, 'img/r/Q913.jpg',
     ('socrates-el-filosofo-que-solo-sabia-que-no-sabia-nada', 'Sócrates, el filósofo que solo sabía que no sabía nada', 'Hoy es el Día Mundial de la Filosofía. Lo celebramos con el ateniense que nunca escribió un libro y cambió el pensamiento para siempre.', 5),
     ('socrates-the-philosopher-who-knew-he-knew-nothing', 'Socrates, the philosopher who knew that he knew nothing', 'Today is World Philosophy Day. We celebrate it with the Athenian who never wrote a book and changed thought for ever.', 5)),
   'cervantes': A(F0, 'img/r/Q5682.jpg',
     ('cervantes-y-el-quijote', 'Cervantes y el Quijote, la primera novela moderna', 'Un soldado herido en Lepanto, cautivo en Argel y recaudador de impuestos escribió el libro más famoso en español.', 6),
     ('cervantes-and-don-quixote', 'Cervantes and Don Quixote, the first modern novel', 'A soldier wounded at Lepanto, held captive in Algiers and later a tax collector wrote the most famous book in Spanish.', 6)),
   'beauvoir': A(F0, 'img/r/Q7197.jpg',
     ('simone-de-beauvoir-y-el-segundo-sexo', 'Simone de Beauvoir y «El segundo sexo»', '«No se nace mujer: se llega a serlo». La filósofa que dio al feminismo una de sus frases más citadas.', 5),
     ('simone-de-beauvoir-and-the-second-sex', 'Simone de Beauvoir and «The Second Sex»', '«One is not born, but rather becomes, a woman». The philosopher who gave feminism one of its most quoted lines.', 5)),
   'spinoza': A(F1, 'img/r/Q35802.jpg',
     ('spinoza-el-filosofo-que-pulia-lentes', 'Spinoza, el filósofo que pulía lentes', 'Nació en Ámsterdam el 24 de noviembre de 1632, fue expulsado de su comunidad y escribió una ética como si fuera geometría.', 5),
     ('spinoza-the-philosopher-who-ground-lenses', 'Spinoza, the philosopher who ground lenses', 'Born in Amsterdam on 24 November 1632, he was cast out of his community and wrote an ethics as if it were geometry.', 5)),
   'montaigne': A(F2, 'img/r/Q41568.jpg',
     ('montaigne-y-el-invento-del-ensayo', 'Montaigne y el invento del ensayo', 'Un noble francés se encerró en su torre a escribir sobre sí mismo y creó un género literario nuevo.', 5),
     ('montaigne-and-the-invention-of-the-essay', 'Montaigne and the invention of the essay', 'A French nobleman shut himself in his tower to write about himself and created a new literary genre.', 5)),
   'dickinson': A(F3, 'img/r/Q4441.jpg',
     ('emily-dickinson-la-poeta-que-no-quiso-publicar', 'Emily Dickinson, la poeta que no quiso publicar', 'Nació el 10 de diciembre de 1830. Escribió casi 1.800 poemas y en vida solo vio impresos unos pocos.', 5),
     ('emily-dickinson-the-poet-who-would-not-publish', 'Emily Dickinson, the poet who would not publish', 'She was born on 10 December 1830. She wrote nearly 1,800 poems and saw only a handful printed in her lifetime.', 5)),
   'austen': A(F4, 'img/r/Q36322.jpg',
     ('jane-austen-y-orgullo-y-prejuicio', 'Jane Austen y «Orgullo y prejuicio»', 'Nació el 16 de diciembre de 1775 y publicó su primera novela firmada solo «por una dama». Hoy es una de las novelistas más leídas del mundo.', 5),
     ('jane-austen-and-pride-and-prejudice', 'Jane Austen and «Pride and Prejudice»', 'Born on 16 December 1775, she published her first novel signed only «By a Lady». Today she is one of the most widely read novelists in the world.', 5)),
   'dickens': A(F5, 'img/r/Q5686.jpg',
     ('dickens-y-cuento-de-navidad', 'Dickens y «Cuento de Navidad»', 'En 1843 Charles Dickens escribió en seis semanas la historia de Scrooge, y cambió la forma de celebrar la Navidad.', 5),
     ('dickens-and-a-christmas-carol', 'Dickens and «A Christmas Carol»', 'In 1843 Charles Dickens wrote the story of Scrooge in six weeks, and changed the way Christmas is celebrated.', 5)),
   'platon': A(F6, 'img/r/Q859.jpg',
     ('platon-y-el-mito-de-la-caverna', 'Platón y el mito de la caverna', 'Unos prisioneros que solo ven sombras: la imagen más famosa de la filosofía, explicada para empezar el año.', 5),
     ('plato-and-the-allegory-of-the-cave', 'Plato and the allegory of the cave', 'Prisoners who only ever see shadows: the most famous image in philosophy, explained to start the year.', 5)),
   'tolkien': A(F7, 'img/r/Q892.jpg',
     ('tolkien-el-profesor-que-invento-la-tierra-media', 'Tolkien, el profesor que inventó la Tierra Media', 'Nació el 3 de enero de 1892. Un filólogo de Oxford que empezó inventando lenguas y acabó creando un mundo.', 6),
     ('tolkien-the-professor-who-invented-middle-earth', 'Tolkien, the professor who invented Middle-earth', 'Born on 3 January 1892, an Oxford philologist who began by inventing languages and ended up creating a world.', 6)),
   'arendt': A(F8, 'img/r/Q60025.jpg',
     ('hannah-arendt-y-la-banalidad-del-mal', 'Hannah Arendt y la banalidad del mal', 'La filósofa que asistió al juicio de Eichmann y descubrió que el mal más terrible puede venir de personas corrientes.', 6),
     ('hannah-arendt-and-the-banality-of-evil', 'Hannah Arendt and the banality of evil', 'The philosopher who attended the Eichmann trial and found that the most terrible evil can come from ordinary people.', 6)),
  },
 },
 'enfermeria': {
  'nombre': 'enfermeria.si', 'dominio': 'enfermeria.si', 'autor': 'Alejandro Rosàs',
  'idiomas': ['es'], 'no_tocar_web': True,
  'envoltura': ('<div class="wrap" id="contenido">', '</div>'),
  'clase_fig': 'blog-fig', 'clase_miga': 'crumbs',
  'pref': {'u': ''},
  'css': css('var(--scrub)', 'var(--muted)', 'var(--ink)', 'var(--card)', 'var(--line)', 'var(--line)')
         + '\n.blog-fig img{width:auto;aspect-ratio:auto;object-fit:contain}.blog-card img{aspect-ratio:auto}.blog-texto h2{font-family:Bitter,Georgia,serif}',
  'head': EP['head'], 'cab': EP['cab'], 'pie': EP['pie'],
  'indice': {'es': ('El blog de enfermeria.si', 'Historia de la enfermería, consejos de cuidados y preparación del EIR. Un artículo nuevo cada martes.')},
  'articulos': {
   'nightingale': E(F0, 'assets/img/barrett.jpg',
     ('florence-nightingale-la-dama-de-la-lampara', 'Florence Nightingale, la dama de la lámpara', 'En noviembre de 1854 llegó al hospital militar de Scutari. Lo que hizo allí fundó la enfermería moderna.', 5)),
   'manos': E(F0, 'assets/img/manos.jpg',
     ('la-higiene-de-manos-el-gesto-que-mas-vidas-salva', 'La higiene de manos, el gesto que más vidas salva', 'Cuándo, cómo y con qué: los cinco momentos de la OMS y los errores más habituales.', 5)),
   'eir': E(F0, 'assets/img/consulta-cap.jpg',
     ('como-preparar-el-eir', 'Cómo preparar el EIR: un plan para los meses que quedan', 'Organizar el estudio, hacer simulacros y repasar sin agobiarse. Consejos prácticos para llegar al examen en forma.', 6)),
   'henderson': E(F1, 'assets/img/poston.jpg',
     ('virginia-henderson-y-las-14-necesidades', 'Virginia Henderson y las 14 necesidades básicas', 'La enfermera estadounidense que definió qué hace una enfermera y cuyo modelo se sigue usando en España.', 5)),
   'sida': E(F2, 'assets/img/lleida.jpg',
     ('el-sida-y-la-enfermeria', 'Día Mundial del Sida: el papel de la enfermería', 'Cada 1 de diciembre recordamos una epidemia que cambió la sanidad. Las enfermeras estuvieron en primera línea desde el principio.', 5)),
   'glasgow': E(F3, 'assets/img/portada.jpg',
     ('historia-de-la-escala-de-glasgow', 'La historia de la escala de Glasgow', 'Dos neurocirujanos escoceses crearon en 1974 la escala que hoy se usa en todo el mundo para valorar la conciencia.', 5)),
   'cuidador': E(F4, 'assets/img/calcetin.jpg',
     ('cuidar-al-que-cuida', 'Cuidar al que cuida', 'Quien atiende cada día a un familiar dependiente también necesita cuidados. Señales de alarma y ayudas.', 5)),
   'atragantamiento': E(F5, 'assets/img/casa.jpg',
     ('atragantamientos-en-las-comidas-de-navidad', 'Atragantamientos en las comidas de Navidad: qué hacer', 'Turrones, mariscos y uvas de Nochevieja. Cómo prevenir el atragantamiento y cómo actuar si ocurre.', 5)),
   'zendal': E(F6, COMMONS + 'Francisco_J._Balmis_%2849919701747%29.jpg?width=640',
     ('isabel-zendal-la-primera-enfermera-en-mision-internacional', 'Isabel Zendal, la enfermera de la expedición Balmis', 'Cuidó de los niños que llevaron la vacuna de la viruela a América y Asia. Se la recuerda como la primera enfermera de una misión sanitaria internacional.', 5)),
   'caidas': E(F7, 'assets/img/silla.jpg',
     ('prevenir-caidas-en-personas-mayores', 'Cómo prevenir caídas en personas mayores', 'Una de cada tres personas mayores de 65 años se cae al menos una vez al año. Qué se puede hacer en casa.', 5)),
   'eir2': E(F8, 'assets/img/cap-granollers.jpg',
     ('ultimos-consejos-para-el-eir', 'Últimos consejos para el EIR', 'Las semanas finales, la víspera y el día del examen: cómo repasar, descansar y gestionar el tiempo.', 5)),
  },
 },
}
