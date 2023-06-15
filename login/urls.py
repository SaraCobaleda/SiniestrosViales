from django.urls import path
from . import views

urlpatterns = [
    path("", views.holaMundo),
    path("about/", views.hola)
]