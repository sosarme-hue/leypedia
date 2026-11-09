# -*- coding: utf-8 -*-
# Utilidades para definir contratos de forma compacta (motor genérico de app.js)

LISTA = []  # cada contrato añadido con X()

def N(i, es, ca):
    return (i, es, ca, "name")

def T(i, es, ca, v="", ph_es="", ph_ca=""):
    return (i, es, ca, "text", v, (ph_es, ph_ca))

def E(i, es, ca, v="1000", step="10"):
    return (i, es, ca, "number", v, f'min="0" step="{step}"')

def D(i, es, ca, v="1", mx="999"):
    return (i, es, ca, "number", v, f'min="0" max="{mx}"')

def S(i, es, ca, opts):
    return (i, es, ca, "select", opts)

def A(i, es, ca, ph_es="", ph_ca=""):
    return (i, es, ca, "area", "", (ph_es, ph_ca))

def R(la_es, lb_es, la_ca, lb_ca, a="a", b="b"):
    """Encabezado de contrato entre dos partes."""
    es = (f"En {{t:ci}}, a {{fecha}}.</p><p><b>REUNIDOS</b>: de una parte, {{n:{a}}}, mayor de edad, con DNI/NIE ____________, en adelante «{la_es}»; "
          f"y de otra, {{n:{b}}}, mayor de edad, con DNI/NIE ____________, en adelante «{lb_es}». Ambas partes se reconocen capacidad para firmar este documento y acuerdan lo siguiente:")
    ca = (f"A {{t:ci}}, {{fecha}}.</p><p><b>REUNITS</b>: d'una banda, {{n:{a}}}, major d'edat, amb DNI/NIE ____________, d'ara endavant «{la_ca}»; "
          f"i de l'altra, {{n:{b}}}, major d'edat, amb DNI/NIE ____________, d'ara endavant «{lb_ca}». Totes dues parts es reconeixen capacitat per signar aquest document i acorden el següent:")
    return es, ca

def L(a="a", b="b"):
    """Encabezado de carta o comunicación."""
    es = f"En {{t:ci}}, a {{fecha}}.</p><p><b>De:</b> {{n:{a}}}, con DNI/NIE ____________.<br><b>A:</b> {{n:{b}}}."
    ca = f"A {{t:ci}}, {{fecha}}.</p><p><b>De:</b> {{n:{a}}}, amb DNI/NIE ____________.<br><b>A:</b> {{n:{b}}}."
    return es, ca

FIRMA_ES = "Y en prueba de conformidad, las partes firman este documento por duplicado."
FIRMA_CA = "I, en prova de conformitat, les parts signen aquest document per duplicat."

def X(id, cat, slug_es, slug_ca, t, lead, ley, catn, tips, f, intro, c_es, c_ca, s_es, s_ca, firma=True):
    LISTA.append(dict(id=id, cat=cat, slug=(slug_es, slug_ca), t=t, lead=lead, ley=ley, catn=catn, tips=tips, f=f,
                      intro=intro, c=(c_es, c_ca), s=(s_es, s_ca), firma=firma))
