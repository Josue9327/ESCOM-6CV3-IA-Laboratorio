import heapq
import time

#Heurística (distancia de Manhattan)
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#Función para calcular vecinos
def calcular_vecinos(nodo, maze):
    vecinos = []
    #Direcciones (derecha, abajo, izquierda, arriba)
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for direccion in direcciones:
        vecino = (nodo[0] + direccion[0], nodo[1] + direccion[1])
        #Comprobar si el vecino está dentro de los límites del laberinto y es transitable
        if 0 <= vecino[0] < len(maze) and 0 <= vecino[1] < len(maze[0]) and maze[vecino[0]][vecino[1]] == 0:
            vecinos.append(vecino)
    
    return vecinos


#Implementación del algoritmo A*
def a_star(maze, start, end):
    #Comenzamos a medir el tiempo
    start_time = time.perf_counter()

    #Cola de prioridad (lista abierta)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  #(costo, nodo)

    #Costo desde el inicio al nodo
    costos = {start: 0}

    #Diccionario para almacenar los padres y reconstruir el camino
    padres = {start: None}

    #Algoritmo A*
    while priority_queue:
        costo_actual, current = heapq.heappop(priority_queue)

        #Si llegamos al final, detenemos la búsqueda
        if current == end:
            break

        #Obtener vecinos del nodo actual
        vecinos = calcular_vecinos(current, maze)

        #Explorar vecinos
        for vecino in vecinos:
            nuevo_costo = costos[current] + 1  # Asumiendo que el costo entre nodos es siempre 1

            #Si es un nuevo nodo o se encuentra un camino más corto
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, end)
                heapq.heappush(priority_queue, (prioridad, vecino))
                padres[vecino] = current

    #Reconstruir el camino
    camino = []
    current = end
    while current:
        camino.append(current)
        current = padres[current]
    camino.reverse()
    
    #Detenemos la medición del tiempo
    end_time = time.perf_counter()

    #Calculamos y mostramos el tiempo total de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

    return camino



maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Posiciones de inicio y fin
inicio = (1, 0)  # Posición inicial
fin = (9, 6)     # Posición final


#Llamar al algoritmo A*
camino = a_star(maze, inicio, fin)
print("Ruta encontrada:", camino)

