from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_alumno", views.alumno_formulario),
    path("buscar_alumno", views.buscar_alumno),
    path("alta_profesor", views.profesor_formulario),
    path("buscar_profesor", views.buscar_profesor),
    path("buscar", views.buscar)

   
]