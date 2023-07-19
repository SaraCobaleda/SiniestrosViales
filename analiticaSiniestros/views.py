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

    df = pd.DataFrame({'Fecha': fechaHora, 'Valor': gravedad})
    fig = px.line(df, x='Fecha', y='Valor')
    plot_div = fig.to_html(full_html=False, include_plotlyjs=True)

    datos  = Siniestro.objects.all()
    print(datos)
    return render(request, 'index.html', {'plot_div': plot_div})