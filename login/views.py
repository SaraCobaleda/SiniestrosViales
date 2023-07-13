from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()
            return render(request, 'login.html', {'message': 'User created successfully'})
        except:
            return render(request, 'register.html', {'error': 'User could not be created'})
        
def login(request):
    return render(request, 'login.html')    

#falta arreglar

def index(request):
    title = "Aplicacion en django!!"
    #return HttpResponse("<h1>index page</h1>")
    return render(request, 'index.html', {'title': title})

def holaMundo(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

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