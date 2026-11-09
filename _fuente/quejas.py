# -*- coding: utf-8 -*-
# Sección de quejas y reclamaciones a la Administración, multas de tráfico y modelos en cada materia
from temas import *
from temas import _slug
from contratos3 import kc
from cbase import LISTA

LM = {c["id"]: c for c in LISTA}
def mlink(cid, lang):
    i = 0 if lang == "es" else 1
    c = LM[cid]
    return (kc(cid), c["t"][i], c["lead"][i])

def clinks(ids, lang):
    return '<div class="clinks">' + "".join(f'<a href="{{{k}}}">{t}<span>{d}</span></a>' for k, t, d in (mlink(x, lang) for x in ids)) + '</div>'

def guia(label, h1, lead, secs, side, lang, resumen):
    es = lang == "es"
    toc = "".join(f'<li><a href="#{_slug(s[0])}">{s[0]}</a></li>' for s in secs)
    body = (f'<div class="claro"><span class="label">{"En 30 segundos" if es else "En 30 segons"}</span><p>{resumen}</p></div>'
            + f'<nav class="toc"><span class="label">{"En esta página" if es else "En aquesta pàgina"}</span><ol>{toc}</ol></nav>'
            + "".join(f'<h2 id="{_slug(h)}">{h}</h2>{b}' for h, b in secs)
            + f'<p class="disc">{"Información general, no asesoramiento. Para un caso concreto, consulta con un profesional." if es else "Informació general, no assessorament. Per a un cas concret, consulta un professional."}</p>')
    return ficha(label, h1, lead, [], body, side)

ADM_IDS = ["instancia", "queja", "reposicion", "alzada", "silencio", "patrimonial", "transparencia", "defensor", "ruido", "historiaclinica", "tributario", "aplazamiento", "ssreclamacion"]
MUL_IDS = ["multaalegaciones", "multaconductor", "multarecurso"]

def quejas_page(lang):
    es = lang == "es"
    t = lambda a, b: a if es else b
    secs = [
     (t("Queja, solicitud, recurso o reclamación", "Queixa, sol·licitud, recurs o reclamació"),
      table([t("Escrito", "Escrit"), t("Para qué sirve", "Per a què serveix"), t("Plazo", "Termini")], [
        [t("Solicitud o instancia", "Sol·licitud o instància"), t("Pedir algo: una licencia, un certificado, una ayuda, una reparación.", "Demanar alguna cosa: una llicència, un certificat, un ajut, una reparació."), t("Sin plazo, salvo convocatorias", "Sense termini, tret de convocatòries")],
        [t("Queja o sugerencia", "Queixa o suggeriment"), t("Denunciar un mal servicio o un trato incorrecto, o proponer una mejora. No anula decisiones.", "Denunciar un mal servei o un tracte incorrecte, o proposar una millora. No anul·la decisions."), t("Sin plazo", "Sense termini")],
        [t("Recurso de reposición", "Recurs de reposició"), t("Pedir al mismo órgano que revise su decisión.", "Demanar al mateix òrgan que revisi la seva decisió."), t("1 mes", "1 mes")],
        [t("Recurso de alzada", "Recurs d'alçada"), t("Recurrir ante el superior una decisión que no agota la vía administrativa.", "Recórrer davant el superior una decisió que no esgota la via administrativa."), t("1 mes", "1 mes")],
        [t("Reclamación de daños", "Reclamació de danys"), t("Pedir una indemnización por un daño causado por un servicio público.", "Demanar una indemnització per un dany causat per un servei públic."), t("1 año", "1 any")],
        [t("Queja al Defensor o al Síndic", "Queixa al Defensor o al Síndic"), t("Cuando la administración no responde o vulnera tus derechos.", "Quan l'administració no respon o vulnera els teus drets."), t("1 año (Defensor del Pueblo)", "1 any (Defensor del Poble)")]])),
     (t("A quién dirigirte", "A qui adreçar-te"),
      table([t("Administración", "Administració"), t("Qué lleva", "Què porta"), t("Dónde presentar", "On presentar")], [
        [t("Ayuntamiento", "Ajuntament"), t("Calles, limpieza, ruido, licencias de obras y actividades, padrón, IBI, plusvalía, multas en ciudad, servicios sociales básicos.", "Carrers, neteja, soroll, llicències d'obres i activitats, padró, IBI, plusvàlua, multes a ciutat, serveis socials bàsics."), t("Sede electrónica o registro municipal (OAC)", "Seu electrònica o registre municipal (OAC)")],
        [t("Generalitat (consellerias)", "Generalitat (conselleries)"), t("Sanidad, educación, vivienda pública, consumo, dependencia, medio ambiente, multas en carreteras catalanas (Servei Català de Trànsit), tributos cedidos.", "Salut, educació, habitatge públic, consum, dependència, medi ambient, multes a carreteres catalanes (Servei Català de Trànsit), tributs cedits."), t("seu.gencat.cat, Oficines d'Atenció Ciutadana o teléfono 012", "seu.gencat.cat, Oficines d'Atenció Ciutadana o telèfon 012")],
        [t("Delegación y subdelegaciones del Gobierno", "Delegació i subdelegacions del Govern"), t("Extranjería, sanciones de seguridad ciudadana, armas, manifestaciones, coordinación de servicios del Estado en la provincia.", "Estrangeria, sancions de seguretat ciutadana, armes, manifestacions, coordinació de serveis de l'Estat a la província."), t("Sede electrónica del Ministerio de Política Territorial o registro de la Subdelegación", "Seu electrònica del Ministeri de Política Territorial o registre de la Subdelegació")],
        [t("Organismos del Estado", "Organismes de l'Estat"), t("Agencia Tributaria, Seguridad Social, SEPE, DGT fuera de Catalunya, Catastro, Registro Civil, pasaporte y DNI.", "Agència Tributària, Seguretat Social, SEPE, DGT fora de Catalunya, Cadastre, Registre Civil, passaport i DNI."), t("Sede electrónica de cada organismo o red de oficinas", "Seu electrònica de cada organisme o xarxa d'oficines")],
        [t("Defensores", "Defensors"), t("Defensor del Pueblo (Estado), Síndic de Greuges (Generalitat, ayuntamientos y servicios básicos en Catalunya) y síndics municipals en muchas ciudades.", "Defensor del Poble (Estat), Síndic de Greuges (Generalitat, ajuntaments i serveis bàsics a Catalunya) i síndics municipals a moltes ciutats."), t("Formulario en su web, gratis y sin abogado", "Formulari al seu web, gratuït i sense advocat")]])),
     (t("Cómo redactarlo", "Com redactar-lo"),
      t("<p>Cualquier escrito a la Administración debe incluir, según el artículo 66 de la Ley 39/2015:</p><ol><li>Tu nombre, DNI y un domicilio o medio electrónico para recibir la respuesta.</li><li>Los <b>hechos</b> explicados por orden y con fechas (EXPONE).</li><li>Lo que <b>pides</b>, de forma concreta (SOLICITA).</li><li>Lugar, fecha y firma.</li><li>El órgano al que va dirigido, con el número de expediente si lo hay.</li></ol><p>Escribe con frases cortas y sin adjetivos: cuanto más concreto, más fácil es que te den la razón. Adjunta las pruebas (fotos, recibos, notificaciones) y cítalas en el texto.</p>",
        "<p>Qualsevol escrit a l'Administració ha d'incloure, segons l'article 66 de la Ley 39/2015:</p><ol><li>El teu nom, DNI i un domicili o mitjà electrònic per rebre la resposta.</li><li>Els <b>fets</b> explicats per ordre i amb dates (EXPOSA).</li><li>El que <b>demanes</b>, de manera concreta (SOL·LICITA).</li><li>Lloc, data i signatura.</li><li>L'òrgan al qual s'adreça, amb el número d'expedient si n'hi ha.</li></ol><p>Escriu amb frases curtes i sense adjectius: com més concret, més fàcil és que et donin la raó. Adjunta les proves (fotos, rebuts, notificacions) i cita-les al text.</p>")),
     (t("Dónde y cómo presentarlo", "On i com presentar-lo"),
      t("<ul><li><b>Por internet</b>, en la sede electrónica, con certificado digital, Cl@ve o idCAT Mòbil. Es lo más rápido y te da justificante al momento.</li><li><b>En persona</b>, en cualquier oficina de registro de cualquier administración: el escrito se enviará a la destinataria (art. 16.4 de la Ley 39/2015).</li><li><b>Por Correos</b>, con «certificado administrativo»: se sella la copia antes de cerrar el sobre y cuenta la fecha de entrega en Correos.</li></ul><p>Guarda siempre el justificante con el número de registro: es tu prueba de que lo presentaste en plazo. Los plazos en días se cuentan en <b>días hábiles</b> (sin sábados, domingos ni festivos), salvo en las multas de tráfico, que van en días naturales.</p>",
        "<ul><li><b>Per internet</b>, a la seu electrònica, amb certificat digital, Cl@ve o idCAT Mòbil. És el més ràpid i et dona justificant al moment.</li><li><b>En persona</b>, a qualsevol oficina de registre de qualsevol administració: l'escrit s'enviarà a la destinatària (art. 16.4 de la Ley 39/2015).</li><li><b>Per Correus</b>, amb «certificat administratiu»: se segella la còpia abans de tancar el sobre i compta la data de lliurament a Correus.</li></ul><p>Guarda sempre el justificant amb el número de registre: és la teva prova que el vas presentar dins de termini. Els terminis en dies es compten en <b>dies hàbils</b> (sense dissabtes, diumenges ni festius), tret de les multes de trànsit, que van en dies naturals.</p>")),
     (t("Si no te responden", "Si no et responen"),
      t("<p>La Administración está obligada a resolver. Si no fija otro plazo, tiene <b>tres meses</b>. Si no lo hace hay «silencio administrativo»:</p><ul><li>En la mayoría de trámites que pides tú, es <b>positivo</b>: se entiende concedido.</li><li>En los recursos, la responsabilidad patrimonial y algunos otros, es <b>negativo</b>: se entiende denegado y puedes pasar al siguiente paso.</li></ul><p>Puedes pedir un certificado que acredite el silencio con el modelo de abajo.</p>",
        "<p>L'Administració està obligada a resoldre. Si no fixa un altre termini, té <b>tres mesos</b>. Si no ho fa hi ha «silenci administratiu»:</p><ul><li>En la majoria de tràmits que demanes tu, és <b>positiu</b>: s'entén concedit.</li><li>En els recursos, la responsabilitat patrimonial i alguns altres, és <b>negatiu</b>: s'entén denegat i pots passar al pas següent.</li></ul><p>Pots demanar un certificat que acrediti el silenci amb el model de sota.</p>")),
     (t("Y después: el juzgado", "I després: el jutjat"),
      t("<p>Cuando se agota la vía administrativa, puedes acudir al <b>juzgado de lo contencioso-administrativo</b> en un plazo de <b>dos meses</b> desde la notificación (o seis meses si fue por silencio). Normalmente necesitas abogado. Si tus ingresos son bajos, puedes pedir <b>justicia gratuita</b> en el colegio de abogados.</p>",
        "<p>Quan s'esgota la via administrativa, pots anar al <b>jutjat contenciós administratiu</b> en un termini de <b>dos mesos</b> des de la notificació (o sis mesos si va ser per silenci). Normalment necessites advocat. Si els teus ingressos són baixos, pots demanar <b>justícia gratuïta</b> al col·legi d'advocats.</p>")),
     (t("Modelos gratuitos", "Models gratuïts"), clinks(ADM_IDS + MUL_IDS, lang)),
    ]
    side = (box(t("En Catalunya", "A Catalunya"), t("<p>La Generalitat tiene su propia ley de procedimiento (Llei 26/2010) y el teléfono 012 de atención ciudadana. El Síndic de Greuges supervisa a la Generalitat, a los ayuntamientos catalanes y a las empresas de agua, luz, gas y telecomunicaciones. Para el acceso a información pública, la GAIP resuelve las reclamaciones.</p>", "<p>La Generalitat té la seva pròpia llei de procediment (Llei 26/2010) i el telèfon 012 d'atenció ciutadana. El Síndic de Greuges supervisa la Generalitat, els ajuntaments catalans i les empreses d'aigua, llum, gas i telecomunicacions. Per a l'accés a informació pública, la GAIP resol les reclamacions.</p>"), "box cc")
            + box(t("Datos clave", "Dades clau"), "<dl>" + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in [
                (t("Plazo para recurrir", "Termini per recórrer"), t("1 mes", "1 mes")), (t("Plazo para resolver (general)", "Termini per resoldre (general)"), t("3 meses", "3 mesos")),
                (t("Daños por un servicio público", "Danys per un servei públic"), t("1 año para reclamar", "1 any per reclamar")), (t("Ir al juzgado", "Anar al jutjat"), t("2 meses", "2 mesos"))]) + "</dl>")
            + box(t("Te puede servir", "Et pot servir"), ul([f'<a href="{{multas}}">{t("Multas de tráfico: cómo responder", "Multes de trànsit: com respondre")}</a>', f'<a href="{{administracion}}">{t("Administración: trámites y derechos", "Administració: tràmits i drets")}</a>', f'<a href="{{contratos}}">{t("Todos los modelos", "Tots els models")}</a>'])))
    resumen = t("Para pedir algo a la Administración o quejarte, escribe un escrito con tus datos, los hechos y lo que pides, y preséntalo por registro guardando el justificante. Si te han notificado una decisión que te perjudica, tienes normalmente un mes para recurrirla. Si no te responden, el silencio también tiene consecuencias. Aquí tienes los modelos más usados, listos para rellenar.",
                "Per demanar alguna cosa a l'Administració o queixar-te, redacta un escrit amb les teves dades, els fets i el que demanes, i presenta'l per registre guardant el justificant. Si t'han notificat una decisió que et perjudica, normalment tens un mes per recórrer-la. Si no et responen, el silenci també té conseqüències. Aquí tens els models més utilitzats, a punt per omplir.")
    return guia(t("Quejas y reclamaciones", "Queixes i reclamacions"), t("Quejas, reclamaciones y recursos ante la Administración", "Queixes, reclamacions i recursos davant l'Administració"),
                t("Ayuntamientos, consellerias, Delegación del Gobierno y ministerios: a quién dirigirte, cómo escribirlo, plazos y modelos gratuitos.", "Ajuntaments, conselleries, Delegació del Govern i ministeris: a qui adreçar-te, com escriure-ho, terminis i models gratuïts."),
                secs, side, lang, resumen)

def multas_page(lang):
    es = lang == "es"
    t = lambda a, b: a if es else b
    secs = [
     (t("Quién te pone la multa", "Qui et posa la multa"),
      table([t("Dónde", "On"), t("Quién sanciona", "Qui sanciona")], [
        [t("Ciudad (vías urbanas)", "Ciutat (vies urbanes)"), t("El ayuntamiento (Guardia Urbana o Policía Local)", "L'ajuntament (Guàrdia Urbana o Policia Local)")],
        [t("Carreteras de Catalunya", "Carreteres de Catalunya"), t("Servei Català de Trànsit (denuncian los Mossos d'Esquadra)", "Servei Català de Trànsit (denuncien els Mossos d'Esquadra)")],
        [t("Carreteras del resto de España (salvo País Vasco)", "Carreteres de la resta d'Espanya (tret del País Basc)"), t("Dirección General de Tráfico (denuncia la Guardia Civil)", "Direcció General de Trànsit (denuncia la Guàrdia Civil)")]])
      + t("<p>Es importante saberlo porque los escritos se dirigen a quien sanciona, y el número de expediente y la forma de pago cambian.</p>", "<p>És important saber-ho perquè els escrits s'adrecen a qui sanciona, i el número d'expedient i la forma de pagament canvien.</p>")),
     (t("Cómo te la notifican", "Com te la notifiquen"),
      t("<ul><li><b>En el acto</b>, si el agente te para: la denuncia ya es la notificación.</li><li><b>Por correo certificado</b> al domicilio del titular del vehículo.</li><li><b>En la Dirección Electrónica Vial (DEV)</b>, obligatoria para empresas y voluntaria para particulares: la notificación se entiende hecha a los 10 días aunque no la abras.</li><li><b>En el Tablón Edictal Único del BOE</b>, si no te encuentran: pasados 20 días cuenta como notificada. Por eso conviene tener actualizado el domicilio en la DGT.</li></ul>",
        "<ul><li><b>En l'acte</b>, si l'agent t'atura: la denúncia ja és la notificació.</li><li><b>Per correu certificat</b> al domicili del titular del vehicle.</li><li><b>A la Direcció Electrònica Vial (DEV)</b>, obligatòria per a empreses i voluntària per a particulars: la notificació s'entén feta als 10 dies encara que no l'obris.</li><li><b>Al Tauler Edictal Únic del BOE</b>, si no et troben: passats 20 dies compta com a notificada. Per això convé tenir actualitzat el domicili a la DGT.</li></ul>")),
     (t("Qué puedes hacer en 20 días naturales", "Què pots fer en 20 dies naturals"),
      t("<ol><li><b>Pagar con un 50 % de descuento.</b> El expediente se cierra, pero renuncias a alegar y se aplican los puntos. No sirve para algunas infracciones muy graves.</li><li><b>Identificar al conductor</b>, si no conducías tú. Es obligatorio: no hacerlo es una infracción muy grave con una multa mucho mayor.</li><li><b>Presentar alegaciones</b>, si crees que la multa es injusta. Pierdes el descuento.</li></ol><p>Si no haces nada, a los 30 días la denuncia se convierte en sanción firme y tendrás que pagar el importe completo.</p>",
        "<ol><li><b>Pagar amb un 50 % de descompte.</b> L'expedient es tanca, però renuncies a al·legar i s'apliquen els punts. No serveix per a algunes infraccions molt greus.</li><li><b>Identificar el conductor</b>, si no conduïes tu. És obligatori: no fer-ho és una infracció molt greu amb una multa molt més alta.</li><li><b>Presentar al·legacions</b>, si creus que la multa és injusta. Perds el descompte.</li></ol><p>Si no fas res, als 30 dies la denúncia es converteix en sanció ferma i hauràs de pagar l'import complet.</p>")),
     (t("Motivos habituales para recurrir", "Motius habituals per recórrer"),
      t("<ul><li><b>Prescripción</b>: la infracción prescribe a los 3 meses si es leve y a los 6 meses si es grave o muy grave, si en ese tiempo no te la notifican.</li><li><b>Radar</b>: debe tener verificación metrológica vigente, y se aplica un margen de error (en radares fijos, 5 km/h hasta 100 km/h y 5 % por encima; en móviles, 7 km/h y 7 %).</li><li><b>Notificación defectuosa</b>: enviada a un domicilio antiguo, sin el segundo intento, o publicada en el BOE sin intentar antes la notificación personal.</li><li><b>Falta de prueba</b>: sin fotografía, sin identificar al agente o con hechos descritos de forma genérica.</li><li><b>Señalización</b> inexistente, tapada o contradictoria.</li></ul>",
        "<ul><li><b>Prescripció</b>: la infracció prescriu als 3 mesos si és lleu i als 6 mesos si és greu o molt greu, si en aquest temps no te la notifiquen.</li><li><b>Radar</b>: ha de tenir verificació metrològica vigent, i s'aplica un marge d'error (en radars fixos, 5 km/h fins a 100 km/h i 5 % per sobre; en mòbils, 7 km/h i 7 %).</li><li><b>Notificació defectuosa</b>: enviada a un domicili antic, sense el segon intent, o publicada al BOE sense intentar abans la notificació personal.</li><li><b>Manca de prova</b>: sense fotografia, sense identificar l'agent o amb fets descrits de manera genèrica.</li><li><b>Senyalització</b> inexistent, tapada o contradictòria.</li></ul>")),
     (t("Cuánto cuesta y cuántos puntos", "Quant costa i quants punts"),
      table([t("Tipo", "Tipus"), t("Multa", "Multa"), t("Puntos", "Punts")], [
        [t("Leve", "Lleu"), t("Hasta 100 €", "Fins a 100 €"), t("No quita puntos", "No treu punts")],
        [t("Grave", "Greu"), t("200 € (velocidad: 100 a 600 €)", "200 € (velocitat: 100 a 600 €)"), t("De 2 a 6 según la infracción", "De 2 a 6 segons la infracció")],
        [t("Muy grave", "Molt greu"), t("500 € (alcohol o drogas: 500 o 1.000 €)", "500 € (alcohol o drogues: 500 o 1.000 €)"), t("Hasta 6", "Fins a 6")]])),
     (t("Si ya te han sancionado", "Si ja t'han sancionat"),
      t("<p>Contra la resolución sancionadora cabe <b>recurso de reposición</b> en un mes, ante el mismo organismo. Después, o si no responden en un mes, puedes ir al <b>juzgado contencioso-administrativo</b> en dos meses. Si no pagas, te cobrarán por vía de apremio con un recargo, y pueden embargar cuentas o la devolución de Hacienda. La sanción prescribe a los cuatro años.</p>",
        "<p>Contra la resolució sancionadora hi escau <b>recurs de reposició</b> en un mes, davant el mateix organisme. Després, o si no responen en un mes, pots anar al <b>jutjat contenciós administratiu</b> en dos mesos. Si no pagues, te la cobraran per via de constrenyiment amb un recàrrec, i poden embargar comptes o la devolució d'Hisenda. La sanció prescriu als quatre anys.</p>")),
     (t("Modelos gratuitos", "Models gratuïts"), clinks(MUL_IDS, lang)),
    ]
    side = (box(t("En Catalunya", "A Catalunya"), t("<p>En las carreteras catalanas la autoridad de tráfico es el Servei Català de Trànsit, no la DGT. Sus multas se pagan y se recurren en la seu electrònica de la Generalitat. Los puntos del carnet sí son estatales: los gestiona la DGT para todos.</p>", "<p>A les carreteres catalanes l'autoritat de trànsit és el Servei Català de Trànsit, no la DGT. Les seves multes es paguen i es recorren a la seu electrònica de la Generalitat. Els punts del carnet sí que són estatals: els gestiona la DGT per a tothom.</p>"), "box cc")
            + box(t("Datos clave", "Dades clau"), "<dl>" + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in [
                (t("Pagar con descuento o alegar", "Pagar amb descompte o al·legar"), t("20 días naturales", "20 dies naturals")), (t("Descuento por pronto pago", "Descompte per pagament immediat"), "50 %"),
                (t("Identificar al conductor", "Identificar el conductor"), t("20 días naturales", "20 dies naturals")), (t("Recurso de reposición", "Recurs de reposició"), t("1 mes", "1 mes"))]) + "</dl>")
            + box(t("Te puede servir", "Et pot servir"), ul([f'<a href="{{quejas}}">{t("Quejas y recursos ante la Administración", "Queixes i recursos davant l'Administració")}</a>', f'<a href="{{administracion}}">{t("Administración", "Administració")}</a>'])))
    resumen = t("Cuando te llega una multa tienes 20 días naturales para elegir: pagarla con un 50 % de descuento, identificar al conductor si no eras tú, o presentar alegaciones si crees que es injusta. Si no haces nada, se convierte en sanción por el importe completo. En Catalunya, las multas en carretera son del Servei Català de Trànsit, y en ciudad, del ayuntamiento.",
                "Quan t'arriba una multa tens 20 dies naturals per triar: pagar-la amb un 50 % de descompte, identificar el conductor si no eres tu, o presentar al·legacions si creus que és injusta. Si no fas res, es converteix en sanció per l'import complet. A Catalunya, les multes a carretera són del Servei Català de Trànsit, i a ciutat, de l'ajuntament.")
    return guia(t("Materia · Tráfico", "Matèria · Trànsit"), t("Multas de tráfico: cómo responder", "Multes de trànsit: com respondre"),
                t("Qué hacer cuando te llega una multa, a quién dirigirte, plazos, motivos para recurrir y modelos gratuitos de alegaciones y recursos.", "Què fer quan t'arriba una multa, a qui adreçar-te, terminis, motius per recórrer i models gratuïts d'al·legacions i recursos."),
                secs, side, lang, resumen)

ROUTES["quejas"] = ("quejas-y-reclamaciones/", "ca/queixes-i-reclamacions/")
ROUTES["multas"] = ("materias/multas-de-trafico/", "ca/materies/multes-de-transit/")
PARENT["multas"] = "materias"
PAGES["quejas"] = {L: dict(title="Quejas y reclamaciones a la Administración" if L == "es" else "Queixes i reclamacions a l'Administració",
    desc="Cómo quejarte o reclamar a ayuntamientos, consellerias, Delegación del Gobierno y ministerios: a quién dirigirte, plazos y modelos gratuitos." if L == "es" else "Com queixar-te o reclamar a ajuntaments, conselleries, Delegació del Govern i ministeris: a qui adreçar-te, terminis i models gratuïts.",
    crumbs=[], html=quejas_page(L)) for L in ("es", "ca")}
PAGES["multas"] = {L: dict(title="Multas de tráfico: cómo responder" if L == "es" else "Multes de trànsit: com respondre",
    desc="Qué hacer cuando te llega una multa de tráfico: pagar con descuento, identificar al conductor, alegar o recurrir, plazos y modelos." if L == "es" else "Què fer quan t'arriba una multa de trànsit: pagar amb descompte, identificar el conductor, al·legar o recórrer, terminis i models.",
    crumbs=[("materias", "Materias" if L == "es" else "Matèries")], html=multas_page(L)) for L in ("es", "ca")}

# menú: añadir «Quejas» tras Contratos
for L, txt in (("es", "Quejas"), ("ca", "Queixes")):
    nav = UI[L]["nav"]
    if not any(k == "quejas" for k, _ in nav):
        nav.insert([k for k, _ in nav].index("contratos") + 1, ("quejas", txt))
PARENT.setdefault("quejas", "quejas")

# Quejas y reclamaciones frecuentes en cada materia
QMAP = {
 "vivienda": ["ruido", "llaves", "reclamacion", "queja"],
 "trabajo": ["salarios", "ssreclamacion", "dimision", "queja"],
 "familia": ["instancia", "queja", "silencio", "defensor"],
 "sucesiones": ["tributario", "aplazamiento", "instancia"],
 "consumo": ["reclamacion", "garantia", "baja", "desistimientocompra", "defensor"],
 "autonomos": ["tributario", "aplazamiento", "ssreclamacion", "instancia"],
 "fiscalidad": ["tributario", "aplazamiento", "silencio"],
 "segsocial": ["ssreclamacion", "historiaclinica", "defensor"],
 "extranjeria": ["queja", "silencio", "alzada", "defensor"],
 "administracion": ["instancia", "queja", "reposicion", "alzada", "silencio", "patrimonial", "transparencia", "defensor"],
 "datos": ["rgpd", "transparencia", "queja"],
}
for mk, ids in QMAP.items():
    if mk not in PAGES:
        continue
    for L in ("es", "ca"):
        es = L == "es"
        blk = (f'<h2 id="quejas-frecuentes">{"Quejas y reclamaciones más frecuentes" if es else "Queixes i reclamacions més freqüents"}</h2>'
               + f'<p>{"Modelos gratuitos que se rellenan en tu navegador. Para escritos a cualquier administración, consulta también la guía de " if es else "Models gratuïts que s&#39;omplen al teu navegador. Per a escrits a qualsevol administració, consulta també la guia de "}<a href="{{quejas}}">{"quejas y reclamaciones" if es else "queixes i reclamacions"}</a>.</p>'
               + clinks(ids, L))
        h = PAGES[mk][L]["html"]
        for marker in ('<p class="disc">', '<span class="vig">'):
            if marker in h:
                i = h.index(marker); h = h[:i] + blk + h[i:]; break
        else:
            i = h.rfind('</div></div>')
            h = h[:i] + '<div class="prose" style="margin-top:22px">' + blk + '</div>' + h[i:]
        PAGES[mk][L]["html"] = h
    if mk in MAT:
        pass

# Enlace a multas desde la página de materias
for L in ("es", "ca"):
    es = L == "es"
    card = (f'<a class="guia" href="{{multas}}"><b>{"Multas de tráfico" if es else "Multes de trànsit"}</b><span>{"Pagar, alegar o recurrir, y modelos." if es else "Pagar, al·legar o recórrer, i models."}</span></a>'
            f'<a class="guia" href="{{quejas}}"><b>{"Quejas a la Administración" if es else "Queixes a l&#39;Administració"}</b><span>{"Ayuntamientos, Generalitat y Estado." if es else "Ajuntaments, Generalitat i Estat."}</span></a>')
    for pid in ("home", "materias"):
        h = PAGES[pid][L]["html"]
        j = h.find('<div class="guias">')
        if j >= 0:
            k = h.find('</div>', j)
            PAGES[pid][L]["html"] = h[:k] + card + h[k:]
