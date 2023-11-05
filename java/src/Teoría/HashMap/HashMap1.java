package Teoría.HashMap;

import java.util.HashMap;

public class HashMap1 {
    public static void main(String[] args) {
        // Crear un objeto HashMap
        HashMap<String, Integer> map = new HashMap<>();

        // Agregar elementos al HashMap
        map.put("Uno", 1);
        map.put("Dos", 2);
        map.put("Tres", 3);

        // Acceder a un valor específico
        System.out.println("El valor asociado con 'Dos' es: " + map.get("Dos"));
    }
}
