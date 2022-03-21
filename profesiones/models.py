from django.db import models

# Create your models here.


class Licenciado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Ingeniero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)  


class Medico(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)      