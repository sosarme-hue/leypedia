# Escolapedia y Planetpedia (noviembre de 2026). Se añade a SITIOS desde sitios.py.
from sitios import F0, F1, F2, F3, F4, F5, F6, F7, F8
from sitios_tn import css, A
from plantillas_ep import PLANT

PP, ES = PLANT['planetpedia'], PLANT['escolapedia']
US = 'https://images.unsplash.com/'
Q = '?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&q=80&w=1080'

def E(f, img, es):  # Escolapedia: solo español
    return {'fecha': f, 'img': img, 'es': es, 'en': es}

def U(foto):
    return US + foto + Q

EP = {
 'planetpedia': {
  'nombre': 'Planetpedia', 'dominio': 'planetpedia.net', 'autor': 'Alejandro Rosàs',
  'no_tocar_web': True,
  'envoltura': ('<div class="wrap">', '</div>'),
  'clase_fig': 'blog-fig', 'clase_miga': 'migas',
  'pref': {'u': ''},
  'css': css('var(--teal-ink)', 'var(--ink-soft)', 'var(--ink)', 'var(--surface)', 'var(--line)', 'var(--line)'),
  'head': PP['head'], 'cab': PP['cab'], 'pie': PP['pie'], 'body': PP['body'],
  'indice': {'es': ('El blog de Planetpedia', 'Historias de la Tierra y del universo: volcanes, estrellas, exploradores y fenómenos del cielo. Un artículo nuevo cada martes.'),
             'en': ('The Planetpedia blog', 'Stories of the Earth and the universe: volcanoes, stars, explorers and wonders of the sky. A new post every Tuesday.')},
  'articulos': {
   'voyager': A(F0, 'img/universo/voyager.jpg',
     ('voyager-1-a-un-dia-luz-de-la-tierra', 'La Voyager 1, a un día luz de la Tierra', 'La nave más lejana jamás construida alcanza estos días una distancia simbólica: su señal tarda 24 horas en llegarnos.', 5),
     ('voyager-1-one-light-day-from-earth', 'Voyager 1, one light-day from Earth', 'The most distant spacecraft ever built reaches a symbolic distance these days: its signal takes 24 hours to reach us.', 5)),
   'cielo': A(F0, 'img/tierra/atmosfera_iss.jpg',
     ('por-que-el-cielo-es-azul', '¿Por qué el cielo es azul?', 'El aire es transparente y la luz del Sol es blanca. Entonces, ¿de dónde sale el azul? Y ¿por qué los atardeceres son rojos?', 5),
     ('why-is-the-sky-blue', 'Why is the sky blue?', 'Air is transparent and sunlight is white. So where does the blue come from? And why are sunsets red?', 5)),
   'extremos': A(F0, 'img/tierra/dallol.jpg',
     ('los-lugares-mas-extremos-de-la-tierra', 'Los lugares más extremos de la Tierra', 'El más caliente, el más frío, el más seco, el más alto y el más profundo: un viaje por los récords del planeta.', 5),
     ('the-most-extreme-places-on-earth', 'The most extreme places on Earth', 'The hottest, the coldest, the driest, the highest and the deepest: a journey through the planet’s records.', 5)),
   'darwin': A(F1, 'img/tierra/darwin.jpg',
     ('darwin-y-el-origen-de-las-especies', 'Darwin y «El origen de las especies»', 'El 24 de noviembre de 1859 salió a la venta el libro que cambió nuestra forma de entender la vida.', 5),
     ('darwin-and-on-the-origin-of-species', 'Darwin and «On the Origin of Species»', 'On 24 November 1859 the book that changed the way we understand life went on sale.', 5)),
   'nubes': A(F2, 'img/tierra/nubes.jpg',
     ('como-reconocer-las-nubes', 'Cómo reconocer las nubes y saber qué tiempo hará', 'Cúmulos, estratos, cirros y cumulonimbos: una guía sencilla para leer el cielo.', 5),
     ('how-to-identify-clouds', 'How to identify clouds and tell what the weather will do', 'Cumulus, stratus, cirrus and cumulonimbus: a simple guide to reading the sky.', 5)),
   'geminidas': A(F3, 'img/universo/perseidas.jpg',
     ('geminidas-la-mejor-lluvia-de-estrellas-del-ano', 'Gemínidas, la mejor lluvia de estrellas del año', 'La noche del 13 al 14 de diciembre llegan las estrellas fugaces más abundantes. Cuándo y cómo verlas.', 5),
     ('geminids-the-best-meteor-shower-of-the-year', 'The Geminids, the best meteor shower of the year', 'On the night of 13 to 14 December the most abundant shooting stars arrive. When and how to see them.', 5)),
   'lapalma': A(F4, 'img/tierra/tajogaite.jpg',
     ('la-palma-cinco-anos-despues-del-volcan', 'La Palma, cinco años después del volcán', 'El 13 de diciembre de 2021 terminó la erupción del Tajogaite tras 85 días. Lo que nos enseñó.', 5),
     ('la-palma-five-years-after-the-volcano', 'La Palma, five years after the volcano', 'On 13 December 2021 the Tajogaite eruption ended after 85 days. What it taught us.', 5)),
   'solsticio': A(F5, 'img/universo/tierra.jpg',
     ('el-solsticio-de-invierno', 'El solsticio de invierno, el día más corto del año', 'El 21 de diciembre empieza el invierno astronómico. Por qué ocurre y por qué no es el día más frío.', 5),
     ('the-winter-solstice', 'The winter solstice, the shortest day of the year', 'Astronomical winter begins on 21 December. Why it happens and why it is not the coldest day.', 5)),
   'apolo8': A(F6, 'img/universo/salida_tierra.jpg',
     ('apolo-8-la-nochebuena-que-vimos-la-tierra-desde-la-luna', 'Apolo 8: la Nochebuena en que vimos la Tierra desde la Luna', 'En 1968 tres astronautas dieron diez vueltas a la Luna y tomaron la foto «Salida de la Tierra».', 5),
     ('apollo-8-the-christmas-eve-we-saw-earth-from-the-moon', 'Apollo 8: the Christmas Eve we saw Earth from the Moon', 'In 1968 three astronauts orbited the Moon ten times and took the «Earthrise» photograph.', 5)),
   'perihelio': A(F7, 'img/universo/sol.jpg',
     ('el-perihelio-en-enero-estamos-mas-cerca-del-sol', 'El perihelio: en enero estamos más cerca del Sol', 'A principios de enero la Tierra pasa por el punto de su órbita más cercano al Sol. Entonces, ¿por qué hace frío?', 5),
     ('perihelion-in-january-we-are-closest-to-the-sun', 'Perihelion: in January we are closest to the Sun', 'In early January the Earth passes the point of its orbit nearest the Sun. So why is it cold?', 5)),
   'antartida': A(F8, 'img/tierra/pinguinos.jpg',
     ('antartida-el-continente-helado', 'La Antártida, el continente helado', 'El lugar más frío, seco y ventoso del planeta guarda casi toda el agua dulce de la Tierra.', 5),
     ('antarctica-the-frozen-continent', 'Antarctica, the frozen continent', 'The coldest, driest and windiest place on the planet holds almost all of the Earth’s fresh water.', 5)),
  },
 },
 'escolapedia': {
  'nombre': 'Escolapedia', 'dominio': 'escolapedia.com', 'autor': 'Alejandro Rosàs',
  'idiomas': ['es'], 'no_tocar_web': True, 'raiz_fisica': 'dist',
  'envoltura': ('<div class="wrap">', '</div>'),
  'clase_fig': 'blog-fig', 'clase_miga': 'crumbs',
  'pref': {'u': ''},
  'css': css('var(--pen)', 'var(--muted)', 'var(--ink)', 'var(--card)', 'var(--line)', 'var(--line)'),
  'head': ES['head'], 'cab': ES['cab'], 'pie': ES['pie'],
  'indice': {'es': ('El blog de Escolapedia', 'Ideas para estudiar mejor, acompañar a los hijos en el colegio y aprender en familia. Un artículo nuevo cada martes.')},
  'articulos': {
   'infancia': E(F0, U('photo-1516890896652-41ca1a35787c'),
     ('dia-del-nino-y-derechos-de-la-infancia', 'Día del Niño: los derechos de la infancia explicados', 'Cada 20 de noviembre se celebra la Convención sobre los Derechos del Niño. Qué dice y cómo hablar de ella en casa y en clase.', 5)),
   'tecnicas': E(F0, U('photo-1598981457915-aea220950616'),
     ('tecnicas-de-estudio-que-funcionan', 'Técnicas de estudio que funcionan (y las que no)', 'Releer y subrayar da sensación de saber, pero rinde poco. Lo que dice la investigación sobre cómo se aprende de verdad.', 6)),
   'deberes': E(F0, U('photo-1629360057380-18b15b42e650'),
     ('como-ayudar-con-los-deberes-sin-hacerlos', 'Cómo ayudar con los deberes sin hacerlos', 'Acompañar sí, resolver no. Claves para que los deberes sirvan para aprender y no acaben en discusión.', 5)),
   'esquema': E(F1, U('photo-1510936994138-07e06c7c5add'),
     ('como-hacer-un-buen-esquema', 'Cómo hacer un buen esquema paso a paso', 'Un esquema no es copiar el libro en pequeño. Cómo elegir las ideas clave y ordenarlas para estudiar mejor.', 5)),
   'leer': E(F2, U('photo-1553729784-e91953dec042'),
     ('ideas-para-animar-a-leer-en-casa', 'Diez ideas para animar a leer en casa', 'El gusto por la lectura no se impone, se contagia. Propuestas sencillas para cada edad.', 5)),
   'examenes': E(F3, U('photo-1757193714692-44cdf07a5377'),
     ('preparar-los-examenes-de-la-primera-evaluacion', 'Cómo preparar los exámenes de la primera evaluación', 'Llegan las semanas de exámenes antes de Navidad. Un plan de siete días, sin noches en vela.', 5)),
   'notas': E(F4, U('photo-1560785496-321917f24016'),
     ('las-notas-de-la-primera-evaluacion-que-hacer', 'Las notas de la primera evaluación: qué hacer con ellas', 'Buenas o malas, las notas son información. Cómo hablar de ellas en casa y preparar el segundo trimestre.', 5)),
   'jugando': E(F5, U('photo-1577897113292-3b95936e5206'),
     ('aprender-jugando-en-vacaciones-de-navidad', 'Aprender jugando en las vacaciones de Navidad', 'Juegos de mesa, de palabras y de números para seguir aprendiendo sin que parezcan deberes.', 5)),
   'cocina': E(F6, U('photo-1605433246995-23f532d1e001'),
     ('matematicas-en-la-cocina', 'Matemáticas en la cocina', 'Pesar, medir, repartir y calcular tiempos: una receta es un problema de matemáticas que se puede comer.', 5)),
   'reyes': E(F7, U('photo-1608755727748-dfa2e44f255b'),
     ('regalos-de-reyes-que-ayudan-a-aprender', 'Regalos de Reyes que ayudan a aprender', 'Libros, juegos, construcciones y experimentos: ideas por edades para regalar algo que dure más que un día.', 5)),
   'rutina': E(F8, U('photo-1594608661623-aa0bd3a69d98'),
     ('volver-a-la-rutina-despues-de-navidad', 'Volver a la rutina después de Navidad', 'Horarios, sueño, mochila y estudio: cómo recuperar el ritmo del colegio sin agobios.', 5)),
  },
 },
}
