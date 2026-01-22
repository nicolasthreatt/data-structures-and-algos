#include <cassert>
#include <string>
#include <optional>
#include <vector>

template <typename T>
class Stack {
private:
    std::vector<T> items = {};

public:
    Stack() = default;  // Constructor

    void push(const T& item) {
        items.push_back(item);
    }

    std::optional<T> pop() {
        if (items.empty()) return std::nullopt;

        T item = items.back();
        items.pop_back();
        return item;
    }

    std::optional<T> peek() {
        if (items.empty()) return std::nullopt;

        return items.back();   // top of the stack
    }

    size_t size() const {
        return items.size();
    }

    bool isEmpty() const {
        return items.empty();
    }
};

int main() {
    Stack<int> stack;

    assert(stack.isEmpty() == true);
    assert(stack.size() == 0);
    assert(!stack.pop().has_value());
    assert(!stack.peek().has_value());

    stack.push(1);
    assert(stack.isEmpty() == false);
    assert(stack.size() == 1);
    assert(stack.peek().value() == 1);

    stack.push(2);
    assert(stack.size() == 2);
    assert(stack.peek().value() == 2);

    assert(stack.pop().value() == 2);
    assert(stack.size() == 1);
    assert(stack.peek().value() == 1);

    assert(stack.pop().value() == 1);
    assert(stack.isEmpty() == true);
    assert(!stack.pop().has_value());
    assert(!stack.peek().has_value());

    stack.push(10);
    stack.push(20);
    stack.push(30);

    assert(stack.peek().value() == 30);
    assert(stack.pop().value() == 30);
    assert(stack.peek().value() == 20);
    assert(stack.size() == 2);

    Stack<std::string> s2;
    s2.push("hello");
    assert(s2.peek().value() == "hello");
    assert(s2.pop().value() == "hello");
    assert(s2.isEmpty() == true);

    Stack<double> s3;
    s3.push(3.14);
    assert(s3.pop().value() == 3.14);
    assert(s3.isEmpty() == true);

    return 0;
}
