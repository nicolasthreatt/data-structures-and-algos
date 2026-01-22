from typing import Any, List, Optional


class Stack:
    def __init__(self):
        self.items: List[Any] = []

    def push(self, item: Any):
        self.items.append(item)
    
    def pop(self) -> Optional[Any]:
        if self.items:
            return self.items.pop()
        return None
    
    def peek(self) -> Optional[Any]:
        if self.items:
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []


if __name__ == "__main__":
    stack = Stack()

    assert stack.is_empty() is True
    assert stack.size() == 0
    assert stack.pop() is None
    assert stack.peek() is None

    stack.push(1)
    assert stack.is_empty() is False
    assert stack.size() == 1
    assert stack.peek() == 1

    stack.push(2)
    assert stack.size() == 2
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert stack.size() == 1
    assert stack.peek() == 1

    assert stack.pop() == 1
    assert stack.is_empty() is True
    assert stack.pop() is None
    assert stack.peek() is None

    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.peek() == 20
    assert stack.size() == 2

    stack.push("hello")
    assert stack.peek() == "hello"
    assert stack.pop() == "hello"

    stack.push(3.14)
    assert stack.pop() == 3.14
    assert stack.is_empty() is False

    stack.pop()
    stack.pop()
    assert stack.is_empty() is True
