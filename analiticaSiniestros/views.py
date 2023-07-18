from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from analiticaSiniestros.models import Siniestro, Prueba

# Create your views here.

@login_required
def index(request):
    datos  = Siniestro.objects.all()
    print(datos)
    return render(request, 'index.html', {'datos': datos})