__author__ = 'Beren'
from contenidos.modulos.contactos.models import *
from django.contrib import admin


class Enviar_aAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Enviar A',                {'fields': ['nombre','email']}),
        ]


admin.site.register(Contactos)
admin.site.register(Mensajes)
