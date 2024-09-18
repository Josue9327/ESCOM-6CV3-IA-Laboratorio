import java.util.*;

class Nodo {
    int[] estado;
    String camino;
    boolean disponible;

    public Nodo(int[] estado, String camino) {
        this.estado = estado.clone();  // Hacemos una copia del array para evitar referencias.
        this.camino = camino;
    }
    public Nodo(int[] estado, String camino, boolean disponible) {
        this.estado = estado.clone();  // Hacemos una copia del array para evitar referencias.
        this.camino = camino;
        this.disponible = disponible;
    }

    public Nodo(Nodo otro) {
        this.estado = otro.estado.clone();  // Copiar el estado para no modificar el original.
        this.camino = otro.camino;
    }

    public String imprimirNodo() {
        return Arrays.toString(estado) + " | Movimiendo: " + camino;
    }
}
