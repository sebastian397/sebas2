from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Mensaje
from .models import Carrera
from .models import Persona

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'status')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ap_pat', 'ap_mat', 'usu', 'fecha_nac', 'carrera', 'status')

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('txt_mensaje', 'persona', 'status')

