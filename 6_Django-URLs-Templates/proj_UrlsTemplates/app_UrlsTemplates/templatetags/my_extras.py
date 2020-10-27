#Archivo con Filtros customizados
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    '''
    Esta función corta todos los valores "arg" del String.
    '''
    return value.replace(arg,'')

#register.filter('cut', cut)