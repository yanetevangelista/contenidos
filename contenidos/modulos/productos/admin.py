__author__ = 'Beren'
from contenidos.modulos.productos.models import *
from django.contrib import admin


class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

class ProductosAdmin(admin.ModelAdmin):
    fieldsets = [
                    ('Detalles Principales',                {'fields': ['id_interno','nombre','anno','marca','precio','motor','caja','categoria']}),
                    ('Detalles Secundarios',                {'fields': ['combustible','traccion','kilometraje','cilindraje','puestos','puertas','color','descripcion']}),
                    ('Dimensiones',                         {'fields': ['alto','largo','ancho','distancia_ejes']}),
                    ('Otros',                               {'fields': ['url','activo'],'classes': ['collapse', 'extrapretty']}),
                ]

    inlines = [ImagenProductoInline]
    list_display = ('id','id_interno','nombre','activo','url')

class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Detalles Principales',                {'fields': ['nombre','descripcion','padre']}),
        ('Otros',                               {'fields': ['url','activo'],'classes': ['collapse', 'extrapretty']}),
        ]
    prepopulated_fields = {'url': ['nombre']}


admin.site.register(Productos,ProductosAdmin)
admin.site.register(Categoria)