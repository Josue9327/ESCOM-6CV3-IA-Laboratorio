import java.util.*;

public class BusquedaPuzzle {
    private static final int[] estadoObjetivo = {1, 2, 3, 4};
    private static final int[] estadoInicial = {4, 1, 2, 3};

    public static void main(String[] args) {
        Nodo nodoActual = new Nodo(estadoInicial, "");
        if (bfs(nodoActual)) {
            System.out.println("Solución encontrada");
        } else {
            System.out.println("Sin solución");
        }
    }

    private static boolean bfs(Nodo nodoInicial) {
        Set<String> nodosVisitados = new HashSet<>();
        String estadoObjetivoString = Arrays.toString(estadoObjetivo);
        
        Queue<Nodo> nodosFrontera = new LinkedList<>();
        nodosFrontera.add(nodoInicial);
        
        while (!nodosFrontera.isEmpty()) {
            Nodo nodoActual = nodosFrontera.poll();
            String estadoString = Arrays.toString(nodoActual.estado);
            System.out.println(nodoActual.imprimirNodo());
            
            if (estadoString.equals(estadoObjetivoString)) {
                return true;
            }

            nodosVisitados.add(estadoString);
            Queue<Nodo> nodosHijos = calcularNodosHijos(nodoActual);
            
            for (Nodo nodo : nodosHijos) {
                String hijoEstadoString = Arrays.toString(nodo.estado);
                if (!nodosVisitados.contains(hijoEstadoString) && !nodosFrontera.contains(nodo)) {
                    nodosFrontera.add(nodo);
                }
            }
        }
        return false;
    }

    private static Queue<Nodo> calcularNodosHijos(Nodo nodo) {
        Queue<Nodo> nodosFrontera = new LinkedList<>();
        nodosFrontera.add(operacionI(nodo));
        nodosFrontera.add(operacionC(nodo));
        nodosFrontera.add(operacionD(nodo));
        return nodosFrontera;
    }

    private static Nodo operacionI(Nodo estado) {
        Nodo hijo = new Nodo(estado);
        int aux = hijo.estado[0];
        hijo.estado[0] = hijo.estado[1];
        hijo.estado[1] = aux;
        hijo.camino += "-I";  // Agregamos "I" al camino para representar la operación
        return hijo;
    }

    private static Nodo operacionC(Nodo estado) {
        Nodo hijo = new Nodo(estado);
        int aux = hijo.estado[1];
        hijo.estado[1] = hijo.estado[2];
        hijo.estado[2] = aux;
        hijo.camino += "-C";
        return hijo;
    }

    private static Nodo operacionD(Nodo estado) {
        Nodo hijo = new Nodo(estado);
        int aux = hijo.estado[2];
        hijo.estado[2] = hijo.estado[3];
        hijo.estado[3] = aux;
        hijo.camino += "-D";
        return hijo;
    }
}
