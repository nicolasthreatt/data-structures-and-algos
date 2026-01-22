#include <cassert>
#include <deque>
#include <optional>
#include <string>

template <typename T>
class Deque {
private:
    std::deque<T> items;

public:
    Deque() = default;  // Constructor

    void addFront(const T& item) {
        items.push_front(item);
    }

    void addRear(const T& item) {
        items.push_back(item);
    }

    std::optional<T> removeFront() {
        if (items.empty()) return std::nullopt;

        T frontItem = items.front();
        items.pop_front();
        return frontItem;
    }

    std::optional<T> removeRear() {
        if (items.empty()) return std::nullopt;

        T rearItem = items.back();
        items.pop_back();
        return rearItem;
    }

    size_t size() const {
        return items.size();
    }

    bool isEmpty() const {
        return items.empty();
    }
};

int main() {
    {
        Deque<int> deque;

        assert(deque.isEmpty());
        assert(deque.size() == 0);

        deque.addFront(1);
        assert(!deque.isEmpty());
        assert(deque.size() == 1);

        deque.addRear(2);
        assert(deque.size() == 2);

        auto front = deque.removeFront();
        assert(front.has_value() && front.value() == 1);
        assert(deque.size() == 1);

        auto rear = deque.removeRear();
        assert(rear.has_value() && rear.value() == 2);
        assert(deque.isEmpty());

        assert(!deque.removeFront().has_value());
        assert(!deque.removeRear().has_value());
    }

    {
        Deque<std::string> deque;

        deque.addRear("hello");
        deque.addFront("world");
        assert(deque.size() == 2);

        auto front = deque.removeFront();
        assert(front.has_value() && front.value() == "world");

        auto rear = deque.removeRear();
        assert(rear.has_value() && rear.value() == "hello");

        assert(deque.isEmpty());
    }

    {
        Deque<int> deque;
        deque.addFront(10);
        deque.addRear(20);
        deque.addFront(5);

        assert(deque.size() == 3);

        assert(deque.removeRear().value() == 20);
        assert(deque.removeFront().value() == 5);
        assert(deque.removeFront().value() == 10);
        assert(deque.isEmpty());
    }

    return 0;
}
