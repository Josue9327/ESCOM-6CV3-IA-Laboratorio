from Validaciones import Validaciones
from bayes import NaiveBayes
import numpy as np
archivo = 'synthetic_classification_dataset.csv'
##########################   Naive Bayes con hold:out   ######################################
def b_hold_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Dividimos el dataset con hold_out
    matrizEntrenamiento, matrizPrueba = Validaciones.hold_out(objeto.matriz)
    # Creamos una instancia del clasificador Naive Bayes y lo entrenamos
    clasificador = NaiveBayes()
    clasificador.entrenar(matrizEntrenamiento)
    # Clasificamos los puntos de prueba
    aciertos = 0
    for punto in matrizPrueba:
        punto_a_clasificar = np.array(punto[:-1], dtype=float)
        clase_real = punto[-1]
        clase_predicha = clasificador.predecir(punto_a_clasificar)
        if clase_predicha == clase_real:
            aciertos += 1   
    # Calculamos la exactitud
    exactitud = aciertos / len(matrizPrueba)
    print(f"Exactitud promedio del modelo con hold_out cross-validation: {exactitud * 100:.2f}%")
##########################   Naive Bayes con ten_fold_cross_validation   ######################
def b_cross_validation():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Realizamos el 10-fold cross-validation
    folds = Validaciones.ten_fold_cross_validation(objeto.matriz)
    aciertos = 0
    total = 0
    # Iteramos el 10-fold cross-validation
    for i in range(10):
        # Definimos conjunto de prueba y entrenamiento
        matriz_prueba = folds[i]
        folds_entrenamiento = folds[:i] + folds[i + 1:]
        matriz_entrenamiento = []
        for fold in folds_entrenamiento:
            matriz_entrenamiento.extend(fold)
        # Entrenamos el clasificador Naive Bayes
        clasificador = NaiveBayes()
        clasificador.entrenar(matriz_entrenamiento)
        # Clasificamos cada punto de prueba y contamos los aciertos
        for punto in matriz_prueba:
            punto_a_clasificar = np.array(punto[:-1], dtype=float)
            clase_real = punto[-1]
            clase_predicha = clasificador.predecir(punto_a_clasificar)
            if clase_predicha == clase_real:
                aciertos += 1
            total += 1   
    # Calculamos la exactitud
    exactitud = aciertos / total
    print(f"Exactitud promedio del clasificador con ten-fold cross-validation: {exactitud * 100:.2f}%")
##########################   Naive Bayes con leave_one_out   #################################
def b_leave_one_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Realizamos la validación Leave-One-Out
    folds = Validaciones.leave_one_out(objeto.matriz)
    aciertos = 0
    total = 0
    # Iteramos sobre los folds de Leave-One-Out
    for matriz_entrenamiento, matriz_prueba in folds:
        # Entrenamos el clasificador Naive Bayes
        clasificador = NaiveBayes()
        clasificador.entrenar(matriz_entrenamiento)
        # Clasificamos el punto de prueba y contamos los aciertos
        for punto in matriz_prueba:
            punto_a_clasificar = np.array(punto[:-1], dtype=float)
            clase_real = punto[-1]
            clase_predicha = clasificador.predecir(punto_a_clasificar)
            if clase_predicha == clase_real:
                aciertos += 1
            total += 1    
    # Calculamos la exactitud
    exactitud = aciertos / total
    print(f"Exactitud promedio del modelo con Leave-One-Out cross-validation: {exactitud * 100:.2f}%")
# Ejecutamos las funciones con el clasificador Naive Bayes
b_hold_out()
b_cross_validation()
b_leave_one_out()