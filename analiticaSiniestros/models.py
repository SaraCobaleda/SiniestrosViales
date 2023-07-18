from django.db import models

# Create your models here.

class Siniestro(models.Model):
    gravedad = models.FloatField()
    claseSiniestro = models.FloatField()
    choque = models.FloatField()
    codigoLocalidad = models.FloatField()
    disenoLugar = models.FloatField()
    condicion = models.FloatField()
    estado = models.FloatField()
    edad = models.FloatField()
    sexo = models.FloatField()
    claseVehiculo = models.FloatField()
    servicio = models.FloatField()
    enfuga = models.FloatField()
    codigoCausa = models.FloatField()
    fechaHora = models.DateTimeField()
    def __str__(self):
        return str(self.pk)
    
class Prueba(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

