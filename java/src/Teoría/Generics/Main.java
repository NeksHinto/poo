package Teoría.Generics;

public class Main {
    public static void main(String[] args) {
        Box<String> stringBox = new Box<>();
        stringBox.put("Hola, soy un string.");
        System.out.println(stringBox.get());

        Box<Integer> integerBox = new Box<>();
        integerBox.put(123);
        System.out.println(integerBox.get());
    }
}