## Para seleccionar datos dentro de un array 
## Slice[inicio(incluido):fin(excluido)]

import numpy as np

bmi = np.array([23.183391, 20.2020202, 21.73650525])

##Posiciones
## 0  1  2
# -3 -2 -1

##Posciones 0,1,2 o -3,-2,-1
print(f"La posicion 0 es {bmi[0]}")
print(f"La posicion -3 es igual que la posicion 0 es {bmi[-3]}")

##posicion 1 o -2
print(f"La posicion 1 es {bmi[1]}")
print(f"La posicion -2 es igual que la poscion 1 es {bmi[-2]}")

## posicion 2 o -1
print(f"La posicion 2 es {bmi[2]}")
print(f"La posicion -1 es igual que la posicion 2 es {bmi[-1]}")

##Calcular valores quye superen una condicion
print(f"Valores que superan 21: {bmi > 21}")

##Retornar solo los valores que cumplen la condicion
print(f"Valores que superan 21: {bmi[bmi > 21]}")

##EJERCICIO: Calcular masivamente el area de 5 rectangulos y devolver
## unicamente aquellos con area>10
base_rec = np.array([5,2,4,7,8])
alturas_rec =np.array([3,4,1,4,3])

area_rec = base_rec * alturas_rec
print(f"Areas de los rectangulos son: {area_rec}")
area_rec_mayor_10 = area_rec[area_rec > 10]
area_rec_mayor_10_boolean = area_rec > 10
print(f"Areas de los rectangulos mayores a 10 son: {area_rec_mayor_10}")
print(f"Areas de los rectangulos mayores a 10 son: {area_rec_mayor_10_boolean}")

print(f"LISTAS")
a = [2,5,7]
b = [3,4,5]
print(f"con listas:{a+b}") ## Devuelve: [2, 5, 7, 3, 4, 5]

print(f"con numpy:")
a_numpy = np.array([2,5,7])
b_numpy = np.array([3,4,5])
print(f"con numpy:{a_numpy + b_numpy}") ## Devuelve: [5 9 12]
