import pandas as pd
import numpy as np
from sklearn.metrics import jaccard_score

siniestros = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="SINIESTROS")
actorVial = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="ACTOR_VIAL")
vehiculos = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="VEHICULOS")
hipotesis = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="HIPOTESIS")
diccionario = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="DICCIONARIO")

historico = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\historico_siniestros_bogota_d.c_-.csv")

#DIAGNOSTICO

#Left Join
accidentes = pd.merge(siniestros, actorVial, on='CODIGO_ACCIDENTE', how='left')
accidentes = pd.merge(accidentes, vehiculos, on='CODIGO_ACCIDENTE', how='left')
accidentes = pd.merge(accidentes, hipotesis, on='CODIGO_ACCIDENTE', how='left')

columnas  = (['CODIGO_ACCIDENTE', 'FECHA_x', 'HORA', 'GRAVEDAD', 'CLASE_x', 'CHOQUE',
              'OBJETO_FIJO', 'DIRECCION', 'CODIGO_LOCALIDAD', 'DISENO_LUGAR',
              'CODIGO_ACCIDENTADO', 'FECHA_y', 'CONDICION', 'ESTADO', 'EDAD', 'SEXO',
              'VEHICULO_x', 'FECHA_z', 'VEHICULO_y', 'CLASE_y', 'SERVICIO',
              'MODALIDAD', 'ENFUGA', 'FECHA_q', 'CODIGO_CAUSA'])

accidentes.columns = columnas

for i in range(accidentes.shape[1]):
    print(columnas[i], ": ", accidentes[columnas[i]].value_counts())

for i in range(accidentes.shape[1]):
    print(columnas[i], ": ", accidentes[columnas[i]].isna().sum())

#Comparar la relacion entre colimnas
conjunto1 = set(accidentes['FECHA_x'])
conjunto2 = set(accidentes['FECHA_y'])

coeficiente_jaccard = jaccard_score(conjunto1, conjunto2) * 100
print("Porcentaje de similitud:", coeficiente_jaccard)

correlacion = accidentes['FECHA_x'].corr(accidentes['FECHA_y'])
porcentaje_similitud = abs(correlacion) * 100
print("Porcentaje de similitud:", porcentaje_similitud)