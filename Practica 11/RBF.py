from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from Validaciones import Validaciones
import numpy as np

archivo = 'synthetic_classification_dataset.csv'

##########################   Red Neuronal RBF con hold-out   ######################################
def RBF_hold_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Dividimos el dataset con hold-out:
    matrizEntrenamiento, matrizPrueba = Validaciones.hold_out(objeto.matriz)
    # Separamos los datos y la clase de las matrices de entrenamiento y prueba
    Xprueba = [fila[:-1] for fila in matrizPrueba]
    yprueba = [fila[-1] for fila in matrizPrueba]
    Xentrenamiento = [fila[:-1] for fila in matrizEntrenamiento]
    yentrenamiento = [fila[-1] for fila in matrizEntrenamiento]
    # Convertimos las clases y datos a números
    Xentrenamiento_numerico = np.array(Xentrenamiento, dtype=float)
    Xprueba_numerico = np.array(Xprueba, dtype=float)
    label_encoder = LabelEncoder()
    yprueba_numerico = label_encoder.fit_transform(yprueba)
    yentrenamiento_numerico = label_encoder.transform(yentrenamiento)
    # Creamos el modelo RBF (usamos SVC con kernel radial)
    rbf = SVC(kernel='rbf', gamma='scale', random_state=42)
    # Entrenamos el modelo
    rbf.fit(Xentrenamiento_numerico, yentrenamiento_numerico)
    # Realizamos predicciones con la matriz de prueba
    y_pred = rbf.predict(Xprueba_numerico)
    # Evaluamos el modelo
    accuracy = accuracy_score(yprueba_numerico, y_pred)
    print(f"Precisión de Red Neuronal RBF con hold-out: {accuracy * 100:.2f}%")

##########################   Red Neuronal RBF con ten-fold cross-validation ######################################
def RBF_ten_fold_cross_validation():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Convertimos las clases a números
    X = [fila[:-1] for fila in objeto.matriz]
    y = [fila[-1] for fila in objeto.matriz]
    label_encoder = LabelEncoder()
    y_numerico = label_encoder.fit_transform(y)
    # Actualizamos la matriz con etiquetas numéricas
    matriz_numerica = [fila[:-1] + [y_numerico[i]] for i, fila in enumerate(objeto.matriz)]
    # Generamos los folds usando la matriz numérica
    folds = Validaciones.ten_fold_cross_validation(matriz_numerica)
    evaluaciones = []
    # Iteramos sobre los 10 folds
    for i in range(10):
        # Definimos conjunto de prueba y entrenamiento
        matriz_prueba = folds[i]
        folds_entrenamiento = folds[:i] + folds[i + 1:]
        matriz_entrenamiento = [fila for fold in folds_entrenamiento for fila in fold]
        # Separamos características y etiquetas
        X_entrenamiento = [fila[:-1] for fila in matriz_entrenamiento]
        y_entrenamiento = [fila[-1] for fila in matriz_entrenamiento]
        X_prueba = [fila[:-1] for fila in matriz_prueba]
        y_prueba = [fila[-1] for fila in matriz_prueba]
        # Convertimos a matrices NumPy
        X_entrenamiento_numerico = np.array(X_entrenamiento, dtype=float)
        X_prueba_numerico = np.array(X_prueba, dtype=float)
        y_entrenamiento_numerico = np.array(y_entrenamiento, dtype=int)
        y_prueba_numerico = np.array(y_prueba, dtype=int)
        # Creamos y entrenamos el modelo RBF
        rbf = SVC(kernel='rbf', gamma='scale', random_state=42)
        rbf.fit(X_entrenamiento_numerico, y_entrenamiento_numerico)
        # Realizamos predicciones con la matriz de prueba y evaluamos la precisión
        y_pred = rbf.predict(X_prueba_numerico)
        accuracy = accuracy_score(y_prueba_numerico, y_pred)
        evaluaciones.append(accuracy)
    # Calculamos la precisión promedio
    promedio = np.mean(evaluaciones) * 100
    print(f"\nPrecisión Promedio de Red Neuronal RBF con ten-fold cross-validation: {promedio:.2f}%")

##########################   Red Neuronal RBF con leave-one-out ######################################
def RBF_leave_one_out():
    # Cargamos la matriz
    objeto = Validaciones(archivo)
    # Separamos características y etiquetas
    X = [fila[:-1] for fila in objeto.matriz]
    y = [fila[-1] for fila in objeto.matriz]
    # Convertimos clases a números
    label_encoder = LabelEncoder()
    y_numerico = label_encoder.fit_transform(y)
    # Actualizamos la matriz con etiquetas numéricas
    matriz_numerica = [fila[:-1] + [y_numerico[i]] for i, fila in enumerate(objeto.matriz)]
    # Generamos los folds usando Leave-One-Out
    folds = Validaciones.leave_one_out(matriz_numerica)
    evaluaciones = []
    # Iteramos sobre cada fold
    for matriz_entrenamiento, matriz_prueba in folds:
        # Separamos características y etiquetas para entrenamiento y prueba
        X_entrenamiento = [fila[:-1] for fila in matriz_entrenamiento]
        y_entrenamiento = [fila[-1] for fila in matriz_entrenamiento]
        X_prueba = [fila[:-1] for fila in matriz_prueba]
        y_prueba = [fila[-1] for fila in matriz_prueba]
        # Convertimos las características a números
        X_entrenamiento_numerico = np.array(X_entrenamiento, dtype=float)
        X_prueba_numerico = np.array(X_prueba, dtype=float)
        y_entrenamiento_numerico = np.array(y_entrenamiento, dtype=int)
        y_prueba_numerico = np.array(y_prueba, dtype=int)
        # Creamos y entrenamos el modelo RBF
        rbf = SVC(kernel='rbf', gamma='scale', random_state=42)
        rbf.fit(X_entrenamiento_numerico, y_entrenamiento_numerico)
        # Realizamos predicciones con el conjunto de prueba y calculamos la precisión
        y_pred = rbf.predict(X_prueba_numerico)
        accuracy = accuracy_score(y_prueba_numerico, y_pred)
        evaluaciones.append(accuracy)
    # Calculamos y mostramos la precisión promedio
    promedio = np.mean(evaluaciones) * 100
    print(f"\nPrecisión Promedio de Red Neuronal RBF con leave-one-out: {promedio:.2f}%")

# Llamamos a las funciones
RBF_hold_out()
RBF_ten_fold_cross_validation()
RBF_leave_one_out()
