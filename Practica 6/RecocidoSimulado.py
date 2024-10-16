import numpy as np
#Función de Himmelblau
def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2
#Parametros
#Temperatura inicial
temp_inicial = 10000  
#Temperatura final
temp_final = 1        
#Enfriamiento
cooling_rate = .99
#Número de iteraciones
num_iteraciones = 1000  

#Generamos un punto inicial aleatorio
x_actual = np.random.uniform(-5, 5)
y_actual = np.random.uniform(-5, 5)

#Guardamos elpunto y su valor de la función
x_mejor, y_mejor = x_actual, y_actual
valor_mejor = himmelblau(x_mejor, y_mejor)

#Algoritmo de Recocido Simulado
temp = temp_inicial
while temp > temp_final:
    for _ in range(num_iteraciones):
        #Generamos un nuevo vecino aleatorio en base al punto actual
        x_nuevo = x_actual + np.random.uniform(-0.5, 0.5)
        y_nuevo = y_actual + np.random.uniform(-0.5, 0.5)
        # Limitamos los valores a [-5, 5]
        x_nuevo = np.clip(x_nuevo, -5, 5)
        y_nuevo = np.clip(y_nuevo, -5, 5)
        #Calculamos el valor de la función en el nuevo punto
        valor_nuevo = himmelblau(x_nuevo, y_nuevo)
        #Si el nuevo punto es mejor lo aceptamos. Si no lo es, lo aceptamos con una probabilidad dependiente de la temperatura
        if valor_nuevo < valor_mejor or np.random.rand() < np.exp((valor_mejor - valor_nuevo) / temp):
            x_actual, y_actual = x_nuevo, y_nuevo
            valor_mejor = valor_nuevo
            x_mejor, y_mejor = x_actual, y_actual
    #Enfriamos la temperatura
    temp *= cooling_rate

print(f"Mejores valores encontrados: x = {x_mejor}, y = {y_mejor}")
print(f"Valor mínimo de la función: f(x, y) = {valor_mejor}")
