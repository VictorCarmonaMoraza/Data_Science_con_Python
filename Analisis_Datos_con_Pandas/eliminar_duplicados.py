# A esto se le llama limpieza de datos
# Eliminar duplicados
# Eliminar valores erroneos
# Eliminar columnas de un dataframe

import pandas as pd

info_pais = {"pais": ["Argentina", "Brasil", "Chile", "Colombia", "Perú", "Argentina", "Chile"],
             "poblacion": [45.38, 213.99, 19.49, 51.71, 32.51, 45.38, 16],
             "area": [2780400, 8515767, 756102, 1141748, 1285216, 2780400, None]}

# Convertir a dataframe
df_pais = pd.DataFrame(info_pais)

# Eliminamos duplicados
df_pais_sin_duplicados = df_pais.drop_duplicates()
print(df_pais_sin_duplicados)

# Si queremos guardar sobre el mismo dataframe los valores sin duplicados
# df_pais = df_pais.drop_duplicates()
# print(f"Mismo dataframe df_pais: {df_pais}")

# Aplicamos duplicados sobre columnas
# Dejara solo una Argentina y un Chile
df_pais = df_pais.drop_duplicates("pais")
print(f"Mismo dataframe df_pais: {df_pais}")

# Eliminar nan
df_pais_sin_nan = df_pais.dropna()
print(f"Dataframe sin NaN: {df_pais_sin_nan}")

# Eliminar columnas
df_pais = df_pais.drop(columns=["area"])
print(f"Dataframe sin columna 'area': {df_pais}")


# 📝 Ejercicio
# A partir del archivo pedestrian_information_2020.csv, realiza las siguientes tareas:

# 1. Verificar registros
#    - Obtén el número total de registros en el DataFrame.

# 2. Eliminar duplicados
#    - Identifica y elimina los registros duplicados, es decir, aquellos que tienen los mismos valores en todas las columnas.
#    - ¿Cuántos registros duplicados existían?

# 3. Eliminar valores erróneos (NaN)
#    - Elimina todas las filas que contengan valores faltantes (NaN).
#    - ¿Cuántos valores NaN había en el DataFrame?

# 4. Calcular porcentaje de error
#    - ¿Qué porcentaje de los datos originales correspondía a valores erróneos (NaN)?

# --------------------------------------------------------------------
# Aquí puedes empezar a programar tu solución paso a paso 👇

# Cargar el archivo CSV en un DataFrame
df_info = pd.read_csv(r"pedestrian_information_2020_mod.csv", delimiter=";",
                 encoding="ISO-8859-1")

## 1. Verificar numero total de registros
print(f"Numero total de registros en el DataFrame: {df_info.shape}")

## 2. Eliminar duplicados
df_exec_sin_duplicados = df_info.drop_duplicates()
print(f"Numero total de registros en el DataFrame sin duplicados: {df_exec_sin_duplicados.shape}")

## 3. Eliminar valores erróneos (NaN)
df_exec_sin_nan = df_exec_sin_duplicados.dropna()
print(f"Numero total de registros en el DataFrame sin NaN: {df_exec_sin_nan.shape}")

## 4. Calcular porcentaje de error
## Registros sin Nan
valores_erroneos = df_exec_sin_duplicados.shape[0] - df_exec_sin_nan.shape[0]
print(f"Numero total de registros eliminados : {valores_erroneos}")
porcentaje_error = valores_erroneos / df_info.shape[0] * 100
print(f"Porcentaje de error en el DataFrame: {porcentaje_error:.6f}%")

