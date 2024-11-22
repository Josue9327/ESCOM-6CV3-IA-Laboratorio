import numpy as np
from collections import Counter  # Para conteo de votos
class KNN:
    def __init__(self, datos_entrenamiento, k=1):
        # Inicializamos la clase con los datos de entrenamiento y el valor de k
        self.datos_entrenamiento = datos_entrenamiento
        self.k = k
    def distancia_euclidiana(self, punto1, punto2):
        # Calculamos la distancia euclidiana entre dos puntos
        return np.sqrt(np.sum((punto1 - punto2) ** 2))
    def clasificar(self, punto):
        # Lista para almacenar las distancias a los puntos de entrenamiento
        distancias = []
        # Iteramos sobre cada punto en el conjunto de entrenamiento
        for fila in self.datos_entrenamiento:
            punto_entrenamiento = np.array(fila[:len(fila)-1], dtype=float)
            etiqueta = fila[len(fila)-1]          
            # Calculamos la distancia entre el punto dado y el punto de entrenamiento
            distancia = self.distancia_euclidiana(punto, punto_entrenamiento)           
            # Almacenamos la distancia y la etiqueta como una tupla
            distancias.append((distancia, etiqueta))        
        # Ordenamos las distancias de menor a mayor
        distancias.sort(key=lambda x: x[0])      
        # Obtenemos las etiquetas de los k vecinos más cercanos
        vecinos_cercanos = [dist[1] for dist in distancias[:self.k]]
        # Realizamos la votación mayoritaria para determinar la clase predicha
        clase_calculada = Counter(vecinos_cercanos).most_common(1)[0][0]
        return clase_calculada