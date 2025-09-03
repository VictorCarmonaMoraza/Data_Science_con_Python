## EJERCICIO
## Cargar los primeros 535 registros del fichero CSV de trafico
## de peatones (delimitador ";") indicando como indice del Dataframe
## la columna "CÓDIGO_POSTAL"

import pandas as pd


df = pd.read_csv(r"pedestrian_information_2020.csv", delimiter=";",
                 nrows=535, index_col="CÓDIGO_POSTAL", encoding="ISO-8859-1")

print(df.head())
print(df.info())