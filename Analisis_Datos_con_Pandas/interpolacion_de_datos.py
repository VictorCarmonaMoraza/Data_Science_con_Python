import pandas as pd

info_pais = {
    "pais": ["Argentina", "Brasil", "Chile", "Colombia", "Perú"],
    "poblacion": [None, 213.99, 19.49, 51.71, None],
    "area": [2780400, 8515767, None, 1141748, None]
}

## convertir a dataframe
df_pais = pd.DataFrame(info_pais)


## Rellenar con la funcion fillna
df_poblacion_relleno = df_pais["poblacion"].fillna(df_pais["poblacion"].median()) 
print(f"Relleno con fillna: {df_poblacion_relleno}")

## Rellenar con la funcion interpolate(El primer valor de poblacion que su valor es None no lo rellena)
df_poblacion_interpolado = df_pais.interpolate(method="linear", limit_direction="forward")
print(f"Relleno con interpolate: {df_poblacion_interpolado}")


## Rellenar con la funcion interpolate(Se rellena todos los NaN)
df_poblacion_interpolado2 = df_pais.interpolate(method="linear", limit_direction="both")
print(f"Relleno con interpolate2: {df_poblacion_interpolado2}")