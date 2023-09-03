from django.db import models

class Inventario(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email= models.EmailField(null=True)

class Empleado(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email= models.EmailField(null=True)