from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from contenidos.settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contenidos.views.home', name='home'),
    # url(r'^contenidos/', include('contenidos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}),


    (r'^', include('contenidos.modulos.productos.urls')),
    (r'^terminos-y-condiciones', include('contenidos.modulos.textos.urls')),
    (r'^contactos', include('contenidos.modulos.contactos.urls'))
)
