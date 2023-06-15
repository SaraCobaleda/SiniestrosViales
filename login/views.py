from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def holaMundo(request):
    return HttpResponse("<h1>HolaMundo</h1>")

def hola(request):
    return HttpResponse("<h2>holi</h2>")