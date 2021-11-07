from django.db import models

# Create your models here.
class Localizacion(models.Model):
    id = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)

class Estacion(models.Model):
    id = models.CharField(max_length=12)
    nombre = models.CharField(max_length=30)
    puntos_alquiler = models.IntegerField(default=0)
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)

class Pista(models.model):
    id = models.CharField(max_length=12)
    color_tipo = models.CharField(max_lenght=30)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)