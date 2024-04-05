from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario

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

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"], camada=datos["camada"] )
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse ("Ingrese el nombre del curso")


#**************Alumnos



def alumnos(request):
    return render(request , "alumnos.html")

def alta_alumno(request,nombre):
    alumno = Alumno(nombre=nombre, legajo=234512)
    alumno.save()
    texto = f"Se guardo en la BD el alumno: {alumno.nombre} {alumno.legajo}"
    return HttpResponse(texto)

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=datos["nombre"], legajo=datos["legajo"] )
            alumno.save()
            return render(request , "formulario_alumnos.html")

    return render(request , "formulario_alumnos.html")

def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscar_alumnos(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        return render( request , "resultado_busqueda_alumnos.html" , {"alumnos": alumnos})
    else:
        return HttpResponse ("Ingrese el nombre del alumno")


#*************Profesores

def Profesores(request):
    return render(request , "profesores.html")

def alta_profesor(request,nombre):
    profesor = Profesor(nombre=nombre, matricula=1105)
    profesor.save()
    texto = f"Se guardo en la BD el profesor: {profesor.nombre} {profesor.legajo}"
    return HttpResponse(texto)

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=datos["nombre"], matricula=datos["matricula"] )
            profesor.save()
            return render(request , "formulario_profesores.html")

    return render(request , "formulario_profesores.html")

def buscar_profesor(request):
    return render(request, "buscar_profesor.html")

def buscar_profesores(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesor.objects.filter(nombre__icontains=nombre)
        return render( request , "resultado_busqueda_profesores.html" , {"profesores": profesores})
    else:
        return HttpResponse ("Ingrese el nombre del profesor")