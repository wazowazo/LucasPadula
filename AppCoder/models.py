from django.db import models

class Familia(models.Model):
    fecha_ingreso = models.DateField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()



