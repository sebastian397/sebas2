from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bienvenida.html')

from django.shortcuts import render
from .models import Mensaje

def mensajes(request):
    mensajes = Mensaje.objects.all().order_by('id')
    return render(request, 'mensajes.html', {'mensajes': mensajes})
