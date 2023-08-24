from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("usersProfile", views.usersProfile, name = 'usersProfile'),
    path("basicQuestion", views.basicQuestions, name = 'basicQuestions'),
    path("diccionario", views.diccionario, name = 'diccionario'),
    path("verDatos", views.verDatos, name = 'verDatos')
]