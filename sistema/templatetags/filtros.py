from django import template

register = template.Library()


@register.filter(name='addvalue')
def addvalue(value, arg):
    return value.as_widget(attrs={'value': arg})


@register.filter(name='formatcpf')
def formatcpf(value):
    cpf = []
    for index, numero in enumerate(value):
        if index == 3 or index == 6:
            cpf.append('.')
            cpf.append(numero)
        elif index == 9:
            cpf.append('-')
            cpf.append(numero)
        else:
            cpf.append(numero)
    cpf = ''.join(cpf)
    return cpf


@register.filter(nome='formatphone')
def formatphone(value):
    telefone = []
    for index, numero in enumerate(value):
        if index == 0:
            telefone.append('(')
            telefone.append(numero)
        elif index == 2:
            telefone.append(')')
            telefone.append(' ')
            telefone.append(numero)
        elif index == 7:
            telefone.append('-')
            telefone.append(numero)
        else:
            telefone.append(numero)
    telefone = ''.join(telefone)
    return telefone


@register.filter(name='formatcep')
def formatcep(value):
    cep = []
    for index, numero in enumerate(value):
        if index == 5:
            cep.append('-')
            cep.append(numero)
        else:
            cep.append(numero)
    cep = ''.join(cep)
    return cep