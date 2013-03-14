# -*- coding: utf-8 -*-
# Create your views here.
#!/usr/bin/env python
# -*- coding: utf8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader, Context
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from contenidos.settings import MEDIA_ROOT

from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str, smart_unicode

from contenidos.modulos.productos.models import *

def productos(request):

    categorias = Categoria.objects.filter(padre=None)
    products = Productos.objects.all()

    template = "productos/productos.html"
    data = {
        'products': products,
        'categorias': categorias
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

def detalle_producto(request,slug):
    categorias = Categoria.objects.filter(padre=None)
    products = get_object_or_404(Productos, url=slug)

    template = "productos/detalle_productos.html"
    data = {
        'producto' : products,
        'categorias' : categorias
    }
    return render_to_response(template, data, context_instance=RequestContext(request))

def productos_categoria (request,slug):
    categorias = Categoria.objects.filter(padre=None)
    categoria = Categoria.objects.get(url=slug)
    products = Productos.objects.filter(categoria=categoria)

    template = "productos/categoria_productos.html"
    data = {
        'products' : products,
        'categorias' : categorias
    }
    return render_to_response(template, data, context_instance=RequestContext(request))