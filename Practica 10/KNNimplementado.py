from Validaciones import Validaciones
from KNN import KNN  
import numpy as np

archivo = 'bezdekIris.data'

##########################   KNN con hold:out   ######################################
def knn_hold_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Dividimos el dataset con hold_out
    matrizEntrenamiento, matrizPrueba = Validaciones.hold_out(objeto.matriz)
    # Creamos una instancia del clasificador 1NN
    clasificador = KNN(matrizEntrenamiento, 3)
    # Probamos el dataset de prueba
    matrizClasificada = []
    for puntos in matrizPrueba:
        clase_calculada = clasificador.clasificar(np.array(puntos[:-1], dtype=float))  # Usamos clasificar
        matrizClasificada.append(np.array(puntos[:-1] + [clase_calculada]))
    # Calculamos su grado de exactitud y la matriz de confusión
    aciertos = 0
    for i in range(len(matrizPrueba)):
        iguales = np.array_equal(matrizClasificada[i], matrizPrueba[i])
        if iguales:
            aciertos += 1
    exactitud = aciertos / len(matrizPrueba)
    print(f"Exactitud promedio del modelo con hold_out cross validation: {exactitud * 100:.2f}%")

##########################   KNN con ten_fold_cross_validation   ######################################
def knn_cross_validation():
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
        # Entrenamos el clasificador KNN
        clasificador = KNN(matriz_entrenamiento, 3)

        # Clasificamos cada punto de prueba y contamos los aciertos
        for punto in matriz_prueba:
            punto_a_clasificar = np.array(punto[:-1], dtype=float)
            clase_real = punto[-1]
            clase_predicha = clasificador.clasificar(punto_a_clasificar)  # Usamos clasificar

            if clase_predicha == clase_real:
                aciertos += 1
            total += 1
    # Calculamos la exactitud
    exactitud = aciertos / total
    print(f"Exactitud promedio del clasificador con ten-fold cross-validation: {exactitud * 100:.2f}%")

##########################   KNN con leave_one_out   ######################################
def knn_leave_one_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Realizamos la validación Leave-One-Out
    folds = Validaciones.leave_one_out(objeto.matriz)
    aciertos = 0
    total = 0

    # Iteramos sobre los folds de Leave-One-Out
    for matriz_entrenamiento, matriz_prueba in folds:
        # Entrenamos el clasificador KNN
        clasificador = KNN(matriz_entrenamiento, 3)

        # Clasificamos el punto de prueba y contamos los aciertos
        for punto in matriz_prueba:
            punto_a_clasificar = np.array(punto[:-1], dtype=float)
            clase_real = punto[-1]
            clase_predicha = clasificador.clasificar(punto_a_clasificar)  # Usamos clasificar

            if clase_predicha == clase_real:
                aciertos += 1
            total += 1

    # Calculamos la exactitud
    exactitud = aciertos / total
    print(f"Exactitud promedio del modelo con Leave-One-Out cross-validation: {exactitud * 100:.2f}%")

# Ejecutamos las funciones con el clasificador KNN
knn_hold_out()
knn_cross_validation()
knn_leave_one_out()
