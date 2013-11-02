__author__ = 'Beren'
from contenidos.modulos.contactos.models import *
from django.contrib import admin


class Enviar_aAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Enviar A',                {'fields': ['nombre','email']}),
        ]

class ContactosAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')

admin.site.register(Contactos,ContactosAdmin)
admin.site.register(Mensajes)
admin.site.register(Newsletter)


