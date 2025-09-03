import pandas as pd

df = pd.read_csv(r"pedestrian_information_2020.csv", delimiter=";",
                  encoding="ISO-8859-1")

## Visualizar i registros del dataframe(defecto = 5)
print(df.head(10))

## Devuelve el numero de filas y columnas del dataframe
print(df.shape)


## Devuelve informacion del indice/ columnas del dataframe
print(df.index)
print(df.columns)

## Obtener informacion de todas las columnas del dataframe
print(df.info())

## Devuelve el numero de valores non-NA
print(df.count())

## SUM(): Suma todos los valores de una columna
print(f"La suma de todos los valores de la columna NÚMERO es: {df["NÚMERO"].sum()}")

## Mean() / Median(): Calcula el promedio / mediana de una columna
print(f"El promedio de la columna NÚMERO es: {df["NÚMERO"].mean()}")
print(f"La mediana de la columna NÚMERO es: {df["NÚMERO"].median()}")

## Quantile(k) (Equivalente Percentile de Numpy): Calcula el percentile k de una columna [0,1]
## Significa que el 80% de los valores no supera 51
print(f"El percentil 80 de la columna NÚMERO es: {df["NÚMERO"].quantile(0.80)}")

## Min() / Max(): Obtener el minimo y maximo de una columna
print(f"El valor minimo de la columna NÚMERO es: {df["NÚMERO"].min()}")
print(f"El valor maximo de la columna NÚMERO es: {df["NÚMERO"].max()}")

## Describe(): Realiza un resumen estadistico para todas las columnas de tipo numerico
print(df.describe())

## EJERCICIO
## A partir del dataframe anterior con la informacion de trafico peatonal, obtener
# la informacion del dataframe y la informacion estadística:
# ¿ Cuantos valores erroneos tiene la columna "PEATONES"?
# ¿Cual es la mediana de la variable "PEATONES"?
# ¿Cual es el rango de fechas de nuestros datos?
#Crea una columna acumulativa del numero de peatones(metodo cumsum)

## Obtenemos el numero de filas y columnas de nuestros dataframe
print(f"El numero de filas y de columnas es: {df.shape}")

## Obtenemos los 5 primeros registros
print(df.head())

## Obtener informacion de cada columna
print(df.info())

## Devuelve el numero de valores non-NA
print(df.count())

## Obtener la mediana de la columna de PEATONES
print(f"La mediana de la columna PEATONES es: {df['PEATONES'].median()}")
## Promedio
print(f"El promedio de la columna PEATONES es: {df['PEATONES'].mean()}")

## Obtener el percentile 90
## Singifica que el 90% de nuestros tramos de 15 minutos no supera las 956 peatones
print(f"El percentil 90 de la columna PEATONES es: {df['PEATONES'].quantile(0.90)}")

## Obtener el rango de fechas de nuestros datos
print(f"El rango de fechas es: {df['FECHA'].min()} - {df['FECHA'].max()}")

## Obtener datos estadisticos de nuestro dataframe
print(df.describe())

## Crear una columna acumulativa del numero de peatones
df['PEATONES_ACUM'] = df['PEATONES'].cumsum()
print(df.head())
