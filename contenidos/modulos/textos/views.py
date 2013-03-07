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

from contenidos.modulos.textos.models import *

def textos(request):

    categorias = Categoria.objects.filter(padre=None)
    texts = Texto.objects.filter(activo=True)

    template = "textos/terminos_y_condiciones.html"
    data = {
        'textos' : texts,
        'categorias' : categorias
    }
    return render_to_response(template, data, context_instance=RequestContext(request))