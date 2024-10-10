import numpy as np

#Funcion de Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#Parámetros para la búsqueda aleatoria
#Definimos el número de iteraciones (cantidad de puntos aleatorios)
n_puntos = 10000
# Generamos los array para los valores random de x y y en el rango [-5, 5]
x_random = np.random.uniform(low=-5, high=5, size=n_puntos)
y_random = np.random.uniform(low=-5, high=5, size=n_puntos)

#Evaluamos la función de Himmelblau en cada punto aleatorio
valores = []
for i in range(n_puntos):
    valor = himmelblau(x_random[i], y_random[i])
    valores.append(valor)

#Convertimos la lista de valores a un array de numpy para mejor manejo
valores = np.array(valores)

#Buscamos el índice del valor mínimo
indice_minimo = np.argmin(valores)

#Usamos el índice para encontrar las coordenadas correspondientes al mínimo
x_minimo = x_random[indice_minimo]
y_minimo = y_random[indice_minimo]

#Extraemos el valor mínimo de la función
valor_minimo = valores[indice_minimo]

#Imprimimos los resultados
print(f"Mínimo encontrado en: x = {x_minimo}, y = {y_minimo}")
print(f"Valor mínimo de la función: {valor_minimo}")
