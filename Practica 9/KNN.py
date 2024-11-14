import numpy as np

class KNN:
    def __init__(self, datos_entrenamiento):
        # Inicializamos la clase con los datos de entrenamiento
        self.datos_entrenamiento = datos_entrenamiento

    def distancia_euclidiana(self, punto1, punto2):
        # Calculamos la distancia euclidiana entre dos puntos
        return np.sqrt(np.sum((punto1 - punto2) ** 2))

    def clasificar(self, punto):
        # Creamos un diccionario para almacenar las distancias a los puntos de entrenamiento
        distancias = {}

        # Iteramos sobre cada punto en el conjunto de entrenamiento
        for fila in self.datos_entrenamiento:
            punto_entrenamiento = np.array(fila[:len(fila)-1], dtype=float)
            etiqueta = fila[len(fila)-1]
            
            # Calculamos la distancia entre el punto dado y el punto de entrenamiento
            distancia = self.distancia_euclidiana(punto, punto_entrenamiento)
            
            # Almacenamos la distancia y la etiqueta de la clase correspondiente
            distancias[etiqueta] = distancia
        
        # Encontramos la clase del punto de entrenamiento más cercano (el vecino más cercano)
        clase_calculada = min(distancias, key=distancias.get)
        return clase_calculada