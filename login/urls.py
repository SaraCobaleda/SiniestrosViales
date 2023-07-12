from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("about/", views.hola, name = 'about'),
    path("hello/<str:username>", views.holaMundo, name = 'hello'),
    path("projects/", views.projects, name = 'projects'),
    path("tasks/", views.task, name = 'tasks'),
    path("createTask/", views.createTask, name = 'create_task'),
    path("createProject/", views.createProject, name = 'create_project'),
]