import java.util.*;

class Nodo {
    int[] estado;
    String camino;

    public Nodo(int[] estado, String camino) {
        this.estado = estado.clone();  // Hacemos una copia del array para evitar referencias.
        this.camino = camino;
    }

    public Nodo(Nodo otro) {
        this.estado = otro.estado.clone();
        this.camino = otro.camino;
    }

    public String imprimirNodo() {
        return Arrays.toString(estado) + " | Movimiendo: " + camino;
    }
}