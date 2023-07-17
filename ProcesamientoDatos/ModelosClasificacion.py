import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

import joblib

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")
df = df.drop('FECHA_HORA', axis=1)

#muestra aleatoria
muestra = 10000
df = df.sample(n=muestra)

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)
    
#APLICANDO ALGORITMOS
df = df.apply(pd.to_numeric, errors='coerce')

for i in range(df.shape[1]):
    df[df.columns[i]] = df[df.columns[i]].fillna(0)

X = df.drop('GRAVEDAD', axis=1)
y = df['GRAVEDAD']

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

#Exportamos el modelo
joblib.dump(svm_model, r'D:\SiniestrosViales\Modelos Clasificacion\svm_model.pkl')

# Cargar el modelo desde el archivo
#svm_model = joblib.load('svm_model.pkl')


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

#Exportamos el modelo
joblib.dump(knn_model, r'D:\SiniestrosViales\Modelos Clasificacion\knn_model_GRAVEDAD.pkl')

# Cargar el modelo desde el archivo
#knn_model = joblib.load('knn_model.pkl')


# RandomForestClassifier
# Crear un modelo Random Forest con 100 árboles
rf_model = RandomForestClassifier(n_estimators=100)

# Entrenar el modelo Random Forest con los datos de entrenamiento
rf_model.fit(X_train, y_train)

# Predecir las clases para los datos de prueba
y_pred = rf_model.predict(X_test)

# Calcular la precisión (accuracy) del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo Random Forest:", accuracy)

#Exportamos el modelo
joblib.dump(rf_model, r'D:\SiniestrosViales\Modelos Clasificacion\rf_model_GRAVEDAD.pkl')





























