from django import template

register = template.Library()

@register.filter
def cod4(texto):
    if texto == 0:
        texto = ''
    else:
        texto = str(texto).rjust(4, '0')
    return texto

@register.filter
def em_branco(texto):
    if texto is None or texto == '0000':
        texto = ''
    return texto

@register.filter
def razao(texto):
    if texto is None:
        texto = ''
    else:
        texto = texto.upper()
        texto = texto[:30]
    return texto

@register.filter
def cnpj(texto):
    if texto is None:
        texto = ''
    else:
        texto = texto[0:2] + '.' + texto[2:5] + '.' + texto[5:8] + '/' + texto[8:12] + '-' + texto[12:14]
    return texto
