"""
Prompt
    - Using a deque data structure, write a function that takes in an
      input string and returns:
        + True if the string is a palindrome
        + False if the string is not a palindrome

Reminder
    - A palindrome is a word that is spelled the same backwards and forwards:
        + mom
        + level
        + kayak
"""

class Deque:

    def __init__(self) -> None:
        self.items = []

    def add_front(self, item) -> None:
        self.items.insert(0, item)

    def add_rear(self, item) -> None:
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        
        return None

    def remove_rear(self):
        if self.items:
            return self.items.pop()

        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def is_palindrome(input_str):
    # Initialize a deque object
    deque = Deque()

    # Loop throught input string
    for char in input_str:
        # Add all chars in the input string to the since adding to rear
        # is constant time
        deque.add_rear(char)

    while deque.size() >= 2: # Size of 1 or 0 means string is a palindrome
        front_item = deque.remove_front()
        rear_item = deque.remove_rear()

        if front_item != rear_item:
            return False

    return True


# TEST CASES
print(is_palindrome('racecar'))
print(is_palindrome('oranges'))
