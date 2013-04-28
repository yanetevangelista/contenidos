# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from contenidos.modulos.contactos.models import *
from contenidos.modulos.productos.models import Categoria

def contactos(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST': # If the form has been submitted...
        try:
            ins = Contactos.objects.get(email=request.POST['email'])
            form = ContactosForm(request.POST, instance=ins)# A form bound to the POST data
        except ObjectDoesNotExist:
            form = ContactosForm(request.POST)

        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            nuevo_contacto = form.save()
            inlineform = InlineMensajeFactory(request.POST,instance=nuevo_contacto)
            if inlineform.is_valid():
                nuevo_mensaje = inlineform.save()
                nuevo_mensaje[0].enviar_emails()
            return render(request, 'contactos/contactos.html', {
                'categorias': categorias,
                'form': form,
                'inlineform': inlineform,
                'exito': '1'
                })
        else:
            inlineform = InlineMensajeFactory(request.POST)
    else:
        form = ContactosForm() # An unbound form
        inlineform = InlineMensajeFactory()

    return render(request, 'contactos/contactos.html', {
        'categorias': categorias,
        'form': form,
        'inlineform': inlineform,
        'exito':0
        })

