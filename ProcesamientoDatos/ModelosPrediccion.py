import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


df = pd.read_csv(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv")

df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])
df['FECHA_HORA'] = df['FECHA_HORA'].apply(lambda x: int(x.timestamp()))

#muestra aleatoria
muestra = 100
df = df.sample(n=muestra)

# Cuantos Valores faltantes hay
missing_values = df.isnull().sum()
print(missing_values)
    
#APLICANDO ALGORITMOS
df = df.apply(pd.to_numeric, errors='coerce')

for i in range(df.shape[1]):
    df[df.columns[i]] = df[df.columns[i]].fillna(0)

X = df.drop('FECHA_HORA', axis=1)
y = df['FECHA_HORA']

#pasarlos a arreglos de numpy
y = y.values
X = X.values

#PREDICCION
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# DecisionTreeRegressor
# Crear el regresor de Árbol de Decisión
regressor = DecisionTreeRegressor()

# Entrenar el regresor
regressor.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = regressor.predict(X_test)

# Calcular el error cuadrático medio (MSE) del regresor
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)

y_test = pd.DataFrame(y_test, columns=[0])
y_test[0] = pd.to_datetime(y_test[0], unit='s')
y_pred = pd.DataFrame(y_pred, columns=[0])
y_pred[0] = pd.to_datetime(y_pred[0], unit='s')

#RandomForestRegressor
# Crear el regresor de Random Forest
regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Entrenar el regresor
regressor.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = regressor.predict(X_test)

# Calcular el error cuadrático medio (MSE) del regresor
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)


#SVC
# Crear el clasificador SVC
clf = SVC(kernel='rbf', C=1.0)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)

# Mostrar el informe de clasificación
report = classification_report(y_test, y_pred)
print("Informe de clasificación:")
print(report)


#LogisticRegression
# Crear el clasificador de regresión logística
clf = LogisticRegression()

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)

# Mostrar el informe de clasificación
report = classification_report(y_test, y_pred)
print("Informe de clasificación:")
print(report)