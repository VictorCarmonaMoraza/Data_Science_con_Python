## Libreria enfocada al calculo numerico sencilla y rapida
## Su objeto base es el Array Numpy (alternativa a la lista)
## Calculos realizados sobre todo el Array
## Solo pueden contener un tipo de dato (normalmente numero) a diferencia de las listas

## Instalacion de Numpy para Python: pip install numpy
## Importar Numpy: import numpy as np

##Calculo elemento a elemento
import numpy as np

np_alt = np.array([1.7,1.65,1.82])
np_peso = np.array([67,55,72])

bmi = np_peso / np_alt**2
print(bmi)
