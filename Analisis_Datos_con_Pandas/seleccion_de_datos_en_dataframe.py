## Selección de datos en un DataFrame
## LOC (Basada en etiquetas)
## ILOC (Basada en posiciones)

import pandas as pd

# Datos iniciales
data = {
    "Nombre": ["Marta", "Luis", "Marta", "Pedro"],
    "Edad": [23, 30, 27, 35],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
}

df = pd.DataFrame(data)

# Cambiar el índice a la columna "Nombre"
##lo que ocurre es que la columna Nombre pasa a ser el índice del DataFrame, es decir,
# Pandas deja de usar los números 0, 1, 2... como identificadores de fila y empieza a
# usar los valores de esa columna.
df = df.set_index("Nombre")

## : → significa “todas las filas”.
## ["Ciudad"] → significa “solo la columna Ciudad”.
## Estás seleccionando todas las filas pero únicamente la columna "Ciudad".
df_nombre = df.loc[:,["Ciudad"]]

##print(df)
print(df_nombre)

## ILOC:Devuelve de la columna 0 (Edad) las filas 1 y 2 (Luis y Marta)
print(df.iloc[1:3, [0]])
