from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib.auth.decorators import login_required
from contenidos.modulos.productos.views import *
urlpatterns = patterns('',
    url(r'^$', productos , name='productos'),
    url(r'^productos/categoria/(?P<slug>[-\w]+)/$', detalle_producto, name='detalle_producto'),
    url(r'^productos/(?P<slug>[-\w]+)/$', productos_categoria, name='productos_categoria'),
)
