# Tenispedia y Newtonpedia (noviembre de 2026). Se añade a SITIOS desde sitios.py.
from sitios import F0, F1, F2, F3, F4, F5, F6, F7, F8
from plantillas_tn import PLANT

def css(acc, suave, texto, tarj, linea, fondo_img):
    return f""".blog-art{{max-width:760px;margin:0 auto}}
.blog-art h1{{margin:.3em 0 .1em;line-height:1.15}}
.blog-meta{{color:{suave};font-size:.92em;margin:.3em 0 1.1em}}
.blog-entradilla{{font-size:1.16em;line-height:1.55;color:{texto};border-left:4px solid {acc};padding:2px 0 2px 14px;margin:0 0 1.4em}}
.blog-texto p{{line-height:1.72;font-size:1.06em;max-width:none}}
.blog-texto h2{{margin:1.6em 0 .4em;line-height:1.2}}
.blog-texto a{{color:{acc}}}
.blog-fig{{margin:1.6em 0;text-align:center}}
.blog-fig img{{max-width:100%;max-height:560px;height:auto;border-radius:6px;box-shadow:0 2px 10px #0002;background:{fondo_img}}}
.blog-fig figcaption{{font-size:.88em;color:{suave};margin-top:8px;line-height:1.4}}
.blog-cab{{text-align:center;margin:14px auto 26px;max-width:720px}}
.blog-cab h1{{margin:.2em 0}}
.blog-cab p{{font-size:1.1em;color:{suave}}}
.blog-lista{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;margin:14px 0}}
.blog-card{{display:flex;flex-direction:column;gap:6px;background:{tarj};border:1px solid {linea};border-radius:10px;overflow:hidden;text-decoration:none;color:{texto};padding-bottom:14px;transition:box-shadow .2s}}
.blog-card:hover{{box-shadow:0 4px 14px #0002;text-decoration:none}}
.blog-card img{{width:100%;height:180px;object-fit:cover;object-position:top;background:{fondo_img}}}
.blog-card b,.blog-card span{{padding:0 14px}}
.blog-card b{{font-size:1.14em;color:{acc};line-height:1.25}}
.blog-card span{{font-size:.94em;line-height:1.45}}
.blog-card .blog-fecha{{font-size:.78em;text-transform:uppercase;letter-spacing:.06em;color:{suave};margin-top:6px}}
.blog-portada{{max-width:1100px;margin:0 auto 30px}}
.blog-mas{{max-width:1100px;margin:44px auto 10px;border-top:1px solid {linea};padding-top:10px}}
.blog-todos{{font-weight:600;color:{acc}}}
.compartir a{{margin-left:8px;color:{acc}}}
@media(max-width:600px){{.blog-texto p{{font-size:1em}}.blog-card img{{height:150px}}}}"""

TP, NP = PLANT['tenispedia'], PLANT['newtonpedia']

def A(f, img, es, en):
    return {'fecha': f, 'img': img, 'es': es, 'en': en}

TN = {
 'tenispedia': {
  'nombre': 'Tenispedia', 'dominio': 'tenispedia.com', 'autor': 'Alejandro Rosàs',
  'js_menu': 'assets/tenis.js', 'clase_fig': 'blog-fig', 'clase_miga': 'miga',
  'pref': {'t': 't/', 'r': 'r/', 'k': 'torneo/', 'e': 'e/', 'p': 'p/'},
  'data_raiz': {'es': '../', 'en': '../../en/'},
  'css': css('var(--verde2)', 'var(--suave)', 'var(--texto)', 'var(--fondo)', 'var(--linea)', 'var(--papel)'),
  'head': TP['head'], 'cab': TP['cab'], 'pie': TP['pie'],
  'indice': {'es': ('El blog de Tenispedia', 'Historias de tenistas, partidos legendarios y curiosidades de la historia del tenis. Un artículo nuevo cada martes.'),
             'en': ('The Tenispedia blog', 'Stories of players, legendary matches and curiosities from tennis history. A new post every Tuesday.')},
  'articulos': {
   'davis': A(F0, 'img/a/torneo-davis-cup.webp',
     ('historia-de-la-copa-davis', 'La Copa Davis: historia de la Ensaladera', 'Cómo una apuesta de unos estudiantes de Harvard en 1900 se convirtió en la gran competición de selecciones del tenis.', 6),
     ('the-history-of-the-davis-cup', 'The Davis Cup: the story of the Salad Bowl', 'How a challenge between Harvard students in 1900 became the great team competition of tennis.', 6)),
   'borgmcenroe': A(F0, 'img/r/Q104506.webp',
     ('borg-contra-mcenroe-hielo-y-fuego', 'Borg contra McEnroe: el hielo y el fuego', 'La rivalidad más corta y más intensa de la historia del tenis, de la final de Wimbledon de 1980 a la retirada del sueco.', 6),
     ('borg-v-mcenroe-ice-and-fire', 'Borg v McEnroe: ice and fire', "The shortest and most intense rivalry in tennis history, from the 1980 Wimbledon final to the Swede's retirement.", 6)),
   'lenglen': A(F0, 'img/r/Q232831.webp',
     ('suzanne-lenglen-y-el-partido-del-siglo', 'Suzanne Lenglen y el partido del siglo', 'La primera gran estrella del tenis femenino y su único duelo con Helen Wills, en Cannes en 1926.', 6),
     ('suzanne-lenglen-and-the-match-of-the-century', 'Suzanne Lenglen and the match of the century', "Women's tennis's first great star and her only meeting with Helen Wills, in Cannes in 1926.", 6)),
   'laver': A(F1, 'img/r/Q105550.webp',
     ('rod-laver-y-el-grand-slam-de-1969', 'Rod Laver y el Grand Slam de 1969', 'El único hombre que ha ganado dos veces los cuatro grandes en un mismo año.', 5),
     ('rod-laver-and-the-1969-grand-slam', 'Rod Laver and the 1969 Grand Slam', 'The only man to win all four majors in the same year twice.', 5)),
   'gibson': A(F2, 'img/r/Q53550.webp',
     ('althea-gibson-la-pionera', 'Althea Gibson, la pionera', 'La primera tenista negra que ganó Roland Garros, Wimbledon y el US Open, en los años cincuenta.', 5),
     ('althea-gibson-the-pioneer', 'Althea Gibson, the pioneer', 'The first Black player to win the French Championships, Wimbledon and the US Championships, in the 1950s.', 5)),
   'origenes': A(F3, 'img/r/Q725054.webp',
     ('del-juego-de-pelota-a-wimbledon-1877', 'Del juego de pelota a Wimbledon 1877: así nació el tenis', 'Del jeu de paume de los monasterios franceses al primer torneo de Wimbledon.', 6),
     ('from-real-tennis-to-wimbledon-1877', 'From real tennis to Wimbledon 1877: how tennis was born', 'From the jeu de paume of French monasteries to the first Wimbledon tournament.', 6)),
   'santana': A(F4, 'img/r/Q445602.webp',
     ('manolo-santana-y-el-tenis-espanol', 'Manolo Santana y el despegue del tenis español', 'De recogepelotas en Madrid a campeón de Roland Garros, Forest Hills y Wimbledon.', 5),
     ('manolo-santana-and-the-rise-of-spanish-tennis', 'Manolo Santana and the rise of Spanish tennis', 'From ball boy in Madrid to champion at Roland Garros, Forest Hills and Wimbledon.', 5)),
   'raqueta': A(F5, 'img/r/Q16474.webp',
     ('de-la-madera-al-grafito-historia-de-la-raqueta', 'De la madera al grafito: historia de la raqueta', 'Cómo cambió la herramienta del tenista, y con ella la forma de jugar.', 5),
     ('from-wood-to-graphite-the-history-of-the-racket', 'From wood to graphite: the history of the racket', "How the player's tool changed, and the way the game is played changed with it.", 5)),
   'sexos': A(F6, 'img/a/partido-battle-of-the-sexes-king-v-riggs-1973.webp',
     ('la-batalla-de-los-sexos-king-contra-riggs', 'La batalla de los sexos: Billie Jean King contra Bobby Riggs', 'El partido de 1973 que vieron 90 millones de personas y que fue mucho más que un partido.', 5),
     ('the-battle-of-the-sexes-king-v-riggs', 'The Battle of the Sexes: Billie Jean King v Bobby Riggs', 'The 1973 match watched by 90 million people that was much more than a match.', 5)),
   'fedal': A(F7, 'img/r/Q10132.webp',
     ('federer-contra-nadal-la-rivalidad', 'Federer contra Nadal: la rivalidad que lo cambió todo', 'Cuarenta partidos, nueve finales de Grand Slam y una amistad: la historia del «Fedal».', 6),
     ('federer-v-nadal-the-rivalry', 'Federer v Nadal: the rivalry that changed everything', 'Forty matches, nine Grand Slam finals and a friendship: the story of «Fedal».', 6)),
   'australia': A(F8, 'img/a/torneo-australian-open.webp',
     ('historia-del-open-de-australia', 'Historia del Open de Australia', 'Del césped de 1905 a las pistas duras de Melbourne Park: el grande que abre la temporada.', 5),
     ('the-history-of-the-australian-open', 'The history of the Australian Open', 'From the grass of 1905 to the hard courts of Melbourne Park: the major that opens the season.', 5)),
  },
 },
 'newtonpedia': {
  'nombre': 'Newtonpedia', 'dominio': 'newtonpedia.com', 'autor': 'Alejandro Rosàs',
  'js_menu': 'assets/newton.js', 'clase_fig': 'blog-fig', 'clase_miga': 'miga',
  'pref': {'p': 'p/', 'd': 'd/', 's': 's/'},
  'data_raiz': {'es': '../', 'en': '../../en/'},
  'css': css('var(--ac2)', 'var(--te)', 'var(--t)', 'var(--pa)', 'var(--li)', 'var(--li)'),
  'head': NP['head'], 'cab': NP['cab'], 'pie': NP['pie'],
  'indice': {'es': ('El blog de Newtonpedia', 'Historias de científicos, inventos y descubrimientos que cambiaron el mundo. Un artículo nuevo cada martes.'),
             'en': ('The Newtonpedia blog', 'Stories of scientists, inventions and discoveries that changed the world. A new post every Tuesday.')},
  'articulos': {
   'relatividad': A(F0, 'img/p/Q937.webp',
     ('einstein-y-la-relatividad-general', 'Einstein y la relatividad general: la gravedad como curvatura', 'En noviembre de 1915 Einstein presentó la teoría que cambió nuestra idea del espacio, el tiempo y la gravedad.', 6),
     ('einstein-and-general-relativity', 'Einstein and general relativity: gravity as curvature', 'In November 1915 Einstein presented the theory that changed our idea of space, time and gravity.', 6)),
   'curie': A(F0, 'img/p/Q7186.webp',
     ('marie-curie-y-sus-dos-premios-nobel', 'Marie Curie y sus dos premios Nobel', 'La primera persona que ganó dos Nobel, y la única en dos ciencias distintas.', 6),
     ('marie-curie-and-her-two-nobel-prizes', 'Marie Curie and her two Nobel Prizes', 'The first person to win two Nobel Prizes, and the only one in two different sciences.', 6)),
   'lovelace': A(F0, 'img/p/Q7259.webp',
     ('ada-lovelace-y-el-primer-programa', 'Ada Lovelace y el primer programa de ordenador', 'La hija de Lord Byron que, en 1843, imaginó lo que podrían hacer las máquinas de calcular.', 5),
     ('ada-lovelace-and-the-first-computer-program', 'Ada Lovelace and the first computer program', "Lord Byron's daughter who, in 1843, imagined what calculating machines could do.", 5)),
   'darwin': A(F1, 'img/p/Q1035.webp',
     ('darwin-y-el-origen-de-las-especies', 'Darwin y «El origen de las especies»', 'El 24 de noviembre de 1859 salió a la venta el libro que explicó la evolución por selección natural.', 6),
     ('darwin-and-on-the-origin-of-species', 'Darwin and «On the Origin of Species»', 'On 24 November 1859 the book that explained evolution by natural selection went on sale.', 6)),
   'penicilina': A(F2, 'img/p/Q37064.webp',
     ('fleming-y-la-penicilina', 'Fleming y la penicilina: el moho que salvó millones de vidas', 'Un descuido en un laboratorio de Londres en 1928 y el largo camino hasta el primer antibiótico.', 5),
     ('fleming-and-penicillin', 'Fleming and penicillin: the mould that saved millions of lives', 'A slip in a London laboratory in 1928 and the long road to the first antibiotic.', 5)),
   'nobel': A(F3, 'img/p/Q23810.webp',
     ('historia-de-los-premios-nobel', 'Historia de los premios Nobel', 'Del inventor de la dinamita al premio más famoso de la ciencia, que se entrega cada 10 de diciembre.', 5),
     ('the-history-of-the-nobel-prizes', 'The history of the Nobel Prizes', "From the inventor of dynamite to science's most famous prize, awarded every 10 December.", 5)),
   'wright': A(F4, 'img/d/Q197.webp',
     ('los-hermanos-wright-y-el-primer-vuelo', 'Los hermanos Wright y el primer vuelo', 'El 17 de diciembre de 1903, en Kitty Hawk, un avión voló 12 segundos y cambió el mundo.', 5),
     ('the-wright-brothers-and-the-first-flight', 'The Wright brothers and the first flight', 'On 17 December 1903, at Kitty Hawk, a plane flew for 12 seconds and changed the world.', 5)),
   'newton': A(F5, 'img/p/Q935.webp',
     ('isaac-newton-nacido-el-dia-de-navidad', 'Isaac Newton, nacido el día de Navidad', 'El hombre que da nombre a esta web nació el 25 de diciembre de 1642. Repasamos su vida y sus grandes ideas.', 6),
     ('isaac-newton-born-on-christmas-day', 'Isaac Newton, born on Christmas Day', 'The man this site is named after was born on 25 December 1642. A look at his life and his great ideas.', 6)),
   'earthrise': A(F6, 'img/p/Q18762.webp',
     ('salida-de-la-tierra-la-foto-del-apolo-8', '«Salida de la Tierra»: la foto del Apolo 8', 'La Nochebuena de 1968, tres astronautas vieron por primera vez la Tierra asomando sobre la Luna.', 5),
     ('earthrise-the-apollo-8-photograph', 'Earthrise: the Apollo 8 photograph', 'On Christmas Eve 1968, three astronauts saw the Earth rising over the Moon for the first time.', 5)),
   'galileo': A(F7, 'img/p/Q307.webp',
     ('galileo-y-las-lunas-de-jupiter', 'Galileo y las lunas de Júpiter', 'En enero de 1610 un telescopio casero mostró cuatro lunas alrededor de Júpiter y puso en duda el universo de Ptolomeo.', 5),
     ('galileo-and-the-moons-of-jupiter', 'Galileo and the moons of Jupiter', 'In January 1610 a home-made telescope showed four moons around Jupiter and cast doubt on the universe of Ptolemy.', 5)),
   'cajal': A(F8, 'img/p/Q150526.webp',
     ('ramon-y-cajal-y-la-neurona', 'Ramón y Cajal y la neurona', 'Cómo un médico español, con un microscopio y mucha paciencia, descubrió cómo está hecho el cerebro.', 6),
     ('ramon-y-cajal-and-the-neuron', 'Ramón y Cajal and the neuron', 'How a Spanish doctor, with a microscope and great patience, discovered how the brain is built.', 6)),
  },
 },
}
