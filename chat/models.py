from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    ap_pat = models.CharField(max_length=100)
    ap_mat = models.CharField(max_length=100)
    usu = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.ap_pat} {self.ap_mat}'

class Mensaje(models.Model):
    txt_mensaje = models.TextField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.txt_mensaje
