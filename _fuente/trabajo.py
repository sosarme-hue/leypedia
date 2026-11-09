# -*- coding: utf-8 -*-
# Materia Trabajo: jubilación y cómo leer la nómina
from curiosidades import *

ROUTES["trabajo"] = ("materias/trabajo/", "ca/materies/treball/")
ROUTES["jubilacion"] = ("materias/trabajo/jubilacion/", "ca/materies/treball/jubilacio/")
ROUTES["nomina"] = ("materias/trabajo/nomina/", "ca/materies/treball/nomina/")
for _k in ("trabajo", "jubilacion", "nomina"):
    PARENT[_k] = "materias"

def _T(es, a, b):
    return a if es else b

# ---------------- JUBILACIÓN ----------------
def jubilacion(lang):
    es = lang == "es"
    t = lambda a, b: _T(es, a, b)
    body = (
      f'<div class="claro"><span class="label">{t("En 30 segundos", "En 30 segons")}</span><p>'
      + t("En 2026 puedes jubilarte a los <b>65 años</b> si has cotizado al menos <b>38 años y 3 meses</b>; si no, a los <b>66 años y 10 meses</b>. Necesitas un mínimo de <b>15 años cotizados</b>. La pides a la Seguridad Social por internet o con cita previa, hasta 3 meses antes de la fecha en que quieras jubilarte.",
          "El 2026 et pots jubilar als <b>65 anys</b> si has cotitzat com a mínim <b>38 anys i 3 mesos</b>; si no, als <b>66 anys i 10 mesos</b>. Necessites un mínim de <b>15 anys cotitzats</b>. La demanes a la Seguretat Social per internet o amb cita prèvia, fins a 3 mesos abans de la data en què et vulguis jubilar.")
      + '</p></div>'
      + f'<h2>{t("¿A qué edad me puedo jubilar?", "A quina edat em puc jubilar?")}</h2>'
      + f'<p>{t("La edad ordinaria sube poco a poco hasta llegar a los 67 años en 2027. Quien ha cotizado muchos años puede seguir jubilándose a los 65.", "L&#39;edat ordinària puja de mica en mica fins a arribar als 67 anys el 2027. Qui ha cotitzat molts anys es pot continuar jubilant als 65.")}</p>'
      + table([t("Año", "Any"), t("Con estos años cotizados…", "Amb aquests anys cotitzats…"), t("…te jubilas a los", "…et jubiles als"), t("Si no los tienes", "Si no els tens")],
              [["2025", t("38 años o más", "38 anys o més"), "65", t("66 años y 8 meses", "66 anys i 8 mesos")],
               ["2026", t("38 años y 3 meses o más", "38 anys i 3 mesos o més"), "65", t("66 años y 10 meses", "66 anys i 10 mesos")],
               [t("2027 en adelante", "2027 en endavant"), t("38 años y 6 meses o más", "38 anys i 6 mesos o més"), "65", t("67 años", "67 anys")]])
      + f'<h2>{t("¿Cuánto cobraré?", "Quant cobraré?")}</h2>'
      + f'<p>{t("La pensión depende de dos cosas:", "La pensió depèn de dues coses:")}</p><ol>'
      + f'<li><b>{t("La base reguladora", "La base reguladora")}</b>: {t("una media de lo que has cotizado en los últimos años (en general, los últimos 25). Una reforma de 2023 permite, de forma gradual desde 2026, usar un periodo más largo descartando los peores meses; la Seguridad Social aplica la opción que te salga mejor.", "una mitjana del que has cotitzat els darrers anys (en general, els darrers 25). Una reforma del 2023 permet, de manera gradual des del 2026, fer servir un període més llarg descartant els pitjors mesos; la Seguretat Social aplica l&#39;opció que et surti millor.")}</li>'
      + f'<li><b>{t("El porcentaje según los años cotizados", "El percentatge segons els anys cotitzats")}</b>: {t("con 15 años cobras el 50 % de la base reguladora, y el porcentaje sube con cada mes cotizado hasta el 100 %, que en 2026 se alcanza con 36 años y 6 meses (37 años a partir de 2027).", "amb 15 anys cobres el 50 % de la base reguladora, i el percentatge puja amb cada mes cotitzat fins al 100 %, que el 2026 s&#39;assoleix amb 36 anys i 6 mesos (37 anys a partir del 2027).")}</li></ol>'
      + f'<p>{t("Cada enero las pensiones suben según el IPC medio del año anterior. Si tienes hijos, puedes tener derecho al complemento para reducir la brecha de género.", "Cada gener les pensions pugen segons l&#39;IPC mitjà de l&#39;any anterior. Si tens fills, pots tenir dret al complement per reduir la bretxa de gènere.")}</p>'
      + f'<div class="claro"><span class="label">{t("Consejo", "Consell")}</span><p>{t("Antes de decidir la fecha, consulta tu informe de vida laboral y usa el simulador de pensión de la Seguridad Social. Si falta algún periodo trabajado, pide que lo corrijan antes de jubilarte.", "Abans de decidir la data, consulta el teu informe de vida laboral i fes servir el simulador de pensió de la Seguretat Social. Si hi falta algun període treballat, demana que el corregeixin abans de jubilar-te.")}</p></div>'
      + f'<h2>{t("Tipos de jubilación", "Tipus de jubilació")}</h2>'
      + table([t("Tipo", "Tipus"), t("Cuándo", "Quan"), t("Qué tener en cuenta", "Què cal tenir en compte")],
              [[t("Ordinaria", "Ordinària"), t("A la edad que te corresponde", "A l&#39;edat que et correspon"), t("La pensión completa según tus años cotizados.", "La pensió completa segons els teus anys cotitzats.")],
               [t("Anticipada voluntaria", "Anticipada voluntària"), t("Hasta 2 años antes, con 35 años cotizados", "Fins a 2 anys abans, amb 35 anys cotitzats"), t("La pensión se reduce por cada mes que te adelantas.", "La pensió es redueix per cada mes que t&#39;avances.")],
               [t("Anticipada involuntaria", "Anticipada involuntària"), t("Hasta 4 años antes, con 33 años cotizados, si te han despedido por causas ajenas a ti", "Fins a 4 anys abans, amb 33 anys cotitzats, si t&#39;han acomiadat per causes alienes a tu"), t("También tiene reducción, menor que la voluntaria. Tienes que llevar al menos 6 meses inscrito como demandante de empleo.", "També té reducció, menor que la voluntària. Has de portar com a mínim 6 mesos inscrit com a demandant d&#39;ocupació.")],
               [t("Demorada", "Demorada"), t("Después de tu edad ordinaria", "Després de la teva edat ordinària"), t("Ganas un 4 % más por cada año completo que retrasas, o un pago único, o una combinación de los dos.", "Guanyes un 4 % més per cada any complet que endarrereixes, o un pagament únic, o una combinació de totes dues coses.")],
               [t("Activa y flexible", "Activa i flexible"), t("Ya jubilado", "Ja jubilat"), t("Permiten cobrar parte de la pensión mientras sigues trabajando.", "Permeten cobrar part de la pensió mentre continues treballant.")],
               [t("Parcial", "Parcial"), t("Desde los 63 aprox., con contrato de relevo", "Des dels 63 aprox., amb contracte de relleu"), t("Reduces tu jornada y cobras la pensión en proporción.", "Redueixes la jornada i cobres la pensió en proporció.")]])
      + f'<h2>{t("Cómo pedir la jubilación, paso a paso", "Com demanar la jubilació, pas a pas")}</h2><ol>'
      + f'<li><b>{t("Revisa tu vida laboral", "Revisa la teva vida laboral")}</b> {t("en la sede electrónica de la Seguridad Social. Comprueba que están todos tus trabajos.", "a la seu electrònica de la Seguretat Social. Comprova que hi són tots els teus treballs.")}</li>'
      + f'<li><b>{t("Elige la fecha", "Tria la data")}</b>. {t("Puedes presentar la solicitud hasta 3 meses antes de dejar de trabajar. Si la presentas más tarde, solo se paga con efectos de 3 meses hacia atrás.", "Pots presentar la sol·licitud fins a 3 mesos abans de deixar de treballar. Si la presentes més tard, només es paga amb efectes de 3 mesos enrere.")}</li>'
      + f'<li><b>{t("Presenta la solicitud", "Presenta la sol·licitud")}</b> {t("de una de estas formas:", "d&#39;una d&#39;aquestes maneres:")}<ul>'
      + f'<li>{t("Por internet, en «Tu Seguridad Social» o la sede electrónica, con Cl@ve, certificado digital o DNI electrónico.", "Per internet, a «Tu Seguridad Social» o la seu electrònica, amb Cl@ve, certificat digital o DNI electrònic.")}</li>'
      + f'<li>{t("Sin certificado, con el trámite de la sede electrónica que no lo exige (adjuntando foto de tu DNI).", "Sense certificat, amb el tràmit de la seu electrònica que no ho exigeix (adjuntant foto del DNI).")}</li>'
      + f'<li>{t("En persona, pidiendo cita previa en un centro de atención (CAISS) del INSS.", "En persona, demanant cita prèvia en un centre d&#39;atenció (CAISS) de l&#39;INSS.")}</li></ul></li>'
      + f'<li><b>{t("Documentos", "Documents")}</b>: {t("DNI o NIE, número de cuenta bancaria a tu nombre y, según el caso, el certificado de empresa, el libro de familia (para el complemento por hijos) o los papeles del despido (jubilación involuntaria).", "DNI o NIE, número de compte bancari a nom teu i, segons el cas, el certificat d&#39;empresa, el llibre de família (per al complement per fills) o els papers de l&#39;acomiadament (jubilació involuntària).")}</li>'
      + f'<li><b>{t("Espera la resolución", "Espera la resolució")}</b>. {t("El INSS tiene 90 días para resolver. Si no contesta, se entiende denegada y puedes reclamar.", "L&#39;INSS té 90 dies per resoldre. Si no contesta, s&#39;entén denegada i pots reclamar.")}</li></ol>'
      + f'<h2>{t("Si no estás de acuerdo", "Si no hi estàs d&#39;acord")}</h2>'
      + f'<p>{t("Si te deniegan la pensión o crees que el cálculo está mal, tienes <b>30 días</b> para presentar una reclamación previa al INSS. Si la rechazan, puedes acudir al Juzgado de lo Social.", "Si et deneguen la pensió o creus que el càlcul està malament, tens <b>30 dies</b> per presentar una reclamació prèvia a l&#39;INSS. Si la rebutgen, pots anar al Jutjat Social.")}</p>'
      + f'<h2>{t("Si no llegas a 15 años cotizados", "Si no arribes a 15 anys cotitzats")}</h2>'
      + f'<p>{t("Puedes pedir la pensión no contributiva de jubilación si tienes 65 años o más, has vivido en España al menos 10 años y tus ingresos son bajos.", "Pots demanar la pensió no contributiva de jubilació si tens 65 anys o més, has viscut a Espanya com a mínim 10 anys i els teus ingressos són baixos.")}</p>'
      + f'<p class="disc">{t("Información general, no asesoramiento. Cada caso tiene particularidades: profesiones con coeficientes reductores, periodos en el extranjero o regímenes especiales.", "Informació general, no assessorament. Cada cas té particularitats: professions amb coeficients reductors, períodes a l&#39;estranger o règims especials.")}</p>'
      + vig(lang, t("Ley General de la Seguridad Social (Real Decreto Legislativo 8/2015), versión consolidada del BOE", "Ley General de la Seguridad Social (Real Decreto Legislativo 8/2015), versió consolidada del BOE")))
    side = (box(t("En Catalunya", "A Catalunya"), f'<p>{t("La pensión de jubilación es estatal y la paga el INSS igual en toda España. Lo que gestiona la Generalitat es la pensión no contributiva: se pide al Departament de Drets Socials.", "La pensió de jubilació és estatal i la paga l&#39;INSS igual a tot Espanya. El que gestiona la Generalitat és la pensió no contributiva: es demana al Departament de Drets Socials.")}</p>', "box cc")
      + box(t("Datos clave", "Dades clau"), f'<dl><dt>{t("Quién la paga", "Qui la paga")}</dt><dd>Instituto Nacional de la Seguridad Social (INSS)</dd><dt>{t("Mínimo cotizado", "Mínim cotitzat")}</dt><dd>{t("15 años, 2 de ellos en los últimos 15", "15 anys, 2 dels quals en els darrers 15")}</dd><dt>{t("Plazo para resolver", "Termini per resoldre")}</dt><dd>{t("90 días", "90 dies")}</dd></dl>')
      + box(t("Te puede servir", "Et pot servir"), ul([f'<a href="{{nomina}}">{t("Cómo leer tu nómina", "Com llegir la teva nòmina")}</a>', f'<a href="{{trabajo}}">{t("Trabajo: todas las guías", "Treball: totes les guies")}</a>'])))
    return ficha(t("Guía · Trabajo", "Guia · Treball"), t("Cómo pedir la jubilación", "Com demanar la jubilació"),
                 t("A qué edad puedes jubilarte en 2026, cuánto cobrarás y cómo presentar la solicitud a la Seguridad Social.", "A quina edat et pots jubilar el 2026, quant cobraràs i com presentar la sol·licitud a la Seguretat Social."),
                 [(t("Norma", "Norma"), "Real Decreto Legislativo 8/2015"), (t("Edad en 2026", "Edat el 2026"), t("65 o 66 años y 10 meses", "65 o 66 anys i 10 mesos")), (t("Dónde", "On"), t("Seguridad Social (INSS)", "Seguretat Social (INSS)"))],
                 body, side)

# ---------------- NÓMINA ----------------
def eur(x):
    s = f"{x:,.2f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".") + " €"

def nomina(lang):
    es = lang == "es"
    t = lambda a, b: _T(es, a, b)
    base, plus = 1800.00, 200.00
    pr = round((base + plus) * 2 / 12, 2)
    dev = round(base + plus + pr, 2)
    cuotas = [(t("Contingencias comunes", "Contingències comunes"), 4.70), (t("Desempleo", "Atur"), 1.55), (t("Formación profesional", "Formació professional"), 0.10), (t("Mecanismo de Equidad Intergeneracional (MEI)", "Mecanisme d&#39;Equitat Intergeneracional (MEI)"), 0.15)]
    ss = [(n, r, round(dev * r / 100, 2)) for n, r in cuotas]
    tss = round(sum(x[2] for x in ss), 2)
    irpf = round(dev * 0.13, 2)
    ded = round(tss + irpf, 2)
    liq = round(dev - ded, 2)
    n = lambda i: f'<span class="nnum">{i}</span>'
    rows = (f'<tr class="nsec"><td colspan="3">{n(1)} {t("Encabezado", "Capçalera")}</td></tr>'
      + f'<tr><td colspan="3">{t("Empresa: Ejemplo, S. L. · CIF B00000000 · Código de cuenta de cotización", "Empresa: Exemple, S. L. · CIF B00000000 · Codi de compte de cotització")}<br>{t("Trabajador: Nombre Apellido · NIF · Nº de afiliación a la SS · Categoría: Administrativo · Grupo de cotización 5 · Antigüedad: 01/03/2021", "Treballador: Nom Cognom · NIF · Núm. d&#39;afiliació a la SS · Categoria: Administratiu · Grup de cotització 5 · Antiguitat: 01/03/2021")}<br>{t("Periodo: del 1 al 30 de noviembre de 2026 · 30 días", "Període: de l&#39;1 al 30 de novembre de 2026 · 30 dies")}</td></tr>'
      + f'<tr class="nsec"><td colspan="3">{n(2)} {t("Devengos (lo que ganas)", "Meritacions (el que guanyes)")}</td></tr>'
      + f'<tr><td>{t("Salario base", "Salari base")}</td><td></td><td class="r">{eur(base)}</td></tr>'
      + f'<tr><td>{t("Plus de convenio", "Plus de conveni")}</td><td></td><td class="r">{eur(plus)}</td></tr>'
      + f'<tr><td>{t("Prorrata de pagas extra", "Prorrata de pagues extra")}</td><td></td><td class="r">{eur(pr)}</td></tr>'
      + f'<tr class="ntot"><td>A. {t("Total devengado", "Total meritat")}</td><td></td><td class="r">{eur(dev)}</td></tr>'
      + f'<tr class="nsec"><td colspan="3">{n(3)} {t("Deducciones (lo que te descuentan)", "Deduccions (el que et descompten)")}</td></tr>'
      + "".join(f'<tr><td>{a}</td><td class="r">{f"{r:.2f}".replace(".", ",")} %</td><td class="r">{eur(v)}</td></tr>' for a, r, v in ss)
      + f'<tr><td>{t("Retención de IRPF", "Retenció d&#39;IRPF")}</td><td class="r">13,00 %</td><td class="r">{eur(irpf)}</td></tr>'
      + f'<tr class="ntot"><td>B. {t("Total a deducir", "Total a deduir")}</td><td></td><td class="r">{eur(ded)}</td></tr>'
      + f'<tr class="nliq"><td>{n(4)} {t("Líquido total a percibir (A − B)", "Líquid total a percebre (A − B)")}</td><td></td><td class="r">{eur(liq)}</td></tr>'
      + f'<tr class="nsec"><td colspan="3">{n(5)} {t("Bases de cotización y aportación de la empresa", "Bases de cotització i aportació de l&#39;empresa")}</td></tr>'
      + f'<tr><td>{t("Base de contingencias comunes y profesionales", "Base de contingències comunes i professionals")}</td><td></td><td class="r">{eur(dev)}</td></tr>'
      + f'<tr><td>{t("Base sujeta a retención de IRPF", "Base subjecta a retenció d&#39;IRPF")}</td><td></td><td class="r">{eur(dev)}</td></tr>')
    recibo = f'<div class="nomina"><div class="ncap">{t("Recibo de salarios · ejemplo", "Rebut de salaris · exemple")}</div><div class="tbl"><table>{rows}</table></div></div>'
    parts = [
     (t("El encabezado", "La capçalera"), t("Comprueba que tus datos son correctos, sobre todo la <b>categoría</b> y el <b>grupo de cotización</b>: de ellos depende el salario mínimo de tu convenio. La <b>antigüedad</b> puede darte derecho a complementos.", "Comprova que les teves dades són correctes, sobretot la <b>categoria</b> i el <b>grup de cotització</b>: en depèn el salari mínim del teu conveni. L&#39;<b>antiguitat</b> et pot donar dret a complements.")),
     (t("Los devengos", "Les meritacions"), t("Son todo lo que cobras en bruto. Las <b>percepciones salariales</b> (salario base, pluses, horas extra, pagas extra) cotizan y tributan. Las <b>no salariales</b>, como las dietas de viaje dentro de ciertos límites o las indemnizaciones, no cotizan. Si tus pagas extra no aparecen prorrateadas, las cobrarás aparte, normalmente en junio y diciembre.", "Són tot el que cobres en brut. Les <b>percepcions salarials</b> (salari base, plusos, hores extra, pagues extra) cotitzen i tributen. Les <b>no salarials</b>, com les dietes de viatge dins de certs límits o les indemnitzacions, no cotitzen. Si les pagues extra no apareixen prorratejades, les cobraràs a part, normalment al juny i al desembre.")),
     (t("Las deducciones", "Les deduccions"), t("Son de dos tipos. Las <b>cotizaciones a la Seguridad Social</b>, que en 2026 suman alrededor de un 6,5 % de tu sueldo si tienes contrato indefinido (el desempleo sube al 1,60 % en los contratos temporales); si cobras por encima de la base máxima, también aparece la cuota de solidaridad. Y la <b>retención de IRPF</b>, un adelanto del impuesto sobre la renta que tu empresa ingresa en Hacienda por ti y que se ajusta en la declaración de la renta.", "Són de dos tipus. Les <b>cotitzacions a la Seguretat Social</b>, que el 2026 sumen al voltant d&#39;un 6,5 % del sou si tens contracte indefinit (l&#39;atur puja a l&#39;1,60 % en els contractes temporals); si cobres per sobre de la base màxima, també hi apareix la quota de solidaritat. I la <b>retenció d&#39;IRPF</b>, un avançament de l&#39;impost sobre la renda que la teva empresa ingressa a Hisenda per tu i que s&#39;ajusta a la declaració de la renda.")),
     (t("El líquido a percibir", "El líquid a percebre"), t("Es lo que te llega al banco: el total devengado menos las deducciones. Es tu <b>sueldo neto</b>.", "És el que t&#39;arriba al banc: el total meritat menys les deduccions. És el teu <b>sou net</b>.")),
     (t("Las bases y la parte de la empresa", "Les bases i la part de l&#39;empresa"), t("Al pie aparecen las bases sobre las que se cotiza y lo que paga la empresa a la Seguridad Social por ti, que es bastante más que tu parte (alrededor de un 30 % adicional). Ese dinero no sale de tu sueldo, pero cuenta para tu futura pensión y tu paro.", "Al peu hi apareixen les bases sobre les quals es cotitza i el que paga l&#39;empresa a la Seguretat Social per tu, que és força més que la teva part (al voltant d&#39;un 30 % addicional). Aquests diners no surten del teu sou, però compten per a la teva futura pensió i el teu atur.")),
    ]
    body = (f'<div class="claro"><span class="label">{t("En 30 segundos", "En 30 segons")}</span><p>{t("La nómina tiene cinco partes: quién eres, lo que ganas en bruto, lo que te descuentan, lo que cobras en neto y, al pie, las bases de cotización. Abajo tienes un ejemplo con cada parte numerada.", "La nòmina té cinc parts: qui ets, el que guanyes en brut, el que et descompten, el que cobres en net i, al peu, les bases de cotització. A sota tens un exemple amb cada part numerada.")}</p></div>'
      + f'<h2>{t("Un ejemplo de nómina", "Un exemple de nòmina")}</h2>' + recibo
      + f'<p class="status">{t("Ejemplo con datos inventados: contrato indefinido, 2.000 € brutos al mes en 14 pagas y una retención de IRPF del 13 %. Tu retención depende de tu sueldo anual y tu situación familiar.", "Exemple amb dades inventades: contracte indefinit, 2.000 € bruts al mes en 14 pagues i una retenció d&#39;IRPF del 13 %. La teva retenció depèn del teu sou anual i la teva situació familiar.")}</p>'
      + f'<h2>{t("Qué significa cada parte", "Què vol dir cada part")}</h2><ol class="nlist">' + "".join(f'<li><b>{a}</b><p>{b}</p></li>' for a, b in parts) + '</ol>'
      + f'<h2>{t("Qué revisar cada mes", "Què revisar cada mes")}</h2>' + ul([
          t("Que el salario base no está por debajo del que marca tu convenio colectivo para tu categoría.", "Que el salari base no està per sota del que marca el teu conveni col·lectiu per a la teva categoria."),
          t("Que aparecen las horas extra que has hecho, o que te las han compensado con descanso.", "Que hi apareixen les hores extra que has fet, o que te les han compensat amb descans."),
          t("Que los días del periodo son correctos si has estado de baja o de vacaciones.", "Que els dies del període són correctes si has estat de baixa o de vacances."),
          t("Que la retención de IRPF no ha cambiado de golpe sin motivo. Si tu situación familiar cambia, comunícalo a la empresa con el modelo 145.", "Que la retenció d&#39;IRPF no ha canviat de cop sense motiu. Si la teva situació familiar canvia, comunica-ho a l&#39;empresa amb el model 145."),
          t("Que tu vida laboral en la Seguridad Social coincide con lo que dice la nómina.", "Que la teva vida laboral a la Seguretat Social coincideix amb el que diu la nòmina.")])
      + f'<h2>{t("Si algo no cuadra", "Si alguna cosa no quadra")}</h2>'
      + f'<p>{t("Pide explicaciones por escrito a la empresa. Puedes reclamar las cantidades que te deban durante <b>1 año</b>. Si no hay acuerdo, hay que presentar una papeleta de conciliación antes de ir al Juzgado de lo Social.", "Demana explicacions per escrit a l&#39;empresa. Pots reclamar les quantitats que et deguin durant <b>1 any</b>. Si no hi ha acord, cal presentar una papereta de conciliació abans d&#39;anar al Jutjat Social.")}</p>'
      + f'<p class="disc">{t("Información general, no asesoramiento. Los porcentajes de cotización son los del régimen general en 2026.", "Informació general, no assessorament. Els percentatges de cotització són els del règim general el 2026.")}</p>'
      + vig(lang, t("Estatuto de los Trabajadores (art. 29) y Orden de 27 de diciembre de 1994 sobre el recibo de salarios", "Estatuto de los Trabajadores (art. 29) i Orden de 27 de diciembre de 1994 sobre el rebut de salaris")))
    side = (box(t("En Catalunya", "A Catalunya"), f'<p>{t("La nómina es igual en toda España. En Catalunya la conciliación previa se presenta ante los servicios de conciliación del Departament d&#39;Empresa i Treball de la Generalitat.", "La nòmina és igual a tot Espanya. A Catalunya la conciliació prèvia es presenta davant dels serveis de conciliació del Departament d&#39;Empresa i Treball de la Generalitat.")}</p>', "box cc")
      + box(t("Datos clave", "Dades clau"), f'<dl><dt>{t("Tu cotización (indefinido)", "La teva cotització (indefinit)")}</dt><dd>{t("6,50 % en 2026", "6,50 % el 2026")}</dd><dt>{t("Plazo para reclamar salarios", "Termini per reclamar salaris")}</dt><dd>{t("1 año", "1 any")}</dd><dt>{t("Obligación de entregarla", "Obligació de lliurar-la")}</dt><dd>{t("Cada mes, en papel o en formato digital", "Cada mes, en paper o en format digital")}</dd></dl>')
      + box(t("Te puede servir", "Et pot servir"), ul([f'<a href="{{jubilacion}}">{t("Cómo pedir la jubilación", "Com demanar la jubilació")}</a>', f'<a href="{{cdimision}}">{t("Carta de dimisión", "Carta de dimissió")}</a>', f'<a href="{{csalarios}}">{t("Reclamación de salarios", "Reclamació de salaris")}</a>'])))
    return ficha(t("Guía · Trabajo", "Guia · Treball"), t("Cómo leer tu nómina", "Com llegir la teva nòmina"),
                 t("Qué es cada línea de la nómina, cuánto te descuentan y por qué, y qué revisar cada mes.", "Què és cada línia de la nòmina, quant et descompten i per què, i què revisar cada mes."),
                 [(t("Norma", "Norma"), t("Estatuto de los Trabajadores, art. 29", "Estatuto de los Trabajadores, art. 29")), (t("Materia", "Matèria"), t("Trabajo · Salario", "Treball · Salari"))], body, side)

def trabajo_hub(lang):
    es = lang == "es"
    t = lambda a, b: _T(es, a, b)
    g = [("jubilacion", t("Cómo pedir la jubilación", "Com demanar la jubilació"), t("Edad, cálculo de la pensión y solicitud paso a paso.", "Edat, càlcul de la pensió i sol·licitud pas a pas.")),
         ("nomina", t("Cómo leer tu nómina", "Com llegir la teva nòmina"), t("Un ejemplo con cada parte explicada.", "Un exemple amb cada part explicada."))]
    c = [("cdimision", t("Carta de dimisión", "Carta de dimissió")), ("csalarios", t("Reclamación de salarios", "Reclamació de salaris")), ("cdomestico", t("Contrato de empleada de hogar", "Contracte de treballadora de la llar")), ("cservicios", t("Contrato de servicios", "Contracte de serveis"))]
    return (f'<h2 class="sec">{t("Guías", "Guies")}</h2><div class="cols">' + "".join(f'<a class="card" href="{{{k_}}}"><span class="label">{t("Guía", "Guia")}</span><h3>{a}</h3><p>{b}</p><span class="go">{t("Leer la guía", "Llegir la guia")}</span></a>' for k_, a, b in g) + '</div>'
      + f'<h2 class="sec">{t("Modelos para el trabajo", "Models per a la feina")}</h2><div class="clinks">' + "".join(f'<a href="{{{k_}}}">{a}</a>' for k_, a in c) + '</div>'
      + f'<p class="status" style="margin-top:18px">{t("Próximamente: despidos, vacaciones, bajas y paro.", "Properament: acomiadaments, vacances, baixes i atur.")}</p>')

for _k, _f, _t in (("jubilacion", jubilacion, ("Cómo pedir la jubilación en 2026", "Com demanar la jubilació el 2026")),
                   ("nomina", nomina, ("Cómo leer tu nómina", "Com llegir la teva nòmina"))):
    PAGES[_k] = {L: dict(title=_t[0 if L == "es" else 1],
        desc=("Edad de jubilación en 2026, cálculo de la pensión, tipos de jubilación y cómo solicitarla a la Seguridad Social." if L == "es" else "Edat de jubilació el 2026, càlcul de la pensió, tipus de jubilació i com sol·licitar-la a la Seguretat Social") if _k == "jubilacion"
             else ("Qué significa cada parte de la nómina: devengos, cotizaciones, IRPF y líquido, con un ejemplo." if L == "es" else "Què vol dir cada part de la nòmina: meritacions, cotitzacions, IRPF i líquid, amb un exemple."),
        crumbs=[("materias", "Materias" if L == "es" else "Matèries"), ("trabajo", "Trabajo" if L == "es" else "Treball")], html=_f(L)) for L in ("es", "ca")}
PAGES["trabajo"] = {L: dict(title="Trabajo" if L == "es" else "Treball",
    desc="Guías de trabajo: jubilación, nómina y modelos de carta y contrato." if L == "es" else "Guies de treball: jubilació, nòmina i models de carta i contracte.",
    crumbs=[("materias", "Materias" if L == "es" else "Matèries")],
    html=simple("Materia" if L == "es" else "Matèria", "Trabajo" if L == "es" else "Treball",
                "Jubilación, nómina y modelos para el día a día en el trabajo." if L == "es" else "Jubilació, nòmina i models per al dia a dia a la feina.", trabajo_hub(L))) for L in ("es", "ca")}

# La materia Trabajo pasa a estar disponible en la cuadrícula de materias
def _mats_live(html, lang):
    es = lang == "es"
    old = f'<div class="mat"><b>{"Trabajo" if es else "Treball"}</b>'
    if old not in html:
        return html
    i = html.index(old); j = html.index("</div>", i)
    seg = html[i:j + 6]
    new = seg.replace('<div class="mat">', '<a class="mat" href="{trabajo}">', 1)[:-6] + "</a>"
    new = new.replace(f'<span class="var" style="color:var(--muted)">{"Próximamente" if es else "Properament"}</span>', "")
    return html.replace(seg, new)
for _p in PAGES.values():
    for L in ("es", "ca"):
        if L in _p and "html" in _p[L]:
            _p[L]["html"] = _mats_live(_p[L]["html"], L)
