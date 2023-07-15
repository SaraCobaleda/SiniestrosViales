import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)

#CONOCIENDO LA DATA

df["EDAD"].plot.box()
plt.show()

valor_maximo = df["EDAD"].max()
valor_minimo = df["EDAD"].min()

print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)

# Create scatter plot
plt.scatter(df['CODIGO_LOCALIDAD'], df['EDAD'])
plt.title('EDAD VS CODIGO_LOCALIDAD')
plt.ylabel('CODIGO_LOCALIDAD')
plt.xlabel('CODIGO_LOCALIDAD')
plt.show()

# Create histogram
plt.hist(df['CLASE_VEHICULO'], bins=10)
plt.show()

print(df['CODIGO_CAUSA'].value_counts())

#APLICANDO ALGORITMOS
df = df.apply(pd.to_numeric, errors='coerce')

for i in range(df.shape[1]):
    df[df.columns[i]] = df[df.columns[i]].fillna(0)

#reduccion de la dimensionalidad
pca = PCA(n_components=1)
df_reducido = df.drop('FECHA_x', axis=1)
df_reducido = df_reducido.drop('HORA', axis=1)
df_reducido = df_reducido.astype(int)
df_reducido = pca.fit_transform(df_reducido)

X = df_reducido
y = df['FECHA_x']

#SVM
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador SVM
clf = svm.SVC(kernel='linear')

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)













