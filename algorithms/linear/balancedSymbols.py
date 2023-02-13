"""
Prompt
    - Create a function that takes in a string of symbol pairs as a parameter
    - Function should return True if the symbol string is balanced or False
      if it is not

Requirements
    - The string should only contain opening and closing symbols, like
      '([{}])' or '(([{])'
    - For symbols to be balanced, each opening symbol must also have a closing
      symbol, and the symbols must be properly nested
    - Make use of a stack in your solutions

Run-Time:
    - O(n)
"""

class Stack:

    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()

        return None
    
    def peek(self):
        if self.items:
            return self.items[-1]

        return None

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []


def match_symbols(symbols_str):

    # Create a dictionary for all the possible symbol combinations
    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()
    stack = Stack()

    index = 0
    while index < len(symbols_str):
        symbol = symbols_str[index]

        # Add opening symbols to the stack if the symbol is an opener
        if symbol in openers:
            stack.push(symbol)
    
        else:
            # If the Stack is already, empty the symbols are not balanced
            if stack.is_empty():
                return False

            # If there are still items in the Stack, look for a mis-amtch
            else:
                top_item = stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        # Increment index iterator
        index += 1

    # Stack should be after after indexing through the input symbol string
    if stack.is_empty():
        return True


# TEST CASES
print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))