## Crear un array 2D con numpy
## Sintaxis: array_2d = np.array([[valores fila 1], [valores fila 2]]) 

## Para esta matriz
## 2  7  8
## 4  8  10

import numpy as np

np_2d = np.array([[2,7,8],[4,8,10]])

## Seleccionar datos en un array 2D
np_2d_fila1_columna2 = np_2d[0,1] ## Fila 1, columna 2
print(f"El valor en la fila 1, columna 2 es: {np_2d_fila1_columna2}")  ## --->7


np_2d_fila_2_columna_3 = np_2d[1,2] ## Fila 2, columna 3
print(f"El valor en la fila 2, columna 3 es: {np_2d_fila_2_columna_3}")  ## --->10