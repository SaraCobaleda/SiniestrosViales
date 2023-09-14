import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")

print(df['GRAVEDAD'].describe())

leve = df['GRAVEDAD'].value_counts()[3]
medio = df['GRAVEDAD'].value_counts()[2]
grave = df['GRAVEDAD'].value_counts()[1]

        
categorias = ['Con Muertos', 'Con Heridos', 'Solo Daños']
valores = [grave, leve, medio]

plt.bar(categorias, valores)

# Agregar etiquetas y título
plt.xlabel('GRAVEDAD')
plt.ylabel('Valores')
plt.title('Gráfico de Gravedad')

plt.show()
