import java.util.*;
public class BusquedaLaberinto {
    private static final int[] estadoObjetivo = {0,1};
    private static final int[] estadoInicial = {3,4};
    public static void main(String[] args) {
        Nodo nodoActual = new Nodo(estadoInicial, "");
        if (dfs(nodoActual)) {
            System.out.println("Solucion encontrada");
        } else {
            System.out.println("Sin solucion");
        }
    }
    private static boolean dfs(Nodo nodoInicial) {
        Set<String> nodosVisitados = new HashSet<>();
        String estadoObjetivoString = Arrays.toString(estadoObjetivo);
        //Stack<Nodo> nodosFrontera = calcularNodosFrontera(nodoInicial);
        Stack<Nodo> nodosFrontera = new Stack<>();
        nodosFrontera.push(nodoInicial);
        while (!nodosFrontera.isEmpty()) {
            Nodo nodoActual = nodosFrontera.pop();
            String estadoString = Arrays.toString(nodoActual.estado);
            System.out.println(nodoActual.imprimirNodo());
            if(estadoString.equals(estadoObjetivoString)){
                return true;
            }

            nodosVisitados.add(estadoString);
            Stack<Nodo> nodosHijos = calcularNodosHijos(nodoActual);
            for (Nodo nodo : nodosHijos) {
                String hijoEstadoString = Arrays.toString(nodo.estado);
                if(!nodosVisitados.contains(hijoEstadoString) && !nodosFrontera.contains(nodo)){
                    nodosFrontera.push(nodo);
                }
            }
        }
        return false;
    }
    private static Stack<Nodo> calcularNodosHijos(Nodo nodo){
        Stack<Nodo> nodosFrontera = new Stack<>();
        nodosFrontera.push(operacionI(nodo));
        nodosFrontera.push(operacionC(nodo));
        nodosFrontera.push(operacionD(nodo));
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
        hijo.camino += "-C";  // Agregamos "C" al camino para representar la operación
        return hijo;
    }
    
    private static Nodo operacionD(Nodo estado) {
        Nodo hijo = new Nodo(estado);
        int aux = hijo.estado[2];
        hijo.estado[2] = hijo.estado[3];
        hijo.estado[3] = aux;
        hijo.camino += "-D";  // Agregamos "D" al camino para representar la operación
        return hijo;
    }
}
