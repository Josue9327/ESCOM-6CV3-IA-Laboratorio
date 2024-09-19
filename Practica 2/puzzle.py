#Laberinto
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


def dfs(laberinto, inicio, meta, camino=[]):
    """Realiza una búsqueda en profundidad para encontrar un camino."""
    x, y = inicio
    camino.append(inicio)  #Agrega la posición actual al camino

    #Si llegamos a la meta, devuelve el camino
    if inicio == meta:
        return camino

    #Marca la posición actual como visitada
    laberinto[x][y] = 1

    #Iteramos en cada direccion posible
    for direction in movimiento:
        next_x, next_y = x + direction[0], y + direction[1]
        if is_valid_move(next_x, next_y):
            result = dfs(laberinto, (next_x, next_y), meta, camino)
            if result:  #Si encontramos un camino, lo devolvemos
                return result

    #Retrocedemos si no hay camino disponible
    camino.pop()
    return None

#Ejecutar DFS
solution = dfs(laberinto, inicio, meta)
if solution:
    print("Camino encontrado:", solution)
else:
    print("No se encontró un camino.")
