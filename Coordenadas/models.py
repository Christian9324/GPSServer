from django.db import models

# Create your models here.
class Ruta(models.Model):
    idPunto =  models.AutoField(primary_key=True)
    idUser = models.PositiveIntegerField(null=False)
    latitud = models.FloatField(null=False)
    longitud = models.FloatField(null=False)
    hora = models.DateField(auto_now=True)