import pandas as pd

# Cargar el archivo Excel
data = pd.read_excel('Jugadoresfifa21.xlsx')

# Verificar columnas cargadas
print("Columnas disponibles en el archivo:")
print(data.columns)

# Transformaciones
print("\nIniciando limpieza y transformaciones...")

# Asegurarnos de que 'dob' es tipo string antes de dividirla
data['dob'] = data['dob'].astype(str)

# Dividir fecha de nacimiento (dob) en Año, Mes y Día
data[['Año', 'Mes', 'Día']] = data['dob'].str.split('-', expand=True)

# Renombrar columnas relevantes para claridad
data = data.rename(columns={
    'height_cm': 'Altura',
    'weight_kg': 'Peso',
    'value_eur': 'Valor',
    'wage_eur': 'Salario',
    'release_clause_eur': 'Cláusula de rescisión',
    'club_name': 'Equipo',
    'nationality': 'Nacionalidad'
})

# Guardar el archivo limpio
data.to_excel('archivo_limpio.xlsx', index=False)

print("\nTransformaciones completadas. El archivo limpio se ha guardado como 'archivo_limpio.xlsx'.")
