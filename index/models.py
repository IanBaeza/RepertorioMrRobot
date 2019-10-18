from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Gabinete(models.Model):
    modelogabinete=models.CharField(max_length=30)
    tamanogabinete=models.CharField(max_length=5)
    marcagabinete=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.modelogabinete},{self.tamanogabinete},{self.marcagabinete}'

class Fuente(models.Model):
    modelofuente=models.CharField(max_length=30)
    marcafuente=models.CharField(max_length=30)
    wattsfuente=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.modelofuente},{self.marcafuente},{self.wattsfuente}'

class PlacaMadre(models.Model):
    marcaplaca=models.CharField(max_length=30)
    modeloplaca=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.marcaplaca},{self.modeloplaca}'

class Ram(models.Model):
    marcaram=models.CharField(max_length=30)
    modeloram=models.CharField(max_length=30)
    memoriaram=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.marcaram},{self.modeloram},{self.memoriaram}'

class Procesador(models.Model):
    generacionproce=models.CharField(max_length=30)
    modeloproce=models.CharField(max_length=30)
    marcaproce=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.generacionproce},{self.modeloproce},{self.marcaproce}'

class TarjetaVideo(models.Model):
    modelovideo=models.CharField(max_length=30)
    marcavideo=models.CharField(max_length=30)
    generacionvideo=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.modelovideo},{self.marcavideo},{self.generacionvideo}'


class Almacenamiento(models.Model):
    modeloalma=models.CharField(max_length=30)
    capacidadalma=models.CharField(max_length=10)
    tipoalma=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.modeloalma},{self.capacidadalma},{self.tipoalma}'

class Computador(models.Model):
    Gabinete=models.ForeignKey('Gabinete',on_delete=models.SET_NULL, null=True)
    Fuente=models.ForeignKey('Fuente',on_delete=models.SET_NULL, null=True)
    PlacaMadre=models.ForeignKey('PlacaMadre',on_delete=models.SET_NULL, null=True)
    Ram=models.ForeignKey('Ram',on_delete=models.SET_NULL, null=True)
    Procesador=models.ForeignKey('Procesador',on_delete=models.SET_NULL, null=True)
    TarjetaVideo=models.ForeignKey('TarjetaVideo',on_delete=models.SET_NULL, null=True)
    Almacenamiento=models.ForeignKey('Almacenamiento',on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return f'{self.Gabinete},{self.Fuente},{self.PlacaMadre},{self.Ram},{self.Procesador},{self.TarjetaVideo},{self.Almacenamiento}'