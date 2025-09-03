# Instalamos pandas
# pip install pandas

import pandas as pd

info_pais = {"pais": ["Argentina", "Brasil", "Chile", "Colombia", "Perú"],
             "poblacion": [45.38, 213.99, 19.49, 51.71, 32.51],
             "area": [2780400, 8515767, 756102, 1141748, 1285216]}

## Las claves son las columnas(pais,poblacion,area)
## El valor son los datos de columnas que forman la observacion

## Crear el dataframe
## Importante, la funcion es "DataFrame", "dataframe" no es una funcion de Pandas.
df_paises = pd.DataFrame(info_pais)
