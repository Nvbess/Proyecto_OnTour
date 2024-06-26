from django.db import models

# Create your models here.

class Tipo_Viajes(models.Model):
    nombre_viaje = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_viaje

class Contrato(models.Model):
    nombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=150)
    apmaterno = models.CharField(max_length=150)
    rut = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    tipo_viaje = models.ForeignKey(Tipo_Viajes, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
