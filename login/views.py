from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = "Aplicacion en django!!"
    #return HttpResponse("<h1>index page</h1>")
    return render(request, 'index.html', {'title': title})

def holaMundo(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

def hola(request):
    creator = "ME!"
    #return HttpResponse("<h2>holi</h2>")
    return render(request, 'about.html', {'creator': creator})

def projects(request):
    projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def task(request):
    #task = get_object_or_404(Project, id=id)
    #return HttpResponse("Project: %s" % task.name)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def createTask(request):
    if request.method == 'GET':
        return render(request, 'tasks/createTask.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id=2)
        return redirect('tasks')
    
def createProject(request):
    if request.method == 'GET':
        return render(request, 'projects/createProject.html', {
            'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')