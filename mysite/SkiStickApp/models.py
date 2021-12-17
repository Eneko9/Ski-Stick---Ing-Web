from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.  
class Localizacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300,blank=True,null=True)
    def __str__(self):
        return self.nombre

class Pista(models.Model):
    color_tipo = models.CharField(max_length=30)
    def __str__(self):
        return self.color_tipo

class Estacion(models.Model):
    nombre = models.CharField(max_length=30)
    puntos_alquiler = models.IntegerField(default=0)
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)
    pista = models.ManyToManyField(Pista)   
    def __str__(self):
        return self.nombre

class Opinion(models.Model):

    nombre_usu = models.CharField(max_length=30)
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    valoracion = models.IntegerField(default = 1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    opinion = models.TextField(max_length=200)
    def __str__(self):
        return self.nombre_usu

