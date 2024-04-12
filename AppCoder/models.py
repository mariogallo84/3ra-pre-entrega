from django.db import models

# Create your models here.

#esto traerá un montón de funcionalidad, es una clase padre
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"
    #esto generará una tabla con 3 columnas: ID (que viene por defecto), Nombre y Camada

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    legajo = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Legajo: {self.legajo}"
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    matricula = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Matricula: {self.matricula}"
