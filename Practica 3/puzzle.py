from collections import deque

laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

#Coordenadas de inicio y meta
inicio = (0, 1)
meta = (3, 4)

#Direcciones posibles de movimiento (arriba, abajo, izquierda, derecha)
movimiento = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#Verifica si el movimiento es válido dentro del laberinto
def is_valid_move(x, y):
    dentroLimite = 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0])
    caminoValido = dentroLimite and laberinto[x][y] == 0
    return caminoValido

def bfs(laberinto, inicio, meta):
    """Realiza una búsqueda en amplitud para encontrar un camino."""
    #Cola para BFS, inicializamos con el nodo de inicio
    cola = deque([(inicio, [inicio])])
    
    #Mientras haya elementos en la cola
    while cola:
        (x, y), camino = cola.popleft()  # Extrae el nodo actual y el camino recorrido
        
        #Si llegamos a la meta, devolvemos el camino
        if (x, y) == meta:
            return camino
        
        #Marcamos la posición actual como visitada
        laberinto[x][y] = 1
        
        #Iteramos en cada dirección posible
        for direction in movimiento:
            next_x, next_y = x + direction[0], y + direction[1]
            
            if is_valid_move(next_x, next_y):
                #Si el movimiento es válido, lo agregamos a la cola junto con el camino actualizado
                cola.append(((next_x, next_y), camino + [(next_x, next_y)]))
    
    #Si no encontramos ningún camino
    return None

#Ejecutar BFS
solution = bfs(laberinto, inicio, meta)
if solution:
    print("Camino encontrado:", solution)
else:
    print("No se encontró un camino.")
