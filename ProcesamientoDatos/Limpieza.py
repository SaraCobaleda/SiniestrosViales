import pandas as pd
import numpy as np

siniestros = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="SINIESTROS")
actorVial = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="ACTOR_VIAL")
vehiculos = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="VEHICULOS")
hipotesis = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="HIPOTESIS")
diccionario = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="DICCIONARIO")

historico = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\historico_siniestros_bogota_d.c_-.csv")

#DIAGNOSTICO

#Join
accidentes = pd.merge(siniestros, actorVial, on='CODIGO_ACCIDENTE', how='left')
accidentes = pd.merge(accidentes, vehiculos, on='CODIGO_ACCIDENTE', how='left')
accidentes = pd.merge(accidentes, hipotesis, on='CODIGO_ACCIDENTE', how='left')

#actorVial
print(accidentes.columns)
print(accidentes.dtypes)

print(accidentes['FECHA_x'], accidentes['FECHA_y'])

columnas  = accidentes.columns

for i in range(accidentes.shape[1]):
    print("columna hola")
    print(accidentes[columnas[i]].isna().sum())

print(accidentes['CODIGO_ACCIDENTE'].value_counts())
print(accidentes['FECHA'].value_counts())
print(accidentes['HORA'].value_counts())
print(accidentes['GRAVEDAD'].value_counts())
print(siniestros['CLASE'].value_counts())
print(accidentes['CHOQUE'].value_counts())
print(accidentes['OBJETO_FIJO'].value_counts())
print(accidentes['DIRECCION'].value_counts())
print(accidentes['CODIGO_LOCALIDAD'].value_counts())
print(accidentes['DISENO_LUGAR'].value_counts())

print('CODIGO_ACCIDENTE: ', accidentes['CODIGO_ACCIDENTE'].isna().sum())
print('FECHA: ', accidentes['FECHA'].isna().sum())
print('HORA: ', accidentes['HORA'].isna().sum())
print('GRAVEDAD: ', accidentes['GRAVEDAD'].isna().sum())
print('CLASE: ', accidentes['CLASE'].isna().sum())
print('CHOQUE: ', accidentes['CHOQUE'].isna().sum())
print('OBJETO_FIJO: ', accidentes['OBJETO_FIJO'].isna().sum())
print('DIRECCION: ', accidentes['DIRECCION'].isna().sum())
print('CODIGO_LOCALIDAD: ', accidentes['CODIGO_LOCALIDAD'].isna().sum())
print('DISENO_LUGAR: ', accidentes['DISENO_LUGAR'].isna().sum())

print(accidentes['CODIGO_ACCIDENTE'].is_unique)