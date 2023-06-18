from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>index page</h1>")

def holaMundo(request, username):
    print(username)
    return HttpResponse("<h1>Hola %s</h1>" % username)

def hola(request):
    return HttpResponse("<h2>holi</h2>")