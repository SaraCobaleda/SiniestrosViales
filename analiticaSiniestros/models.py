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
        return str(self.fechaHora)
    
class Prueba(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Gravedad(models.Model):
    idGravedad = models.IntegerField()
    DescGravedad = models.CharField(max_length=200)
    def __str__(self):
        return self.DescGravedad
    
class ClaseSiniestro(models.Model):
    idClaseSiniestro = models.IntegerField()
    DescClaseSiniestro = models.CharField(max_length=200)
    def __str__(self):
        return self.DescClaseSiniestro

class Choque(models.Model):
    idChoque = models.IntegerField()
    DescChoque = models.CharField(max_length=200)
    def __str__(self):
        return self.DescChoque

class CodigoLocalidad(models.Model):
    idCodigoLocalidad = models.IntegerField()
    DescCodigoLocalidad = models.CharField(max_length=200)
    def __str__(self):
        return self.DescCodigoLocalidad
    
class DisenoLugar(models.Model):
    idDisenoLugar = models.IntegerField()
    DescDisenoLugar = models.CharField(max_length=200)
    def __str__(self):
        return self.DescDisenoLugar
    
class Condicion(models.Model):
    idCondicion = models.IntegerField()
    DescCondicion = models.CharField(max_length=200)
    def __str__(self):
        return self.DescCondicion
    
class Estado(models.Model):
    idEstado = models.IntegerField()
    DescEstado = models.CharField(max_length=200)
    def __str__(self):
        return self.DescEstado
    
class Sexo(models.Model):
    idSexo = models.IntegerField()
    DescSexo = models.CharField(max_length=200)
    def __str__(self):
        return self.DescSexo
    
class ClaseVehiculo(models.Model):
    idClaseVehiculo = models.IntegerField()
    DescClaseVehiculo = models.CharField(max_length=200)
    def __str__(self):
        return self.DescClaseVehiculo
    
class Servicio(models.Model):
    idServicio = models.IntegerField()
    DescServicio = models.CharField(max_length=200)
    def __str__(self):
        return self.DescServicio
    
class Enfuga(models.Model):
    idEnfuga = models.IntegerField()
    DescEnfuga = models.CharField(max_length=200)
    def __str__(self):
        return self.DescEnfuga
    
class CodigoCausa(models.Model):
    idCodigoCausa = models.IntegerField()
    DescCodigoCausa = models.CharField(max_length=200)
    def __str__(self):
        return self.DescCodigoCausa