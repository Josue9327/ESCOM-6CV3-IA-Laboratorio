import numpy as np

class Euclidiano:
    def __init__(self, datos_entrenamiento):
        #Inicializamos la clase con los datos de entrenamiento
        self.datos_entrenamiento = datos_entrenamiento
        self.vector_promedio = self.calcular_vector_promedio()

    def calcular_vector_promedio(self):
        #Creamos un diccionario para almacenar los datos agrupándolos por clase
        clases = {}
        #Iteramos sobre cada fila y agregamos al diccionario la clase si aun no está y sus puntos
        for fila in self.datos_entrenamiento:
            punto = np.array(fila[:len(fila)-1], dtype=float)
            etiqueta = fila[len(fila)-1]
            if etiqueta not in clases:
                clases[etiqueta] = []
            clases[etiqueta].append(punto)
        
        #Calculamos el vector promedio de cada clase
        vector_promedio = {}
        for etiqueta, puntos in clases.items():
            vector_promedio[etiqueta] = np.mean(puntos, axis=0)
        
        return vector_promedio
    def distancia_euclidiana(self, punto1, punto2):
        return np.sqrt(np.sum((punto1 - punto2) ** 2))

    def clasificar_por_vector_promedio(self, punto):
        #Creamos un diccionario vacío para almacenar las distancias
        distancias = {}
        
        #Iteramos sobre cada etiqueta y vector promedio
        for etiqueta, punto_promedio in self.vector_promedio.items():
            #Calculamos la distancia euclidiana entre el punto y el vector promedio
            distancia = self.distancia_euclidiana(punto, punto_promedio)
            #Asignamos la distancia calculada al diccionario bajo la llave de la etiqueta correspondiente
            distancias[etiqueta] = distancia
        
        #Buscamos la clase con la distancia más corta
        clase_calculada = min(distancias, key=distancias.get)
        return clase_calculada