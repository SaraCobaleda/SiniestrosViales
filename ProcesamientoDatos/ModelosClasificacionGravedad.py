import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import tensorflow as tf

import joblib

df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")
df = df.drop('FECHA_HORA', axis=1)

#muestra aleatoria
muestra = 100000
df = df.sample(n=muestra)

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)


    
#APLICANDO ALGORITMOS GRAVEDAD
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
svm_model.fit(X_train, y_train)

# Predecir las clases para los datos de prueba
y_pred = svm_model.predict(X_test)

# Calcular la precisión (accuracy) del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo SVM:", accuracy)

#Exportamos el modelo
joblib.dump(svm_model, r'D:\SiniestrosViales\Modelos Clasificacion\svm_model_GRAVEDAD.pkl')

# Cargar el modelo desde el archivo
#svm_model = joblib.load('svm_model.pkl')



# K-Nearest Neighbors
# Crear un modelo KNN con K=3 (3 vecinos más cercanos)
knn_model = KNeighborsClassifier(n_neighbors=3)
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
rf_model.fit(X_train, y_train)

# Predecir las clases para los datos de prueba
y_pred = rf_model.predict(X_test)

# Calcular la precisión (accuracy) del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo Random Forest:", accuracy)

#Exportamos el modelo
joblib.dump(rf_model, r'D:\SiniestrosViales\Modelos Clasificacion\rf_model_GRAVEDAD.pkl')


    
# Logistic Regression
# Crear y entrenar el modelo de regresión logística
lg_model = LogisticRegression()
lg_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = lg_model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

#Exportamos el modelo
joblib.dump(lg_model, r'D:\SiniestrosViales\Modelos Clasificacion\lg_model_GRAVEDAD.pkl')



#  Máquinas de Aprendizaje Profundo
# Crear una arquitectura de red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_dim=10),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluar el modelo en el conjunto de prueba
y_pred = model.predict(X_test)
y_pred_binary = (y_pred > 0.5).astype(int)
accuracy = accuracy_score(y_test, y_pred_binary)
print("Precisión del modelo:", accuracy)
