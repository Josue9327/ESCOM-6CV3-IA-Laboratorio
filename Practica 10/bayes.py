import numpy as np
from collections import defaultdict
from collections import Counter
from math import log, exp
class NaiveBayes:
    def __init__(self):
        # Diccionarios para almacenar probabilidades por clase
        self.probabilidades_clase = {}
        self.probabilidades_condicionales = defaultdict(lambda: defaultdict(float))
        self.clases = set()
    def entrenar(self, datos_entrenamiento):  
        # Contar ocurrencias por clase
        conteos_clase = Counter([fila[-1] for fila in datos_entrenamiento])
        total_muestras = len(datos_entrenamiento)
        self.clases = set(conteos_clase.keys())       
        # Calcular probabilidad de cada clase
        for clase, conteo in conteos_clase.items():
            self.probabilidades_clase[clase] = conteo / total_muestras
        # Calcular las probabilidades condicionales para cada atributo dado la clase
        for clase in self.clases:
            muestras_clase = [fila[:-1] for fila in datos_entrenamiento if fila[-1] == clase]
            muestras_clase = np.array(muestras_clase, dtype=float)
            media = np.mean(muestras_clase, axis=0)
            varianza = np.var(muestras_clase, axis=0)
            # Evitar problemas de división por cero añadiendo un pequeño valor a la varianza
            varianza[varianza == 0] = 1e-9
            self.probabilidades_condicionales[clase] = {
                "media": media,
                "varianza": varianza
            }
    def calcular_probabilidad_condicional(self, x, media, varianza):       
        coeficiente = 1 / np.sqrt(2 * np.pi * varianza)
        exponente = exp(-((x - media) ** 2) / (2 * varianza))
        return coeficiente * exponente
    def predecir(self, punto):       
        probabilidades_posteriores = {}       
        for clase in self.clases:
            # Inicializar con la probabilidad de la clase (prior)
            probabilidad_clase = log(self.probabilidades_clase[clase])           
            # Agregar las probabilidades condicionales para cada atributo
            media = self.probabilidades_condicionales[clase]["media"]
            varianza = self.probabilidades_condicionales[clase]["varianza"]          
            for i in range(len(punto)):
                probabilidad_clase += log(
                    self.calcular_probabilidad_condicional(punto[i], media[i], varianza[i])
                )         
            probabilidades_posteriores[clase] = probabilidad_clase    
        # Elegir la clase con mayor probabilidad posterior
        return max(probabilidades_posteriores, key=probabilidades_posteriores.get)