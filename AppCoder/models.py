from django.db import models

# Create your models here.

#esto traerá un montón de funcionalidad, es una clase padre
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    #esto generará una tabla con 3 columnas: ID (que viene por defecto), Nombre y Camada

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    matricula = models.IntegerField()