import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

siniestros = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="SINIESTROS")
actorVial = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="ACTOR_VIAL")
vehiculos = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="VEHICULOS")
hipotesis = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="HIPOTESIS")
diccionario = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="DICCIONARIO")

historico = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\historico_siniestros_bogota_d.c_-.csv")

#DIAGNOSTICO

#Left Join
df = pd.merge(siniestros, actorVial, on='CODIGO_ACCIDENTE', how='left')
df = pd.merge(df, vehiculos, on='CODIGO_ACCIDENTE', how='left')
df = pd.merge(df, hipotesis, on='CODIGO_ACCIDENTE', how='left')

columnas  = (['CODIGO_ACCIDENTE', 'FECHA_x', 'HORA', 'GRAVEDAD', 'CLASE_SINIESTRO', 'CHOQUE',
              'OBJETO_FIJO', 'DIRECCION', 'CODIGO_LOCALIDAD', 'DISENO_LUGAR',
              'CODIGO_ACCIDENTADO', 'FECHA_y', 'CONDICION', 'ESTADO', 'EDAD', 'SEXO',
              'VEHICULO_x', 'FECHA_z', 'VEHICULO_y', 'CLASE_VEHICULO', 'SERVICIO',
              'MODALIDAD', 'ENFUGA', 'FECHA_q', 'CODIGO_CAUSA'])

df.columns = columnas

for i in range(df.shape[1]):
    print(columnas[i], ": ", df[columnas[i]].value_counts())

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)

# Cuantos Valores Duplicados hay
duplicate_rows = df[df.duplicated()]
print(duplicate_rows)

# Eliminar Duplicados
df.drop_duplicates(inplace=True)

#comparar similitud de dos columnas y Calcular la correlación de Pearson en una muestra de los datos
muestra = df.sample(1000)

# Función para convertir fechas en valores numéricos
def fecha_a_ordinal(fecha):
    if pd.isnull(fecha):
        return np.nan
    else:
        return fecha.toordinal()
    
#comparando similitud de columnas de fechas

muestra['FECHA_x'] = pd.to_datetime(muestra['FECHA_x'])
muestra['FECHA_y'] = pd.to_datetime(muestra['FECHA_y'])
muestra['FECHA_q'] = pd.to_datetime(muestra['FECHA_q'])
muestra['FECHA_z'] = pd.to_datetime(muestra['FECHA_z'])

muestra['FECHA_x'] = muestra['FECHA_x'].map(fecha_a_ordinal)
muestra['FECHA_y'] = muestra['FECHA_y'].map(fecha_a_ordinal)
muestra['FECHA_q'] = muestra['FECHA_q'].map(fecha_a_ordinal)
muestra['FECHA_z'] = muestra['FECHA_z'].map(fecha_a_ordinal)

correlacion = muestra['FECHA_x'].corr(muestra['FECHA_y'])
porcentaje_similitud = abs(correlacion) * 100
print("Porcentaje de similitud FECHA_x y FECHA_y:", porcentaje_similitud)

correlacion = muestra['FECHA_x'].corr(muestra['FECHA_q'])
porcentaje_similitud = abs(correlacion) * 100
print("Porcentaje de similitud FECHA_x y FECHA_q:", porcentaje_similitud)

correlacion = muestra['FECHA_x'].corr(muestra['FECHA_z'])
porcentaje_similitud = abs(correlacion) * 100
print("Porcentaje de similitud FECHA_x y FECHA_z:", porcentaje_similitud)

#comparando la similitud de las columnas vehiculo con el coheficiente de Spearman 

correlacion_spearman = muestra['VEHICULO_x'].astype('category').cat.codes.corr(muestra['VEHICULO_y'].astype('category').cat.codes, method='spearman')
correlacion_spearman = abs(correlacion_spearman) * 100
print("Coeficiente de correlación de Spearman:", correlacion_spearman)

#eliminar columnas innecesarias o duplicadas
df = df.drop('OBJETO_FIJO', axis=1)
df = df.drop('MODALIDAD', axis=1)
df = df.drop('FECHA_y', axis=1)
df = df.drop('FECHA_z', axis=1)
df = df.drop('FECHA_q', axis=1)
df = df.drop('VEHICULO_x', axis=1)
df = df.drop('VEHICULO_y', axis=1)
df = df.drop('CODIGO_ACCIDENTADO', axis=1)
df = df.drop('DIRECCION', axis=1)
df = df.drop('CODIGO_ACCIDENTE', axis=1)

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)

for i in range(df.shape[1]):
    print(df.columns[i], ": ", df[df.columns[i]].value_counts())

#CONVERTIR LOS DATOS A DATOS NUMERICOS

#columna de CONDICION
print(df["CONDICION"].value_counts())
mapeo = {'CONDUCTOR': 1, 'MOTOCICLISTA': 2, 'PASAJERO/ACOMPAÑANTE': 3, 'PEATON': 4, 'CICLISTA':5}

df['CONDICION'] = df['CONDICION'].replace(mapeo)
df['CONDICION'] = df['CONDICION'].fillna(0)

print(df['CONDICION'].isnull().sum())
print(df['CONDICION'].value_counts())

#columna de ESTADO
print(df["ESTADO"].value_counts())
mapeo = {'ILESO': 1, 'HERIDO': 2, 'MUERTO': 3}

df['ESTADO'] = df['ESTADO'].replace(mapeo)
df['ESTADO'] = df['ESTADO'].fillna(0)

print(df['ESTADO'].isnull().sum())
print(df['ESTADO'].value_counts())

#columna de SEXO
print(df["SEXO"].value_counts())
mapeo = {'MASCULINO': 1, 'FEMENINO': 2, 'SIN INFORMACION': 0}

df['SEXO'] = df['SEXO'].replace(mapeo)
df['SEXO'] = df['SEXO'].fillna(0)

print(df['SEXO'].isnull().sum())
print(df['SEXO'].value_counts())

#columna de ENFUGA
print(df["ENFUGA"].value_counts())
mapeo = {'N': 1, 'S': 2}

df['ENFUGA'] = df['ENFUGA'].replace(mapeo)
df['ENFUGA'] = df['ENFUGA'].fillna(0)

print(df['ENFUGA'].isnull().sum())
print(df['ENFUGA'].value_counts())

#FECHA_x
df['FECHA_x'] = pd.to_datetime(df['FECHA_x'])
df['FECHA_x'] = df['FECHA_x'].map(fecha_a_ordinal)
print(df['FECHA_x'].isnull().sum())
print(df['FECHA_x'].value_counts())

#HORA
df['HORA'] = pd.to_timedelta(df['HORA']).dt.total_seconds().astype(int)
print(df['HORA'].isnull().sum())
print(df['HORA'].value_counts())

#EDAD
print(df["EDAD"].value_counts())

df['EDAD'] = df['EDAD'].replace('SIN INFORMACION', 0)
promedio = df['EDAD'].mean(skipna=True)
df['EDAD'] = df['EDAD'].fillna(promedio)

print(df['EDAD'].isnull().sum())
print(df['EDAD'].value_counts())

#COMPLPETAR VALORES NULOS DE LAS DEMAS COLUMNAS
df['CHOQUE'] = df['CHOQUE'].fillna(0)
df['CLASE_VEHICULO'] = df['CLASE_VEHICULO'].fillna(0)
df['SERVICIO'] = df['SERVICIO'].fillna(0)
df['CODIGO_CAUSA'] = df['CODIGO_CAUSA'].fillna(0)

#comprobar valores
for i in range(df.shape[1]):
    print(df[df.columns[i]].value_counts())
    
df.to_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv", index=False)