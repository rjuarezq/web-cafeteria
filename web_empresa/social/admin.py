from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


    def get_readonly_fields(self, request, obj=None):
        #Filtro para inhabilitar la edición de los campos del grupo Personal    
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name', )
        #Condicional para inhabilitar los campos por defecto 
        #sino pertenece el usuario al grupo Personal 
        else:
            return ('created', 'updated')
    
admin.site.register(Link, LinkAdmin)