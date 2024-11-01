public class App {
    public static void main(String[] args) {
        Dataset loader = new Dataset();
        try {
            loader.cargarDatos("bezdekIris.DATA");
            String[][] dataMatrix = loader.obtenerMatriz();
            for (String[] row : dataMatrix) {
                for (String valor : row) {
                    System.out.print(valor + "\t");
                }
                System.out.println();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
