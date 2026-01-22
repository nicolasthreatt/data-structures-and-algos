package design;

import java.util.ArrayDeque;

public class Deque<T> {

    private final ArrayDeque<T> items;

    public Deque() {
        items = new ArrayDeque<>();
    }

    public void addFront(T item) {
        items.addFirst(item);
    }

    public void addRear(T item) {
        items.addLast(item);
    }

    public T removeFront() {
        return items.pollFirst();  // returns null if empty
    }

    public T removeRear() {
        return items.pollLast();  // returns null if empty
    }

    public int size() {
        return items.size();
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }
}
