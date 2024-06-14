from django.urls import path
from .views import bienvenida, mensajes

urlpatterns = [
    path('', bienvenida, name='bienvenida'),
    path('mensajes/', mensajes, name='mensajes'),
]
