from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib.auth.decorators import login_required
from contenidos.modulos.contactos.views import *
urlpatterns = patterns('',
    url(r'^$', contactos , name='contactos'),
)
