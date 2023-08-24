import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")

gravedad = df['GRAVEDAD']

NI = 0
leve = 0
medio = 0
grave = 0

for i in gravedad:
    if i == 0:
        NI = NI + 1
    elif i == 1:
        grave = grave + 1
    elif i == 2:
        medio = medio + 1
    else:
        leve = leve + 1
        
categorias = ['Con Muertos', 'Con Heridos', 'Solo Daños']
valores = [grave, leve, medio]

plt.bar(categorias, valores)

# Agregar etiquetas y título
plt.xlabel('GRAVEDAD')
plt.ylabel('Valores')
plt.title('Gráfico de Gravedad')

plt.show()
