from django.db import models

# Create your models here.


class Licenciado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()

class Ingeniero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)  