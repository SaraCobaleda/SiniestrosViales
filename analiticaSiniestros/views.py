from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import plotly.graph_objects as go
import plotly.express as px

from analiticaSiniestros.models import Siniestro, Prueba

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

    claseSiniestro = [registro.claseSiniestro for registro in registros_mas_recientes]
    claseSiniestro = np.array(list(claseSiniestro))

    choque = [registro.choque for registro in registros_mas_recientes]
    choque = np.array(list(claseSiniestro))

    codigoLocalidad = [registro.codigoLocalidad for registro in registros_mas_recientes]
    codigoLocalidad = np.array(list(claseSiniestro))

    disenoLugar = [registro.disenoLugar for registro in registros_mas_recientes]
    disenoLugar = np.array(list(claseSiniestro))

    condicion = [registro.condicion for registro in registros_mas_recientes]
    condicion = np.array(list(claseSiniestro))

    estado = [registro.estado for registro in registros_mas_recientes]
    estado = np.array(list(claseSiniestro))

    edad = [registro.edad for registro in registros_mas_recientes]
    edad = np.array(list(claseSiniestro))

    sexo = [registro.sexo for registro in registros_mas_recientes]
    sexo = np.array(list(claseSiniestro))

    claseVehiculo = [registro.claseVehiculo for registro in registros_mas_recientes]
    claseVehiculo = np.array(list(claseSiniestro))

    servicio = [registro.servicio for registro in registros_mas_recientes]
    servicio = np.array(list(claseSiniestro))

    enfuga = [registro.enfuga for registro in registros_mas_recientes]
    enfuga = np.array(list(claseSiniestro))

    codigoCausa = [registro.codigoCausa for registro in registros_mas_recientes]
    codigoCausa = np.array(list(claseSiniestro))

    dfFecha = pd.DataFrame({'Fecha': fechaHora})
    df = pd.DataFrame({'Fecha': fechaHora, 'gravedad': gravedad, "choque":choque, "condicion":condicion})
    fig = px.line(df, x='Fecha', y='gravedad', markers=True)
    plot_div = fig.to_html(full_html=False, include_plotlyjs=True)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=fechaHora, y=choque ,mode='lines',name='lines'))
    fig2.add_trace(go.Scatter(x=fechaHora, y=gravedad ,mode='markers+markers',name='lines+markers'))
    fig2.add_trace(go.Scatter(x=fechaHora, y=condicion,mode='markers', name='markers'))

    plot_div2 = fig2.to_html(full_html=False, include_plotlyjs=True)

    datos  = Siniestro.objects.all()
    print(datos)
    return render(request, 'index.html', {'plot_div': plot_div, 'plot_div2': plot_div2})

@login_required
def usersProfile(request):
     return render(request, 'users-profile.html')

@login_required
def basicQuestions(request):
     print("basicQuestions")
     return render(request, 'pages-faq.html')