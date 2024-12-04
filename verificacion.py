import pandas as pd

# Cargar el archivo limpio
data_limpia = pd.read_excel('archivo_limpio.xlsx')

# Verificar las columnas relevantes
print("Columnas en el archivo limpio:")
print(data_limpia.columns)

# Mostrar muestra de datos
print("\nEjemplo de los datos limpios:")
print(data_limpia.head())

# Comprobaciones básicas
print("\nComprobaciones de calidad de datos:")
print("Valores nulos por columna:")
print(data_limpia.isnull().sum())

print("\nTipos de datos:")
print(data_limpia.dtypes)
