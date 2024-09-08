#Libreria para la generacion de numeros aleatorios
import numpy as np
#Definimos la función
def f(x, y):
    return (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
#Variables
#Definimos el numero de iteraciones y el rango delas variables
iteraciones = 10000
xMin, xMax = -4.5, 4.5
yMin, yMax = -4.5, 4.5
#Inicializamos un valor minimo con infinito para que tome el primer valor minimo correctamente
minimo = float('inf')
xFinal, yFinal = None, None
#Realizamos las iteraciones
for _ in range(iteraciones):
    #Generamos los valores de x e y en el rango establecido
    x = np.random.uniform(xMin, xMax)
    y = np.random.uniform(yMin, yMax)
    #Calculamos el valor f(x,y)
    valor = f(x, y)
    #Actualizamos el valor minimo si se encuentra uno mejor al anterior
    if valor < minimo:
        minimo = valor
        xFinal, yFinal = x, y

#Imprimimos los valores finales
print(f"El valor minimo encontrado es {minimo:.6f} en x = {xFinal:.6f}, y = {yFinal:.6f}")
