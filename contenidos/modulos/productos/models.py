#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.template.loader import render_to_string

from sorl.thumbnail import ImageField,get_thumbnail

# Create your models here.


class Maestra(models.Model):
    nombre=models.CharField(max_length=100,null=False)
    descripcion = models.TextField(blank=True,null=True)
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now=True)
    activo=models.BooleanField(db_index=True,default=True)
    class Meta:
        ordering = ["nombre",'modificado']
        abstract = True
    def __unicode__(self):
        return u'%s' % (self.nombre)


class Categoria(Maestra):
    padre = models.ForeignKey('Categoria',blank=True,null=True)
    url=models.SlugField(max_length=100,verbose_name="Url")

    class Meta:
        verbose_name = "Categoria Auto"
        verbose_name_plural = "Categoria Autos"


    def tiene_hijos(self):

        return len(self.__class__.objects.filter(padre=self))

    @property
    def render_subcategorias(self):
        subcategorias=self.__class__.objects.filter(padre=self)

        data={
            'padre':self,
            'subcategorias':subcategorias
        }
        return render_to_string('productos/subcategorias.html', data)



class Productos (Maestra):

    id_interno = models.IntegerField(verbose_name="Numeracion Interna",default=0)
    anno = models.IntegerField(verbose_name="Año del Modelo",default=0)
    motor = models.CharField(verbose_name="Tipo de Motor",max_length=100,null=True,blank=True)
    combustible = models.CharField(verbose_name="Combustible Usado",max_length=100,null=True,blank=True)
    caja = models.CharField(verbose_name="Tipo de Caja", max_length=100,null=True,blank=True)
    traccion = models.CharField(verbose_name="Traccion", max_length=100,null=True,blank=True)
    color = models.CharField(verbose_name="Color", max_length=100,null=True,blank=True)
    puertas = models.IntegerField(verbose_name="Numero de Puertas",default=0,null=True,blank=True)
    puestos = models.IntegerField(verbose_name="Numero de Puestos",default=0,null=True,blank=True)
    largo = models.FloatField(verbose_name="Largo",default=0,null=True,blank=True)
    alto = models.FloatField(verbose_name="Alto",default=0,null=True,blank=True)
    ancho = models.FloatField(verbose_name="Ancho",default=0,null=True,blank=True)
    distancia_ejes = models.FloatField(verbose_name="Distancia entre Ejes",default=0,null=True,blank=True)
    kilometraje =  models.FloatField(verbose_name="Kilometraje",default=0,null=True,blank=True)

    marca = models.CharField(verbose_name="Marca del Auto", max_length=100, null=True, blank=True)


    precio = models.BigIntegerField(verbose_name="Precio", default=0,null=True,blank=True)
    categoria = models.ForeignKey('Categoria')

    url=models.SlugField(max_length=100, verbose_name="Url")


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    @property
    def imagenes(self):
        return ImagenProducto.objects.filter(producto=self)

Productos._meta.get_field('nombre').verbose_name = 'Modelo'
Productos._meta.get_field('descripcion').verbose_name = 'Detalles Adicionales'

def content_image_name(instance, filename):
    filename=filename.split('.')
    filename=str(instance.producto.id)+str('.')+str(filename[-1])
    return '/'.join(['img', 'productos', instance.producto.nombre, filename])

class ImagenProducto(Maestra):
    producto = models.ForeignKey('Productos')
    image = ImageField(upload_to = content_image_name)


    class Meta:
        verbose_name = "Imagen de un Producto"
        verbose_name_plural = "Imagenes de Productos"

    def mostrar_thumb(self,x,y):
        im = get_thumbnail(self.image, '%sx%s'%(x,y), crop='center', quality=99,format='JPEG')
        return im.url

    @property
    def thumb_pag_productos(self):
        """Esta propiedad solo se muestra en la pagina de todos los productos"""
        return self.mostrar_thumb(357,250)

    @property
    def thumb_pag_detalles(self):
        """Esta propiedad solo se muestra en la pagina de detalles del producto"""
        return self.mostrar_thumb(647,487)


