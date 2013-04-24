#!/usr/bin/env python
# -*- coding: utf8 -*-

from django.db import models
from django.forms import ModelForm
from django.core.mail import send_mail
from contenidos.settings import DEFAULT_FROM_EMAIL

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


class Enviar_a (Maestra):

    email = models.EmailField(verbose_name="Enviar Contactos A",max_length=70,blank=True,null=True)
    class Meta:
        verbose_name = "Correo de recepcion"
        verbose_name_plural = "Correos de Recepcion"

class Contactos (Maestra):

    email = models.EmailField(verbose_name="Email",max_length=70)
    mensaje = models.TextField(blank=True,null=True)

    organizacion = models.CharField(verbose_name="Organizacion",max_length=100,null=True,blank=True)
    posicion = models.CharField(verbose_name="Posicion en la Organizacion",max_length=100,null=True,blank=True)

    enviar_a = models.ManyToManyField(Enviar_a)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def enviar_emails(self):
        enviar=[]
        for contacto in self.enviar_a.all():
            enviar += [contacto.email]
        send_mail('Nuevo contacto '+self.nombre, self.mensaje+" Email del Contacto: "+self.email, DEFAULT_FROM_EMAIL, enviar, fail_silently=False)





##contactosform
class ContactosForm(ModelForm):
    class Meta:
        model = Contactos
        fields = ['email','nombre','organizacion','posicion','mensaje']

