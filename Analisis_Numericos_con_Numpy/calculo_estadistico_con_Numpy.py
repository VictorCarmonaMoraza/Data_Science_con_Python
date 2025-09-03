
import numpy as np

temperaturas = np.array([22.4, 21.8, 23.0, 22.5, 21.9, 22.8, 22.7, 23.1, 22.3, 22.6])


media = np.mean(temperaturas)
print(f"La temperatura media es: {media}")

mediana = np.median(temperaturas)
print(f"La mediana en el arrya de temperaturas es: {mediana}")

minimo = np.min(temperaturas)
print(f"La temperatura mínima es: {minimo}")

maximo = np.max(temperaturas)
print(f"La temperatura máxima es: {maximo}")

varianza = np.var(temperaturas)
print(f"La varianza de las temperaturas es: {varianza}")

desviacion_estandar = np.std(temperaturas)
print(f"La desviación estándar de las temperaturas es: {desviacion_estandar}")

percentil_25 = np.percentile(temperaturas, 25)
print(f"El percentil 25 de las temperaturas es: {percentil_25}")

percentil_75 = np.percentile(temperaturas, 75)
print(f"El percentil 75 de las temperaturas es: {percentil_75}")


##Generar datos con Numpy tomando como partida parametros estadisticos

media =2
desviacion_estandar = 0.5
muestras = 1000

nuevas_temperaturas = np.random.normal(media, desviacion_estandar, muestras)
##print(f"Nuevas temperaturas generadas: {nuevas_temperaturas}")

##Graficas para las nueva temperatutas
import matplotlib.pyplot as plt

##Datos simulados
# Parámetros
media = 3
desviacion_estandar = 1.5
muestras = 10000

# Generar datos simulados
array_gaus = np.random.normal(media, desviacion_estandar, muestras)

##Media de los 10000 muestras
media_array = np.mean(array_gaus)
print(f"Media de la distribución gaussiana: {media_array}")

##Desviacion estandar de la distribucion gaussiana
desviacion_estandar_array = np.std(array_gaus)
print(f"Desviación estándar de la distribución gaussiana: {desviacion_estandar_array}")

# La expresión:
#     x̄ - 2σ < x < x̄ + 2σ
# no es la fórmula gaussiana en sí.
# Es una regla empírica que nos dice que, en una distribución normal,
# aproximadamente el 95% de los datos caen dentro de ese rango.

# Rango del 95% (media ± 2σ)
rango_95 = [media - 2*desviacion_estandar, media + 2*desviacion_estandar]

# Función gaussiana
x = np.linspace(min(array_gaus), max(array_gaus), 500)
y = 1/(desviacion_estandar * np.sqrt(2*np.pi)) * np.exp(-((x-media)**2)/(2*desviacion_estandar**2))

# Gráfica de la curva gaussiana con puntos
plt.scatter(x, y, s=100, color='blue', alpha=1, label="Distribución normal")

# Marcar el rango del 95%
plt.axvline(rango_95[0], color='green', linestyle='--', linewidth=2, label=f"Límite inferior ({rango_95[0]:.2f})")
plt.axvline(rango_95[1], color='green', linestyle='--', linewidth=2, label=f"Límite superior ({rango_95[1]:.2f})")
plt.axvspan(rango_95[0], rango_95[1], alpha=0.2, color='green')

# Títulos y leyenda
plt.title("Distribución Gaussiana con rango del 95%")
plt.xlabel("Valores")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()

print("Rango del 95%:", rango_95)
