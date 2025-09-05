
## Ejercicio
## Crear el dataframe(df_nuevo_2025) a partir del fichero 'pedestrian_information_2020_mod.csv'

## - Cree el dataframe (df2) con el filtrado de datos necesarios si queremos enfocar nuestro analisis 
## en que ocurrio los dias comprendidos en el rango [01/01/2020 -01/0572020]

## - Sobre el mismo dataframe(df2), realice el filtrado para el distrito "Centro".Utilice str.contains

## - Verifique si hay valores erroneos en la columna "PEATONES" en estas condiciones, en caso afirmativo
## cree el dataframe df_interp con la interpolacion lineal df2

import pandas as pd


df_nuevo_2025= pd.read_csv(r"pedestrian_information_2020_mod.csv", delimiter=";",encoding="ISO-8859-1")
print(f"Dataframe original: {df_nuevo_2025}")

## Filtrar por rango de fechas
df2 = df_nuevo_2025[(df_nuevo_2025["FECHA"] >= "01/01/2020") & (df_nuevo_2025["FECHA"] <= "01/05/2020")]
print(f"Dataframe filtrado por rango de fechas: {df2}")

df2 =df2[df2["DISTRITO"].str.contains("Centro")]
print(f"Dataframe filtrado por distrito Centro: {df2}")
## Obtener el numero de registros
print(f"Número de registros: {df2.shape[0]}")

## Otra forma de comprobar los valores erroneos es con el metodo count
print(f"Registrso en todas las columnas:{df2.count()}") 

##Verificar si hay valores erroneos en la columna PEATONES
df2_not_null = df2[df2["PEATONES"].notnull()]
print(f"El numero de registros sin valores nulos en PEATONES: {df2_not_null.shape[0]}")

##Mostrar los registros con valores a null
df2_null = df2[df2["PEATONES"].isnull()]
print(df2_null)

## Registros con null
contador = df2.shape[0] - df2_not_null.shape[0]
print(f"El numero de registros con valores nulos en PEATONES: {contador}")

## Rellenar los registros con el metod interpolate de Pandas
df2_interp = df2.interpolate(method='linear', limit_direction='both')
print(f"Dataframe con valores interpolados: {df2_interp}")

##Verficar que todos los registros tienen valores
print(f"Registros en todas las columnas despues de interpolar:{df2_interp.count()}")
