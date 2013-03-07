__author__ = 'Beren'
from contenidos.modulos.textos.models import *
from django.contrib import admin



class TextosAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Terminos y Condiciones',                {'fields': ['nombre','termino_condicion','categoria']}),
        ]


admin.site.register(Texto,TextosAdmin)
admin.site.register(Categoria)