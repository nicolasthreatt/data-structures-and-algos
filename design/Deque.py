from typing import Any, List, Optional


class Deque:
    def __init__(self):
        self.items: List[Any] = []

    def add_front(self, item: Any):
        self.items.insert(0, item)

    def add_rear(self, item: Any):
        self.items.append(item)

    def remove_front(self) -> Optional[Any]:
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self) -> Optional[Any]:
        if self.items:
            return self.items.pop()
        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []


if __name__ == "__main__":
    deque = Deque()

    assert deque.is_empty() is True
    assert deque.size() == 0
    assert deque.remove_front() is None
    assert deque.remove_rear() is None

    deque.add_front(1)
    assert deque.is_empty() is False
    assert deque.size() == 1

    deque.add_rear(2)
    assert deque.size() == 2

    assert deque.remove_front() == 1
    assert deque.size() == 1

    assert deque.remove_rear() == 2
    assert deque.is_empty() is True

    deque.add_front(10)
    deque.add_rear(20)
    deque.add_front(5)

    assert deque.size() == 3
    assert deque.remove_rear() == 20
    assert deque.remove_front() == 5
    assert deque.remove_front() == 10
    assert deque.is_empty() is True

    deque.add_rear("hello")
    deque.add_front("world")

    assert deque.remove_front() == "world"
    assert deque.remove_rear() == "hello"
    assert deque.is_empty() is True
