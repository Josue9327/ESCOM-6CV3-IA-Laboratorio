import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Dataset{
    String[][] Matriz;
    //Cargar datos del archivo .DATA
    public void cargarDatos(String archivoRuta){
        try{
            List<String[]> dataList = new ArrayList<>();
            //Leer y almacenar cada línea en una lista temporal
            BufferedReader reader = new BufferedReader(new FileReader(archivoRuta));
            String line;
            while ((line = reader.readLine()) != null) {
                String[] values = line.split(",");
                dataList.add(values);
            }
            reader.close();

            // Transferir los datos de la lista temporal a una matriz
            int rows = dataList.size();
            int columns = dataList.get(0).length; // Suponemos que todas las filas tienen el mismo número de columnas
            Matriz = new String[rows][columns];
            for (int i = 0; i < rows; i++) {
                Matriz[i] = dataList.get(i);
            }
        }catch(IOException e){
            System.out.println(e.getMessage());
        }
        
    }

    public String[][] obtenerMatriz() {
        return Matriz;
    }
}
