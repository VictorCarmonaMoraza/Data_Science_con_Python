## EJERCICIO
## Cargar los primeros 10.000 registros del fichero CSV de trafico
## de peatones (delimitador ";") indicando como indice del Dataframe
## la columna "IDENTIFICADOR"

import pandas as pd


df = pd.read_csv(r"PEATONES_2020.csv", delimiter=";", nrows=10000, index_col="IDENTIFICADOR", encoding="ISO-8859-1")

print(df.head())
print(df.info())