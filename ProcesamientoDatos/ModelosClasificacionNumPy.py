import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = np.genfromtxt(r"D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv", delimiter=',', skip_header=True)
data = np.delete(data, 13, axis=1)

# Reemplazar valores NaN con las medias de las columnas
data = np.where(np.isnan(data), 0, data)

# Genera datos de ejemplo
X = data[:, :-1]  # Todas las columnas excepto la última
y = data[:, -1]   # Última columna

# Calcular la matriz de covarianza de X
cov_matrix = np.cov(X, rowvar=False)

# Calcular los autovalores y autovectores de la matriz de covarianza
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Ordenar los autovalores y autovectores de mayor a menor
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Elegir los primeros componentes principales que deseas mantener
num_components = 1
selected_eigenvectors = eigenvectors[:, :num_components]

# Realizar la transformación PCA
X = np.dot(X, selected_eigenvectors)

# Divide el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea el modelo SVM y entrena
model = SVC(kernel='linear')  # Puedes elegir el kernel que mejor se ajuste a tus datos
model.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evalúa el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo: {accuracy}")
