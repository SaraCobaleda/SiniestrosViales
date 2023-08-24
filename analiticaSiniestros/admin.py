from django.contrib import admin
from .models import Prueba, Siniestro, Gravedad

# Register your models here.
admin.site.register(Siniestro)
admin.site.register(Prueba)
admin.site.register(Gravedad)