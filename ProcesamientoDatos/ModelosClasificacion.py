import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")
df = df.drop('FECHA_HORA', axis=1)

#muestra aleatoria
muestra = 100000
df = df.sample(n=muestra)

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)
    
#APLICANDO ALGORITMOS
df = df.apply(pd.to_numeric, errors='coerce')

for i in range(df.shape[1]):
    df[df.columns[i]] = df[df.columns[i]].fillna(0)

X = df.drop('CLASE_SINIESTRO', axis=1)
y = df['CLASE_SINIESTRO']

#pasarlos a arreglos de numpy
y = y.values
X = X.values

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# SVM
# Crear un modelo SVM
svm_model = svm.SVC(kernel='linear')

# Entrenar el modelo SVM con los datos de entrenamiento
svm_model.fit(X_train, y_train)

# Predecir las clases para los datos de prueba
y_pred = svm_model.predict(X_test)

# Calcular la precisión (accuracy) del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo SVM:", accuracy)


# K-Nearest Neighbors
# Crear un modelo KNN con K=3 (3 vecinos más cercanos)
knn_model = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo KNN con los datos de entrenamiento
knn_model.fit(X_train, y_train)

# Predecir las clases para los datos de prueba
y_pred = knn_model.predict(X_test)

# Calcular la precisión (accuracy) del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo KNN:", accuracy)
