import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

siniestros = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="SINIESTROS")
actorVial = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="ACTOR_VIAL")
vehiculos = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="VEHICULOS")
hipotesis = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="HIPOTESIS")
diccionario = pd.read_excel(r"D:\SiniestrosViales\ProcesamientoDatos\siniestros_viales_consolidados_bogota_dc.xlsx", sheet_name="DICCIONARIO")

#historico = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\historico_siniestros_bogota_d.c_-.csv")

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

#FECHA_x y HORA
df['FECHA_HORA'] = pd.to_datetime(df['FECHA_x'] + ' ' + df['HORA'])
df.drop(['FECHA_x', 'HORA'], axis=1, inplace=True)

#EDAD
print(df["EDAD"].value_counts())

df['EDAD'] = df['EDAD'].replace('SIN INFORMACION', None)
promedio = df['EDAD'].mean(skipna=True)
df['EDAD'] = df['EDAD'].fillna(promedio)

print(df['EDAD'].isnull().sum())
print(df['EDAD'].value_counts())

#COMPLPETAR VALORES NULOS DE LAS DEMAS COLUMNAS
df['CHOQUE'] = df['CHOQUE'].fillna(0)
df['CLASE_VEHICULO'] = df['CLASE_VEHICULO'].fillna(0)
df['SERVICIO'] = df['SERVICIO'].fillna(0)

#CODIGO_CAUSA
df['CODIGO_CAUSA'] = df['CODIGO_CAUSA'].fillna(0)
df['CODIGO_CAUSA'] = df['CODIGO_CAUSA'].replace('ANT-133',0)

#GRAVEDAD
print(df["GRAVEDAD"].value_counts())
print(df['SEXO'].isnull().sum())

#CLASE_SINIESTRO
print(df["CLASE_SINIESTRO"].value_counts())
print(df['SEXO'].isnull().sum())

#CODIGO_LOCALIDAD
print(df["CODIGO_LOCALIDAD"].value_counts())
print(df['SEXO'].isnull().sum())

#DISENO_LUGAR
print(df["DISENO_LUGAR"].value_counts())
print(df['SEXO'].isnull().sum())

#comprobar valores
for i in range(df.shape[1]):
    print(df[df.columns[i]].value_counts())
    
#reacomodando los codigos de la causa

mapeo_cod_causa = {90	:	1	,
                    91	:	2	,
                    92	:	3	,
                    93	:	4	,
                    94	:	5	,
                    95	:	6	,
                    96	:	7	,
                    97	:	8	,
                    98	:	9	,
                    99	:	10	,
                    101	:	11	,
                    102	:	12	,
                    103	:	13	,
                    104	:	14	,
                    105	:	15	,
                    106	:	16	,
                    107	:	17	,
                    108	:	18	,
                    109	:	19	,
                    110	:	20	,
                    111	:	21	,
                    112	:	22	,
                    113	:	23	,
                    114	:	24	,
                    115	:	25	,
                    116	:	26	,
                    117	:	27	,
                    118	:	28	,
                    119	:	29	,
                    120	:	30	,
                    121	:	31	,
                    122	:	32	,
                    123	:	33	,
                    124	:	34	,
                    125	:	35	,
                    126	:	36	,
                    127	:	37	,
                    128	:	38	,
                    129	:	39	,
                    130	:	40	,
                    131	:	41	,
                    132	:	42	,
                    133	:	43	,
                    134	:	44	,
                    135	:	45	,
                    136	:	46	,
                    137	:	47	,
                    138	:	48	,
                    139	:	49	,
                    140	:	50	,
                    141	:	51	,
                    142	:	52	,
                    143	:	53	,
                    144	:	54	,
                    145	:	55	,
                    146	:	56	,
                    147	:	57	,
                    148	:	58	,
                    149	:	59	,
                    150	:	60	,
                    151	:	61	,
                    152	:	62	,
                    153	:	63	,
                    154	:	64	,
                    155	:	65	,
                    156	:	66	,
                    157	:	67	,
                    201	:	68	,
                    202	:	69	,
                    203	:	70	,
                    204	:	71	,
                    205	:	72	,
                    206	:	73	,
                    207	:	74	,
                    208	:	75	,
                    209	:	76	,
                    210	:	77	,
                    211	:	78	,
                    212	:	79	,
                    213	:	80	,
                    214	:	81	,
                    216	:	82	,
                    217	:	83	,
                    301	:	84	,
                    302	:	85	,
                    303	:	86	,
                    304	:	87	,
                    305	:	88	,
                    306	:	89	,
                    307	:	90	,
                    308	:	91	,
                    401	:	92	,
                    402	:	93	,
                    403	:	94	,
                    404	:	95	,
                    405	:	96	,
                    406	:	97	,
                    407	:	98	,
                    408	:	99	,
                    409	:	100	,
                    410	:	101	,
                    411	:	102	,
                    501	:	103	,
                    502	:	104	,
                    503	:	105	,
                    504	:	106	,
                    505	:	107	,
                    506	:	108	,
                    }

df['CODIGO_CAUSA'] = df['CODIGO_CAUSA'].replace(mapeo_cod_causa)
df['CODIGO_CAUSA'] = df['CODIGO_CAUSA'].fillna(0)

    
df.to_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv", index=False)