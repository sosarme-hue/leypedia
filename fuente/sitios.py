# Configuración de los dos blogs: plantillas copiadas de las páginas reales de cada web (noviembre de 2026).
CSS = """.blog-art{max-width:760px;margin:0 auto}
.blog-art h1{margin:.3em 0 .1em;line-height:1.15}
.blog-meta{color:#6d625a;font-size:.92em;margin:.3em 0 1.1em}
.blog-entradilla{font-size:1.16em;line-height:1.55;color:#3b322c;border-left:4px solid VAR;padding:2px 0 2px 14px;margin:0 0 1.4em}
.blog-texto p{line-height:1.72;font-size:1.06em}
.blog-texto h2{margin:1.6em 0 .4em;line-height:1.2}
.blog-texto a{color:VAR}
.blog-fig{margin:1.6em 0;text-align:center}
.blog-fig img{max-width:100%;max-height:560px;height:auto;border-radius:6px;box-shadow:0 2px 10px #0002}
.blog-fig figcaption{font-size:.88em;color:#6d625a;margin-top:8px;line-height:1.4}
.blog-cab{text-align:center;margin:14px auto 26px;max-width:720px}
.blog-cab h1{margin:.2em 0}
.blog-cab p{font-size:1.1em;color:#4a4039}
.blog-lista{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;margin:14px 0}
.blog-card{display:flex;flex-direction:column;gap:6px;background:#fff;border:1px solid #e5dccb;border-radius:10px;overflow:hidden;text-decoration:none;color:#3b322c;padding-bottom:14px;transition:box-shadow .2s}
.blog-card:hover{box-shadow:0 4px 14px #0002}
.blog-card img{width:100%;height:180px;object-fit:cover;background:#eee}
.blog-card b,.blog-card span{padding:0 14px}
.blog-card b{font-size:1.14em;color:VAR;line-height:1.25}
.blog-card span{font-size:.94em;line-height:1.45}
.blog-card .blog-fecha{font-size:.78em;text-transform:uppercase;letter-spacing:.06em;color:#8a7d70;margin-top:6px}
.blog-portada{max-width:1100px;margin:0 auto 30px}
.blog-mas{max-width:1100px;margin:44px auto 10px;border-top:1px solid #e5dccb;padding-top:10px}
.blog-todos{font-weight:600;color:VAR}
.compartir a{margin-left:8px}
@media(max-width:600px){.blog-texto p{font-size:1em}.blog-card img{height:150px}}"""

PINA_SVG = '<svg class="logo" viewBox="0 0 52 52" aria-hidden="true"><path d="M26 4C12 4 3 13 3 25c0 11 8 19 17 19 4 0 5-3 4-6s1-6 5-6h7c8 0 13-5 13-12C49 11 39 4 26 4z" fill="#f3e9d8"/><circle cx="14" cy="22" r="3.5" fill="#8c2f2b"/><circle cx="22" cy="13" r="3.5" fill="#e3b04b"/><circle cx="33" cy="13" r="3.5" fill="#3d6a8a"/><circle cx="40" cy="22" r="3.5" fill="#b07a2a"/></svg>'
CULI_SVG = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="46" height="46" aria-hidden="true"><path d="M15 33h34C49 46 42 54 32 54S15 46 15 33Z" fill="#f6f0e4"/><rect x="11" y="28" width="42" height="5" rx="2.5" fill="#f6f0e4"/><path d="M15 36C10 36 9 41 13 42M49 36C54 36 55 41 51 42" stroke="#f6f0e4" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M24 24C20 20 28 16 24 12C21 9 26 6 24 4" stroke="#f6f0e4" stroke-width="2.2" fill="none" stroke-linecap="round"/><path d="M32 24C28 20 36 16 32 12C29 9 34 6 32 4" stroke="#f6f0e4" stroke-width="2.2" fill="none" stroke-linecap="round"/><path d="M40 24C36 20 44 16 40 12C37 9 42 6 40 4" stroke="#f6f0e4" stroke-width="2.2" fill="none" stroke-linecap="round"/><path d="M22 42Q32 37 42 42" stroke="#b5c27a" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'

F0, F1, F2, F3, F4, F5, F6, F7, F8 = '2026-11-19', '2026-11-24', '2026-12-01', '2026-12-08', '2026-12-15', '2026-12-22', '2026-12-29', '2027-01-05', '2027-01-12'

SITIOS = {
 'pinacopedia': {
  'nombre': 'Pinacopedia', 'dominio': 'pinacopedia.com', 'autor': 'Alejandro Rosàs',
  'js_menu': 'assets/busca.js', 'clase_fig': 'blog-fig', 'clase_miga': 'miga',
  'css': CSS.replace('VAR', '#8c2f2b'),
  'head': '<link rel="stylesheet" href="{I}assets/fuentes.css">\n<link rel="stylesheet" href="{I}assets/estilo.css">\n<link rel="icon" href="{I}assets/favicon.svg" type="image/svg+xml">',
  'cab': {
   'es': '<header class="cab">\n<a class="marca" href="{R}index.html">' + PINA_SVG + 'Pinacopedia</a>\n<nav class="menu"><a href="{R}explorar.html">Explorar</a><a href="{R}pintores.html">Pintores</a><a href="{R}obras.html">Obras</a><a href="{R}museos.html">Museos</a><a href="{R}index.html#periodos">Periodos</a><a href="{R}maestros.html">Maestros y alumnos</a><a href="{R}curiosidades.html">Curiosidades</a><a class="menu-blog" href="./">Blog</a></nav>\n<span class="redes-cab"></span>\n<span class="idioma"><a href="{ALT}" hreflang="en">English</a></span>\n<form class="busca-mini" action="{R}explorar.html" data-raiz="{R}" data-ra="{I}"><input name="q" type="search" placeholder="Buscar pintor, obra o museo" aria-label="Buscar"></form>\n</header>',
   'en': '<header class="cab">\n<a class="marca" href="{R}index.html">' + PINA_SVG + 'Pinacopedia</a>\n<nav class="menu"><a href="{R}explorar.html">Explore</a><a href="{R}pintores.html">Painters</a><a href="{R}obras.html">Works</a><a href="{R}museos.html">Museums</a><a href="{R}index.html#periodos">Periods</a><a href="{R}maestros.html">Teachers and pupils</a><a href="{R}curiosidades.html">Curiosities</a><a class="menu-blog" href="./">Blog</a></nav>\n<span class="redes-cab"></span>\n<span class="idioma"><a href="{ALT}" hreflang="es">Español</a></span>\n<form class="busca-mini" action="{R}explorar.html" data-raiz="{R}" data-ra="{I}"><input name="q" type="search" placeholder="Search a painter, work or museum" aria-label="Search"></form>\n</header>',
  },
  'pie': {
   'es': '<footer class="pie">\n<p>Pinacopedia, la historia de la pintura en español e inglés. Textos originales; imágenes de obras en dominio público procedentes de Wikimedia Commons.</p>\n<p><a href="{R}sobre.html">Sobre Pinacopedia</a></p>\n<p><a href="{R}aviso-legal.html">Aviso legal</a> · <a href="{R}privacidad.html">Privacidad</a> · <a href="{R}cookies.html">Cookies</a></p><p>© 2026 Alejandro Rosàs · Contenido bajo licencia <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.es" rel="license noopener" style="display:inline">CC BY-NC 4.0</a>, salvo indicación en contrario</p>\n</footer>\n<script src="{I}assets/busca.js"></script>',
   'en': '<footer class="pie">\n<p>Pinacopedia, the history of painting in English and Spanish. Original texts; images of public-domain works from Wikimedia Commons.</p>\n<p><a href="{R}sobre.html">About Pinacopedia</a></p>\n<p><a href="{R}aviso-legal.html">Legal notice</a> · <a href="{R}privacidad.html">Privacy</a> · <a href="{R}cookies.html">Cookies</a></p><p>© 2026 Alejandro Rosàs · Content licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.en" rel="license noopener" style="display:inline">CC BY-NC 4.0</a>, unless otherwise noted</p>\n</footer>\n<script src="{I}assets/busca.js"></script>',
  },
  'indice': {'es': ('El blog de Pinacopedia', 'Historias, cuadros explicados y consejos para disfrutar de la pintura. Un artículo nuevo cada martes.'),
             'en': ('The Pinacopedia blog', 'Stories, paintings explained and tips for enjoying art. A new post every Tuesday.')},
  'articulos': {
   'magos': {'fecha': F0, 'img': 'img/g/Q488825.jpg',
     'es': ('la-adoracion-de-los-magos-en-ocho-cuadros', 'La Adoración de los Magos en ocho cuadros', 'De Giotto a Velázquez: cómo pintaron los grandes maestros la llegada de los Reyes Magos, y qué secretos esconde cada versión.', 7),
     'en': ('the-adoration-of-the-magi-in-eight-paintings', 'The Adoration of the Magi in eight paintings', 'From Giotto to Velázquez: how the great masters painted the arrival of the Magi, and the secrets hidden in each version.', 7)},
   'nieve': {'fecha': F0, 'img': 'img/m/Q500985.jpg',
     'es': ('paisajes-de-invierno-los-cuadros-de-nieve-mas-famosos', 'Paisajes de invierno: los cuadros de nieve más famosos', 'De Los cazadores en la nieve de Brueghel a La urraca de Monet: así entró el invierno en la historia de la pintura.', 6),
     'en': ('winter-landscapes-the-most-famous-snow-paintings', 'Winter landscapes: the most famous snow paintings', "From Bruegel's Hunters in the Snow to Monet's Magpie: how winter found its way into the history of painting.", 6)},
   'mirar': {'fecha': F0, 'img': 'img/g/Q208758.jpg',
     'es': ('como-mirar-un-cuadro-en-diez-minutos', 'Cómo mirar un cuadro en diez minutos', 'Un método sencillo para disfrutar de cualquier pintura en un museo, paso a paso y con Las Meninas como ejemplo.', 6),
     'en': ('how-to-look-at-a-painting-in-ten-minutes', 'How to look at a painting in ten minutes', 'A simple method for enjoying any painting in a museum, step by step, with Las Meninas as an example.', 6)},
   'vermeer': {'fecha': F1, 'img': 'img/m/Q185372.jpg',
     'es': ('la-joven-de-la-perla-el-misterio-de-vermeer', 'La joven de la perla: el misterio de Vermeer', 'Quién era la muchacha, si la perla era de verdad y por qué este pequeño cuadro de Delft fascina tanto.', 6),
     'en': ('girl-with-a-pearl-earring-vermeers-mystery', "Girl with a Pearl Earring: Vermeer's mystery", 'Who the girl was, whether the pearl was real, and why this small painting from Delft is so fascinating.', 6)},
   'bosco': {'fecha': F2, 'img': 'img/r/Q130531.jpg',
     'es': ('el-jardin-de-las-delicias-guia-para-perderse', 'El jardín de las delicias: guía para perderse en El Bosco', 'Cómo recorrer el tríptico más enigmático del Prado, panel a panel, sin perderse ningún detalle.', 7),
     'en': ('the-garden-of-earthly-delights-a-guide', 'The Garden of Earthly Delights: a guide to getting lost in Bosch', "How to explore the Prado's most enigmatic triptych, panel by panel, without missing a detail.", 7)},
   'proverbios': {'fecha': F3, 'img': 'img/m/Q533619.jpg',
     'es': ('los-proverbios-flamencos-refranes-en-un-cuadro', 'Los proverbios flamencos: cien refranes en un cuadro', 'Brueghel pintó más de cien dichos populares en una sola escena. Te enseñamos a encontrarlos.', 6),
     'en': ('netherlandish-proverbs-a-hundred-sayings-in-one-painting', 'Netherlandish Proverbs: a hundred sayings in one painting', 'Bruegel painted more than a hundred popular sayings in a single scene. Here is how to find them.', 6)},
   'noche': {'fecha': F4, 'img': 'img/m/Q45585.jpg',
     'es': ('la-noche-estrellada-de-van-gogh', 'La noche estrellada: lo que Van Gogh veía desde su ventana', 'La historia del cuadro más reproducido del mundo, pintado desde un asilo en Saint-Rémy.', 6),
     'en': ('the-starry-night-by-van-gogh', 'The Starry Night: what Van Gogh saw from his window', "The story of the world's most reproduced painting, made in an asylum in Saint-Rémy.", 6)},
   'fiestas': {'fecha': F5, 'img': 'img/m/Q603751.jpg',
     'es': ('banquetes-y-fiestas-en-la-pintura', 'Banquetes y fiestas en la historia de la pintura', 'De la boda campesina de Brueghel a los bailes de Renoir: cómo pintaron los maestros las grandes celebraciones.', 6),
     'en': ('feasts-and-parties-in-painting', 'Feasts and parties in the history of painting', "From Bruegel's peasant wedding to Renoir's dances: how the masters painted great celebrations.", 6)},
   'juegos': {'fecha': F6, 'img': 'img/m/Q697332.jpg',
     'es': ('juego-de-ninos-de-brueghel', 'Juego de niños: los juegos de hace 500 años según Brueghel', 'Más de ochenta juegos infantiles en un solo cuadro. ¿Cuántos siguen vivos hoy?', 6),
     'en': ('childrens-games-by-bruegel', "Children's Games: how children played 500 years ago, according to Bruegel", 'More than eighty children’s games in a single painting. How many are still played today?', 6)},
   'gioconda': {'fecha': F7, 'img': 'img/m/Q12418.jpg',
     'es': ('diez-curiosidades-sobre-la-gioconda', 'Diez curiosidades sobre La Gioconda', 'El robo de 1911, la copia del Prado, las cejas que faltan: lo que quizá no sabías del cuadro más famoso del mundo.', 6),
     'en': ('ten-curious-facts-about-the-mona-lisa', 'Ten curious facts about the Mona Lisa', "The 1911 theft, the Prado copy, the missing eyebrows: what you may not know about the world's most famous painting.", 6)},
   'libertad': {'fecha': F8, 'img': 'img/m/Q29530.jpg',
     'es': ('la-libertad-guiando-al-pueblo-de-delacroix', 'La Libertad guiando al pueblo: historia de un símbolo', 'Cómo un cuadro sobre tres días de revolución en París se convirtió en el emblema de Francia.', 6),
     'en': ('liberty-leading-the-people-by-delacroix', 'Liberty Leading the People: the story of a symbol', 'How a painting about three days of revolution in Paris became the emblem of France.', 6)},
  },
 },
 'culinapedia': {
  'nombre': 'Culinapedia', 'dominio': 'culinapedia.com', 'autor': 'Alejandro Rosàs',
  'js_menu': 'assets/familia.js', 'clase_fig': 'blog-fig', 'clase_miga': 'migas',
  'css': CSS.replace('VAR', '#7a1f2b'),
  'head': '<link rel="icon" href="{I}assets/icono.svg"><link rel="stylesheet" href="{I}assets/estilo.css?v=7">',
  'cab': {
   'es': '<header class="cab"><div class="in"><a class="marca" href="{R}index.html">' + CULI_SVG + '<span>CULINAPEDIA<small>La enciclopedia de la gastronomía y la cultura alimentaria</small></span></a>\n<nav class="menu"><a href="{R}platos.html">Platos</a><a href="{R}cocinas.html">Cocinas</a><a href="{R}vinos.html">Vinos</a><a href="{R}epocas.html">Épocas</a><a href="{R}personas.html">Personas</a><a href="{R}restaurantes.html">Restaurantes</a><a href="{R}libros.html">Libros</a><a href="{R}dietas.html">Dietas</a><a href="{R}salud.html">Salud</a><a href="{R}calculadora.html">Calorías</a><a class="menu-blog" href="./">Blog</a></nav>\n<div class="idioma" role="group" aria-label="Idioma"><span class="act" lang="es">Español</span><a href="{ALT}" hreflang="en" lang="en">English</a></div></div></header>',
   'en': '<header class="cab"><div class="in"><a class="marca" href="{R}index.html">' + CULI_SVG + '<span>CULINAPEDIA<small>The Encyclopedia of Food and Culinary Culture</small></span></a>\n<nav class="menu"><a href="{R}platos.html">Dishes</a><a href="{R}cocinas.html">Cuisines</a><a href="{R}vinos.html">Wine</a><a href="{R}epocas.html">Eras</a><a href="{R}personas.html">People</a><a href="{R}restaurantes.html">Restaurants</a><a href="{R}libros.html">Books</a><a href="{R}dietas.html">Diets</a><a href="{R}salud.html">Health</a><a href="{R}calculadora.html">Calories</a><a class="menu-blog" href="./">Blog</a></nav>\n<div class="idioma" role="group" aria-label="Language"><a href="{ALT}" hreflang="es" lang="es">Español</a><span class="act" lang="en">English</span></div></div></header>',
  },
  'pie': {
   'es': '<footer class="pie"><p>Culinapedia, la enciclopedia de la gastronomía y la cultura alimentaria, en castellano e inglés. Textos originales a partir de Wikipedia y Wikidata.</p><p>Fotos libres de Wikimedia Commons con su licencia indicada.</p><p><a href="{R}sobre.html">Sobre Culinapedia</a> · <a href="{R}aviso-legal.html">Aviso legal</a> · <a href="{R}privacidad.html">Privacidad</a> · <a href="{R}cookies.html">Cookies</a> · info@culinapedia.com</p><p>© 2026 Alejandro Rosàs · Contenido bajo licencia <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.es" rel="license noopener" style="display:inline">CC BY-NC 4.0</a>, salvo indicación en contrario</p></footer>\n<script src="{I}assets/buscador.js?v=3" defer></script><script src="{I}assets/familia.js" defer></script>',
   'en': '<footer class="pie"><p>Culinapedia, the encyclopedia of food and culinary culture, in English and Spanish. Original texts based on Wikipedia and Wikidata.</p><p>Free photos from Wikimedia Commons under their stated licences.</p><p><a href="{R}sobre.html">About Culinapedia</a> · <a href="{R}aviso-legal.html">Legal notice</a> · <a href="{R}privacidad.html">Privacy</a> · <a href="{R}cookies.html">Cookies</a> · info@culinapedia.com</p><p>© 2026 Alejandro Rosàs · Content licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/deed.en" rel="license noopener" style="display:inline">CC BY-NC 4.0</a>, unless otherwise noted</p></footer>\n<script src="{I}assets/buscador.js?v=3" defer></script><script src="{I}assets/familia.js" defer></script>',
  },
  'indice': {'es': ('El blog de Culinapedia', 'Historias de platos, tradiciones de la mesa y curiosidades gastronómicas. Un artículo nuevo cada martes.'),
             'en': ('The Culinapedia blog', 'Stories of dishes, table traditions and food curiosities. A new post every Tuesday.')},
  'articulos': {
   'turron': {'fecha': F0, 'img': 'img/p/Q159304.webp',
     'es': ('historia-del-turron', 'Historia del turrón: de al-Ándalus a Jijona', 'De dónde viene el dulce más navideño de España, en qué se diferencian el duro y el blando y cómo se come en otros países.', 6),
     'en': ('the-history-of-turron', 'The history of turrón: from al-Andalus to Jijona', "Where Spain's most Christmassy sweet comes from, how hard and soft turrón differ, and how it is eaten in other countries.", 6)},
   'menus': {'fecha': F0, 'img': 'img/p/Q854342.webp',
     'es': ('la-mesa-de-navidad-en-diez-paises', 'La mesa de Navidad en diez países', 'De la Nochebuena española al pollo frito de Japón: qué se come en Navidad en diez países del mundo.', 6),
     'en': ('the-christmas-table-in-ten-countries', 'The Christmas table in ten countries', 'From Spanish Christmas Eve to fried chicken in Japan: what people eat at Christmas in ten countries around the world.', 6)},
   'roscon': {'fecha': F0, 'img': 'blog/img/roscon-de-reyes.webp',
     'es': ('el-roscon-de-reyes-origen-y-tradicion', 'El roscón de Reyes: origen, tradición y cómo elegirlo', 'La historia del último dulce de las fiestas, el sentido de la figurita y el haba, y cómo reconocer un buen roscón.', 5),
     'en': ('the-roscon-de-reyes-origins-and-tradition', 'The roscón de Reyes: origins, tradition and how to choose one', "The story of the holidays' last sweet, the meaning of the figurine and the bean, and how to spot a good roscón.", 5)},
   'churros': {'fecha': F1, 'img': 'img/p/Q727605.webp',
     'es': ('churros-con-chocolate-historia', 'Churros con chocolate: historia de un clásico', 'De dónde vienen los churros, desde cuándo se mojan en chocolate y cómo se llaman en cada rincón de España.', 5),
     'en': ('churros-and-chocolate-history', 'Churros and chocolate: the story of a classic', 'Where churros come from, since when they have been dipped in chocolate, and what they are called around Spain.', 5)},
   'mazapan': {'fecha': F2, 'img': 'img/p/Q106252.webp',
     'es': ('el-mazapan-de-toledo-a-lubeck', 'El mazapán: de Toledo a Lübeck', 'Almendra y azúcar: la historia de un dulce que ha viajado por media Europa y América.', 5),
     'en': ('marzipan-from-toledo-to-lubeck', 'Marzipan: from Toledo to Lübeck', 'Almonds and sugar: the story of a sweet that has travelled across Europe and the Americas.', 5)},
   'dulceseuropa': {'fecha': F3, 'img': 'img/g/Q106252-1.webp',
     'es': ('dulces-navidenos-de-europa', 'Dulces navideños de Europa: un viaje por diez países', 'Stollen, panettone, bûche de Noël, christmas pudding, melomakarona: los dulces de Navidad del continente.', 6),
     'en': ('christmas-sweets-of-europe', 'Christmas sweets of Europe: a trip through ten countries', "Stollen, panettone, bûche de Noël, Christmas pudding, melomakarona: the continent's Christmas sweets.", 6)},
   'pandulce': {'fecha': F4, 'img': 'img/g/Q854342-3.webp',
     'es': ('panettone-y-pan-dulce-de-milan-a-lima', 'Panettone y pan dulce: de Milán a Buenos Aires y Lima', 'Cómo el «pan grande» de Milán se convirtió en el dulce de Navidad de media Sudamérica.', 5),
     'en': ('panettone-and-pan-dulce-from-milan-to-lima', 'Panettone and pan dulce: from Milan to Buenos Aires and Lima', "How Milan's «big bread» became the Christmas sweet of half of South America.", 5)},
   'sobras': {'fecha': F5, 'img': 'img/p/Q70125.webp',
     'es': ('cocina-de-aprovechamiento-las-sobras-de-navidad', 'Cocina de aprovechamiento: qué hacer con las sobras de Navidad', 'Croquetas, canelones de San Esteban, ropa vieja y otras recetas tradicionales para no tirar nada.', 5),
     'en': ('leftover-cooking-christmas-leftovers', 'Leftover cooking: what to do with Christmas leftovers', "Croquettes, Saint Stephen's cannelloni, ropa vieja and other traditional recipes so nothing goes to waste.", 5)},
   'uvas': {'fecha': F6, 'img': 'img/p/Q10978.webp',
     'es': ('las-doce-uvas-de-nochevieja', 'Las doce uvas de Nochevieja: origen y trucos', 'De dónde viene la tradición de las uvas de la suerte y cómo comerlas sin atragantarse.', 5),
     'en': ('the-twelve-grapes-of-new-years-eve', "The twelve grapes of New Year's Eve: origins and tips", 'Where the lucky grapes tradition comes from and how to eat them without choking.', 5)},
   'reyes': {'fecha': F7, 'img': 'img/g/Q177166-2.webp',
     'es': ('dulces-de-reyes-en-el-mundo', 'Dulces de Reyes en el mundo', 'Roscón, casca, galette des rois, rosca mexicana y king cake: qué se come el 6 de enero.', 5),
     'en': ('epiphany-sweets-around-the-world', 'Epiphany sweets around the world', 'Roscón, casca, galette des rois, Mexican rosca and king cake: what people eat on 6 January.', 5)},
   'cocido': {'fecha': F8, 'img': 'img/p/Q1105215.webp',
     'es': ('el-cocido-madrileno-y-sus-primos', 'El cocido madrileño y sus primos de toda España', 'Historia del plato de cuchara más completo y de sus versiones: escudella, cocido montañés, maragato y más.', 6),
     'en': ('cocido-madrileno-and-its-cousins', 'Cocido madrileño and its cousins across Spain', 'The history of the heartiest spoon dish and its versions: escudella, cocido montañés, maragato and more.', 6)},
  },
 },
}

from sitios_tn import TN  # noqa: E402  Tenispedia y Newtonpedia
SITIOS.update(TN)
from sitios_cm import CM  # noqa: E402  Cinematopedia y Medicapedia
SITIOS.update(CM)
from sitios_fe import FE; SITIOS.update(FE)
from sitios_ep import EP; SITIOS.update(EP)
