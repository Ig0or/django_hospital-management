from django import template

register = template.Library()

@register.filter(name='addvalue')
def addvalue(value, arg):
    return value.as_widget(attrs={'value': arg})