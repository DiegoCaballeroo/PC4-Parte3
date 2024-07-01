from django.db import models

class Estudiante(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=100)
    apemat = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    estado = models.BooleanField(default=True)
