package Teoría.HashMap;

import java.util.HashMap;
import java.util.Map;

public class HashMap2 {
    public static void main(String[] args) {
        // Crear un objeto HashMap
        HashMap<String, Integer> map = new HashMap<>();

        // Agregar elementos al HashMap
        map.put("Uno", 1);
        map.put("Dos", 2);
        map.put("Tres", 3);

        // Recorrer el HashMap usando un loop for-each
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            System.out.println("Clave = " + entry.getKey() + ", Valor = " + entry.getValue());
        }
    }
}
