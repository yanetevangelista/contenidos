# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from contenidos.modulos.contactos.models import *

def contactos(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactosForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            enviar_a=Enviar_a.objects.filter(activo=True)
            nuevo_contacto=form.save()
            for correo in enviar_a:
                nuevo_contacto.enviar_a.add(correo)
            nuevo_contacto.save()
            nuevo_contacto.enviar_emails()
            return HttpResponseRedirect('/contactos') # Redirect after POST
    else:
        form = ContactosForm() # An unbound form

    return render(request, 'contactos/contactos.html', {
        'form': form,
        })