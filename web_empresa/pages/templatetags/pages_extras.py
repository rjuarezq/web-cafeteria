from django import template
from pages.models import Page

#Registrar el template tag en la libreria de templates
register = template.Library()

#Con este decorador transformamos la función normal en un tag simple y lo registramos 
#en la libreria de templates
@register.simple_tag()
def get_page_list():
    #Recuperamos todas las paginas
    pages = Page.objects.all()
    #Devolvemos al template en forma de templatetag
    return pages