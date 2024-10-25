def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def check_winner(board, player):
    # Verificar filas, columnas y diagonales
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(4):
        if all([board[row][col] == player for row in range(4)]):
            return True

    if all([board[i][i] == player for i in range(4)]) or all([board[i][3 - i] == player for i in range(4)]):
        return True

    return False
    
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# Función para la IA (Minimax con poda Alfa-Beta)
def minimax(board, depth, is_maximizing, alpha, beta, max_depth=4):
    if check_winner(board, "X"):
        return 1  # Ganador Max (jugador)
    elif check_winner(board, "O"):
        return -1  # Ganador Min (IA)
    elif check_draw(board):
        return 0  # Empate

    # Agregar límite de profundidad
    if depth >= max_depth:
        return 0  # Limita la profundidad de búsqueda para evitar que se quede colgado

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(4):
            for j in range(4):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta, max_depth)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(4):
            for j in range(4):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta, max_depth)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Función para que la IA elija la mejor jugada
def best_move(board):
    best_value = float('inf')  # Queremos minimizar para la IA
    move = (-1, -1)
    for i in range(4):
        for j in range(4):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = minimax(board, 0, True, -float('inf'), float('inf'))
                board[i][j] = " "
                if move_value < best_value:
                    best_value = move_value
                    move = (i, j)
    return move

def best_moveX(board):
    best_value = float('inf')  # Queremos minimizar para la IA
    move = (-1, -1)
    for i in range(4):
        for j in range(4):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_value = minimax(board, 0, True, -float('inf'), float('inf'))
                board[i][j] = " "
                if move_value < best_value:
                    best_value = move_value
                    move = (i, j)
    return move

    
def p_vs_p():
    board = [[" " for _ in range(4)] for _ in range(4)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"Turno del jugador {current_player}")
        
        # Solicitar al jugador la posición donde desea marcar, con validación
        while True:
            row = int(input("Ingresa la fila (0-3): "))
            if 0 <= row <= 3:
                break
            else:
                print("Fila inválida. Debe estar entre 0 y 3. Intenta otra vez.")
        
        while True:
            col = int(input("Ingresa la columna (0-3): "))
            if 0 <= col <= 3:
                break
            else:
                print("Columna inválida. Debe estar entre 0 y 3. Intenta otra vez.")

        # Validar si la posición es válida
        if board[row][col] != " ":
            print("Posición ya ocupada, intenta otra vez.")
            continue

        # Marcar la posición en el tablero
        board[row][col] = current_player

        # Verificar si hay ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} gana!")
            break

        # Verificar si es empate
        if check_draw(board):
            print_board(board)
            print("¡Es un empate!")
            break

        # Cambiar de jugador
        current_player = "O" if current_player == "X" else "X"
        
def p_vs_ai():
    board = [[" " for _ in range(4)] for _ in range(4)]
    current_player = "X"  # El jugador siempre empieza

    while True:
        print_board(board)
        if current_player == "X":
            print(f"Turno del jugador {current_player}")
            
            # Solicitar al jugador la posición donde desea marcar, con validación
            while True:
                row = int(input("Ingresa la fila (0-3): "))
                if 0 <= row <= 3:
                    break
                else:
                    print("Fila inválida. Debe estar entre 0 y 3. Intenta otra vez.")
            
            while True:
                col = int(input("Ingresa la columna (0-3): "))
                if 0 <= col <= 3:
                    break
                else:
                    print("Columna inválida. Debe estar entre 0 y 3. Intenta otra vez.")

            # Validar si la posición es válida
            if board[row][col] != " ":
                print("Posición ya ocupada, intenta otra vez.")
                continue

            # Marcar la posición en el tablero
            board[row][col] = "X"

        else:
            # Turno de la IA
            print("Turno de la IA (O)")
            row, col = best_move(board)
            board[row][col] = "O"

        # Verificar si hay ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} gana!")
            break

        # Verificar si es empate
        if check_draw(board):
            print_board(board)
            print("¡Es un empate!")
            break

        # Cambiar de jugador
        current_player = "O" if current_player == "X" else "X"
        
def ai_vs_ai():
    board = [[" " for _ in range(4)] for _ in range(4)]
    current_player = "X"  # IA X empieza

    while True:
        print_board(board)
        if current_player == "X":
            print(f"Turno del jugador {current_player}")
            row, col = best_move(board)
            board[row][col] = "X"

        else:
            # Turno de la IA
            print(f"Turno del jugador {current_player}")
            row, col = best_move(board)
            board[row][col] = "O"

        # Verificar si hay ganador
        if check_winner(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} gana!")
            break

        # Verificar si es empate
        if check_draw(board):
            print_board(board)
            print("¡Es un empate!")
            break

        # Cambiar de jugador
        current_player = "O" if current_player == "X" else "X"
        
def tic_tac_toe():
    Modo = None
    
    while True:
        Modo = int(input("Selecciona modo de juego \n 1.- Jugador vs Jugador \n 2.- Jugador vs IA \n 3.- IA vs IA \n 4.- Salir \n"))
        if 1 <= Modo <= 4:
            break
        else:
            print("Opción no válida. Por favor ingresa un número entre 1 y 4.")

    match Modo:
        case 1:
            print("Jugador vs Jugador")
            p_vs_p()
        case 2:
            print("Jugador vs IA")
            p_vs_ai()
        case 3:
            print("IA vs IA")
            ai_vs_ai()
        case 4:
            print("Adiós")
            exit()

tic_tac_toe()
