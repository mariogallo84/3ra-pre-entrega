from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def inicio(request):
    return render( request, "padre.html")

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre, camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request , "alumnos.html")
