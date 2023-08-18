import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")

x = df['FECHA_HORA']
y = df['GRAVEDAD']

plt.scatter(x, y, color='blue', label='Datos de ejemplo')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfica de Dispersión')

plt.legend()

plt.show()
