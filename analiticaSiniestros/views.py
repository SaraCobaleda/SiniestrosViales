from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from django.utils import timezone

from analiticaSiniestros.models import *

import numpy as np
import pandas as pd

# Create your views here.


@login_required
def index(request):
    registros_mas_recientes = Siniestro.objects.order_by('-fechaHora')[:100]

    fechaHora = [registro.fechaHora for registro in registros_mas_recientes]
    fechaHora = np.array(list(fechaHora))

    gravedad = [registro.gravedad for registro in registros_mas_recientes]
    gravedad = np.array(list(gravedad))

    claseSiniestro = [
        registro.claseSiniestro for registro in registros_mas_recientes]
    claseSiniestro = np.array(list(claseSiniestro))

    choque = [registro.choque for registro in registros_mas_recientes]
    choque = np.array(list(claseSiniestro))

    codigoLocalidad = [
        registro.codigoLocalidad for registro in registros_mas_recientes]
    codigoLocalidad = np.array(list(claseSiniestro))

    disenoLugar = [
        registro.disenoLugar for registro in registros_mas_recientes]
    disenoLugar = np.array(list(claseSiniestro))

    condicion = [registro.condicion for registro in registros_mas_recientes]
    condicion = np.array(list(claseSiniestro))

    estado = [registro.estado for registro in registros_mas_recientes]
    estado = np.array(list(claseSiniestro))

    edad = [registro.edad for registro in registros_mas_recientes]
    edad = np.array(list(claseSiniestro))

    sexo = [registro.sexo for registro in registros_mas_recientes]
    sexo = np.array(list(claseSiniestro))

    claseVehiculo = [
        registro.claseVehiculo for registro in registros_mas_recientes]
    claseVehiculo = np.array(list(claseSiniestro))

    servicio = [registro.servicio for registro in registros_mas_recientes]
    servicio = np.array(list(claseSiniestro))

    enfuga = [registro.enfuga for registro in registros_mas_recientes]
    enfuga = np.array(list(claseSiniestro))

    codigoCausa = [
        registro.codigoCausa for registro in registros_mas_recientes]
    codigoCausa = np.array(list(claseSiniestro))

    df = pd.DataFrame({'Fecha': fechaHora, 'gravedad': gravedad,
                      "choque": choque, "condicion": condicion})

    fig = px.scatter(df, x='Fecha', y='gravedad')
    plot_div = fig.to_html(full_html=False, include_plotlyjs=True)

    fig2 = px.scatter(df, x='Fecha', y='choque')
    plot_div2 = fig2.to_html(full_html=False, include_plotlyjs=True)

    hombre = 0
    mujer = 0

    for genero in sexo:
        if genero > 0:
            hombre = hombre + 1
        else:
            mujer = mujer + 1

    datos_pastel = {"Hombres": hombre, "Mujeres": mujer}

    piefig = px.pie(values=list(datos_pastel.values()),
                    names=list(datos_pastel.keys()))
    plot_div3 = piefig.to_html(full_html=False, include_plotlyjs=True)

    fig4 = px.scatter(df, x='Fecha', y='condicion')
    plot_div4 = fig2.to_html(full_html=False, include_plotlyjs=True)

    datos = Siniestro.objects.all()
    print(datos)
    return render(request, 'index.html', {'plot_div': plot_div,
                                          'plot_div2': plot_div2,
                                          'plot_div3': plot_div3,
                                          'plot_div4': plot_div4})


@login_required
def diccionario(request):
    gravedades = Gravedad.objects.all()
    claseSinisestro = ClaseSiniestro.objects.all()
    choque = Choque.objects.all()
    codigoLocalidad = CodigoLocalidad.objects.all()
    disenoLugar = DisenoLugar.objects.all()
    condicion = Condicion.objects.all()
    estado = Estado.objects.all()
    edad = Siniestro.objects.values_list('edad', flat=True).distinct()
    sexo = Sexo.objects.all()
    claseVehiculo = ClaseVehiculo.objects.all()
    servicio = Servicio.objects.all()
    enfuga = Enfuga.objects.all()
    codigoCausa = CodigoCausa.objects.all()
    return render(request, 'diccionario.html', {'gravedades': gravedades,
                                                'claseSiniestros': claseSinisestro,
                                                'choques': choque,
                                                'codigoLocalidades': codigoLocalidad,
                                                'disenoLugares': disenoLugar,
                                                'condiciones': condicion,
                                                'estados': estado,
                                                'edades': edad,
                                                'sexos': sexo,
                                                'claseVehiculos': claseVehiculo,
                                                'servicios': servicio,
                                                'enfugas': enfuga,
                                                'codigoCausas': codigoCausa})


@login_required
def verDatos(request):
    siniestro = Siniestro.objects.all()
    return render(request, 'ver-datos.html', {'siniestros': siniestro})


@login_required
def usersProfile(request):
    return render(request, 'users-profile.html')


@login_required
def basicQuestions(request):
    return render(request, 'pages-faq.html')


@login_required
def crearDatos(request):
    gravedad = Gravedad.objects.all()
    claseSinisestro = ClaseSiniestro.objects.all()
    choque = Choque.objects.all()
    codigoLocalidad = CodigoLocalidad.objects.all()
    disenoLugar = DisenoLugar.objects.all()
    condicion = Condicion.objects.all()
    estado = Estado.objects.all()
    sexo = Sexo.objects.all()
    claseVehiculo = ClaseVehiculo.objects.all()
    servicio = Servicio.objects.all()
    enfuga = Enfuga.objects.all()
    codigoCausa = CodigoCausa.objects.all()

    if request.method == 'POST':
        gravedadDato = request.POST.get('gravedadDato')
        claseSinisestroDato = request.POST.get('claseSinisestroDato')
        choqueDato = request.POST.get('choqueDato')
        codigoLocalidadDato = request.POST.get('codigoLocalidadDato')
        disenoLugarDato = request.POST.get('disenoLugarDato')
        condicionDato = request.POST.get('condicionDato')
        estadoDato = request.POST.get('estadoDato')
        edadDato = request.POST.get('edadDato')
        sexoDato = request.POST.get('sexoDato')
        claseVehiculoDato = request.POST.get('claseVehiculoDato')
        servicioDato = request.POST.get('servicioDato')
        enfugaDato = request.POST.get('enfugaDato')
        codigoCausaDato = request.POST.get('codigoCausaDato')
        fechaDato = request.POST.get('fechaDato')
        horaDato = request.POST.get('horaDato')
        fecha = datetime.strptime(fechaDato, "%Y-%m-%d")
        hora = datetime.strptime(horaDato, "%H:%M")
        fecha_hora = datetime.combine(fecha.date(), hora.time())
        fecha_hora = timezone.make_aware(fecha_hora,  timezone=timezone.get_current_timezone())


        siniestro = Siniestro(gravedad = gravedadDato, 
                              claseSiniestro = claseSinisestroDato, 
                              choque = choqueDato, 
                              codigoLocalidad = codigoLocalidadDato,
                              disenoLugar = disenoLugarDato,
                              condicion = condicionDato,
                              estado = estadoDato,
                              edad = edadDato,
                              sexo = sexoDato,
                              claseVehiculo = claseVehiculoDato,
                              servicio = servicioDato,
                              enfuga = enfugaDato,
                              codigoCausa = codigoCausaDato,
                              fechaHora = fecha_hora)
        siniestro.save()

        return render(request, 'crear-datos.html', {'gravedades': gravedad,
                                                    'claseSiniestros': claseSinisestro,
                                                    'choques': choque,
                                                    'codigoLocalidades': codigoLocalidad,
                                                    'disenoLugares': disenoLugar,
                                                    'condiciones': condicion,
                                                    'estados': estado,
                                                    'sexos': sexo,
                                                    'claseVehiculos': claseVehiculo,
                                                    'servicios': servicio,
                                                    'enfugas': enfuga,
                                                    'codigoCausas': codigoCausa})

    else:
        return render(request, 'crear-datos.html', {'gravedades': gravedad,
                                                    'claseSiniestros': claseSinisestro,
                                                    'choques': choque,
                                                    'codigoLocalidades': codigoLocalidad,
                                                    'disenoLugares': disenoLugar,
                                                    'condiciones': condicion,
                                                    'estados': estado,
                                                    'sexos': sexo,
                                                    'claseVehiculos': claseVehiculo,
                                                    'servicios': servicio,
                                                    'enfugas': enfuga,
                                                    'codigoCausas': codigoCausa})


@login_required
def modificarDatos(request):
    return render(request, 'actualizar-datos.html')


@login_required
def eliminarDatos(request):
    return render(request, 'borrar-datos.html')
