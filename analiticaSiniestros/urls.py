from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("usersProfile", views.usersProfile, name = 'usersProfile'),
    path("basicQuestion", views.basicQuestions, name = 'basicQuestions'),
    path("diccionario", views.diccionario, name = 'diccionario'),
    path("verDatos", views.verDatos, name = 'verDatos'),
    path("crearDatos", views.crearDatos, name = 'crearDatos'),
    path("modificarDatos", views.modificarDatos, name = 'modificarDatos'),
    path("eliminarDatos", views.eliminarDatos, name = 'eliminarDatos'),
    path("modificarDatosForm", views.modificarDatosForm, name = 'modificarDatosForm')
]