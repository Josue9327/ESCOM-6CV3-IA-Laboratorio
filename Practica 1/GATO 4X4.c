#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void impresion(char gato[4][4]){
    printf("Estado del tablero:\n");
    for (int fila = 0; fila < 4; fila++) {
        for (int col = 0; col < 4; col++) {
            if (gato[fila][col] == 0)
                printf("| | ");
            else
                printf("|%c| ", gato[fila][col]);
        }
        printf("\n");
    }
}

int verificarx(int i,char gato[4][4]) {
    // Verificar filas
    for (int fila = 0; fila < 4; fila++) {
        if (gato[fila][0] == 'x' && gato[fila][1] == 'x' && gato[fila][2] == 'x' && gato[fila][3] == 'x') {
            printf("Ganador X en fila %d\n", fila);
            return i=8;
        }
    }
    // Verificar columnas
    for (int col = 0; col < 4; col++) {
        if (gato[0][col] == 'x' && gato[1][col] == 'x' && gato[2][col] == 'x' && gato[3][col] == 'x') {
            printf("Ganador X en columna %d\n", col);
            return i=8;
        }
    }
    // Verificar diagonal principal (de izquierda a derecha)
    if (gato[0][0] == 'x' && gato[1][1] == 'x' && gato[2][2] == 'x' && gato[3][3] == 'x') {
        printf("Ganador X en diagonal principal\n");
        return i=8;
    }
    // Verificar diagonal secundaria (de derecha a izquierda)
    if (gato[0][3] == 'x' && gato[1][2] == 'x' && gato[2][1] == 'x' && gato[3][0] == 'x') {
        printf("Ganador X en diagonal secundaria\n");
        return i=8;
    }
    else return i;

}

int verificaro(int i,char gato[4][4]) {
    for (int fila = 0; fila < 4; fila++) {
        if (gato[fila][0] == 'o' && gato[fila][1] == 'o' && gato[fila][2] == 'o' && gato[fila][3] == 'o') {
            printf("Ganador o en fila %d\n", fila);
            return i=8;
        }
    }
    for (int col = 0; col < 4; col++) {
        if (gato[0][col] == 'o' && gato[1][col] == 'o' && gato[2][col] == 'o' && gato[3][col] == 'o') {
            printf("Ganador o en columna %d\n", col);
            return i=8;
        }
    }
    if (gato[0][0] == 'o' && gato[1][1] == 'o' && gato[2][2] == 'o' && gato[3][3] == 'o') {
        printf("Ganador o en diagonal principal\n");
        return i=8;
    }
    if (gato[0][3] == 'o' && gato[1][2] == 'o' && gato[2][1] == 'o' && gato[3][0] == 'o') {
        printf("Ganador o en diagonal secundaria\n");
        return i=8;
    }
    else return i;

}

int main()
{
    char gato[4][4] = {0}; 
    int tiro[2];            
    int num1, num2;
    srand(time(NULL));  
    
    for (int i = 0; i < 8; i++) {
        impresion(gato);
        //Generar tirada
        do {
            num1 = rand() % 4;   
            num2 = rand() % 4;
        } while (gato[num1][num2] != 0); 
        printf("Máquina selecciona: %d, %d\n", num1, num2);
        // Marcar la selección 
        gato[num1][num2] = 'x';
        // Mostramos el tablero 
        impresion(gato);

        // Tiro jugador
        printf("Selecciona casilla (formato fila,columna):\n");
        scanf("%i,%i", &tiro[0], &tiro[1]);

        // Verificamos que la selección del jugador 
        if (tiro[0] >= 0 && tiro[0] < 4 && tiro[1] >= 0 && tiro[1] < 4) {
            // Si la casilla no está ocupada, la marcamos
            if (gato[tiro[0]][tiro[1]] == 0) {
                gato[tiro[0]][tiro[1]] = 'o'; 
                printf("Seleccionaste la casilla: %d, %d\n", tiro[0], tiro[1]);
            } else {
                printf("Casilla ocupada, selecciona otra.\n");
            }
        } else {
            printf("Coordenadas fuera de rango. Deben estar entre 0 y 3.\n");
        }
        i = verificarx(i, gato);
        i = verificaro(i, gato);
    }

    return 0;
}
