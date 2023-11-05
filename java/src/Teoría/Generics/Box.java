package Teoría.Generics;

public class Box<T> {
    private T content;

    public void put(T item) {
        this.content = item;
    }

    public T get() {
        return this.content;
    }
}
