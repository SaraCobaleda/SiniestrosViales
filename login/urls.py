from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("about/", views.hola),
    path("hello/<str:username>", views.holaMundo)
]