from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

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
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar , name="editar_curso"),
    path("login", views.login_request , name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil", views.editarPerfil , name="EditarPerfil")
   
]