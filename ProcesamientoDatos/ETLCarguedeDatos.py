import csv
import psycopg2
from psycopg2 import sql
import pandas as pd


# Step 1: Extract the data from the CSV file
csv_file = r'D:\SiniestrosViales\ProcesamientoDatos\DataLimpia.csv'
data = pd.read_csv(csv_file)

mapeo_columnas = {
    'GRAVEDAD': 'gravedad',
    'CLASE_SINIESTRO': 'claseSiniestro',
    'CHOQUE': 'choque',
    'CODIGO_LOCALIDAD': 'codigoLocalidad',
    'DISENO_LUGAR': 'disenoLugar',
    'CONDICION': 'condicion',
    'ESTADO': 'estado',
    'EDAD': 'edad',
    'SEXO': 'sexo',
    'CLASE_VEHICULO': 'claseVehiculo',
    'SERVICIO': 'servicio',
    'ENFUGA': 'enfuga',
    'CODIGO_CAUSA': 'codigoCausa',
    'FECHA_HORA': 'fechaHora'
}

data.rename(columns=mapeo_columnas, inplace=True)

data.to_csv(r'D:\SiniestrosViales\ProcesamientoDatos\DataLimpia2.csv', index=False)

# Especifica la ruta del archivo CSV
archivo_csv = r'D:\SiniestrosViales\ProcesamientoDatos\DataLimpia2.csv'

# Especifica el tamaño de la muestra que deseas seleccionar
tamano_muestra = 1000  # Cambia este valor según tus necesidades

# Lee el archivo CSV en un DataFrame de pandas
dataframe = pd.read_csv(archivo_csv)

# Selecciona una muestra aleatoria del DataFrame
muestra_aleatoria = dataframe.sample(n=tamano_muestra)

# Imprime la muestra aleatoria
muestra_aleatoria.to_csv(r'D:\SiniestrosViales\ProcesamientoDatos\MuestraData.csv', index=False)

#---------------------------------------------------------------------------------------------------

import csv
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='database-siniestros.c2d0dhv8axyo.us-east-2.rds.amazonaws.com',
    database="postgres",
    user="postgres",
    password="4DBUe8J623cX4n"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Open the CSV file
with open(r'D:\SiniestrosViales\ProcesamientoDatos\MuestraData.csv', 'r') as file:
    # Create a CSV reader object
    csv_data = csv.reader(file)
    
    # Read the header row to get the column names
    header = next(csv_data)
    
    # Construct the SQL query to create the table
    table_name = 'siniestros_crudos'
    columns = ', '.join(f"{column} TEXT" for column in header)
    create_table_query = f"CREATE TABLE {table_name} ({columns})"
    
    # Execute the SQL query to create the table
    cursor.execute(create_table_query)

    # Iterate over the remaining rows and insert data into the table
    for row in csv_data:
        # Construct the SQL query to insert data into the table
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join('%s' for _ in row)})"
        
        # Execute the SQL query to insert data into the table
        cursor.execute(insert_query, row)

# Commit the changes to the database
conn.commit()

# Close the cursor and database connection
cursor.close()
conn.close()

