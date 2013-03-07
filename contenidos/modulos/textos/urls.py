from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import databrowse
from django.contrib.auth.decorators import login_required
from contenidos.modulos.textos.views import *
urlpatterns = patterns('',
    url(r'^$', textos , name='textos'),
)
