package design;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Stack<T> {

    private final List<T> items;

    public Stack() {
        items = new ArrayList<>();
    }

    public void push(T item) {
        items.add(item);
    }

    public Optional<T> pop() {
        if (items.isEmpty()) return Optional.empty();

        return Optional.of(items.remove(items.size() - 1));       // top of the stack
    }

    public Optional<T> peek() {
        if (items.isEmpty()) return Optional.empty();

        return Optional.ofNullable(items.get(items.size() - 1));  // top of the stack
    }

    public int size() {
        return items.size();
    }

    public boolean isEmpty() {
        return items.size() == 0;
    }
}
