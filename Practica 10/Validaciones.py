import os
import random
class Validaciones:
    # Constructor de la clase donde inicializamos el dataset
    def __init__(self, nombreArchivo='bezdekIris.data'):
        self.matriz = self.inicializar_matriz(nombreArchivo)
    #Metodo para separar los datos en 70-30
    def hold_out(matriz):
        #Calculamos el numero de elementos que seran para prueba y entremamiento
        numDatosPrueba = round(len(matriz) * .30)
        numDatosEntrenamiento = len(matriz) - numDatosPrueba
        #Declaramos dos matrices para llenarlos con los datos que seran de prueba y entremamiento
        matrizPrueba = []
        matrizEntrenamiento = []
        #Con un bucle contamos hasta el limite de numero de datos de entrenamiento y de prueba
        #para con un numero aleatorio sacar de la matriz original una fila de datos con la cual llenar las matrices de prueba y entrenamiento
        for i in range(numDatosEntrenamiento):
            numero_aleatorio = random.randint(0, len(matriz) - 1)
            matrizEntrenamiento.append(matriz.pop(numero_aleatorio)) 
        for i in range(numDatosPrueba):
            numero_aleatorio = random.randint(0, len(matriz) - 1)
            matrizPrueba.append(matriz.pop(numero_aleatorio)) 
        #Retornamos las matrices de prueba y entrenamiento
        return matrizEntrenamiento, matrizPrueba
    def ten_fold_cross_validation(matriz):
        #Mezclamos los datos de manera aleatoria
        random.shuffle(matriz)
        #Calculamos el tamaño de cada fold
        tamano_fold = len(matriz) // 10
        folds = []
        #Dividimos los datos en 10 folds
        for i in range(10):
            inicio = i * tamano_fold
            if i == 9:
                folds.append(matriz[inicio:])
            else:
                folds.append(matriz[inicio:inicio + tamano_fold])
        #Retornamos los 10 folds
        return folds     
    def leave_one_out(matriz):
        folds = []
        for i in range(len(matriz)):
            #Dividimos los datos en dos i veces primero en una validación y el resto para entrenamiento
            datos_entrenamiento = matriz[:i] + matriz[i+1:]
            dato_validacion = matriz[i:i+1]
            folds.append((datos_entrenamiento, dato_validacion))
        #Retornamos las i tuplas en las cuales cada una contiene su conjunto de entrenamiento y su valor de validacion    
        return folds
    def inicializar_matriz(self, nombreArchivo):
        file_path = os.path.join(os.path.dirname(__file__), nombreArchivo)
        data_matrix = []
        with open(file_path, 'r') as file:
            for line in file:
                row = line.strip().split(',') 
                data_matrix.append(row)      
        return data_matrix    