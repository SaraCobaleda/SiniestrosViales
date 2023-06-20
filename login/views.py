from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("<h1>index page</h1>")

def holaMundo(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

def hola(request):
    return HttpResponse("<h2>holi</h2>")

def projects(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe = False)

def task(request, name):
    task = get_object_or_404(Project, name=name)
    return HttpResponse("task: %s" % task.id)