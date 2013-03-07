# Create your views here.
#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.template.loader import render_to_string
from tinymce.models import HTMLField


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

    class Meta:
        verbose_name = "Categoria Texto"
        verbose_name_plural = "Categorias Textos"

    def tiene_hijos(self):

        return len(self.__class__.objects.filter(padre=self))

    @property
    def render_subcategorias(self):
        subcategorias=self.__class__.objects.filter(padre=self)

        data={
            'padre':self,
            'subcategorias':subcategorias
        }
        return render_to_string('textos/subcategorias.html', data)

class Texto(Maestra):

    termino_condicion = HTMLField()
    categoria = models.ForeignKey('Categoria')
    class Meta:
        verbose_name = "Termino y condicion"
        verbose_name_plural = "Terminos y Condiciones"

