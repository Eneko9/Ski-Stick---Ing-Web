from django.db import models

# Create your models here.
class Localizacion(models.Model):

    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=30)
    puntos_alquiler = models.IntegerField(default=0)
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Pista(models.Model):
    color_tipo = models.CharField(max_length=30)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.color_tipo