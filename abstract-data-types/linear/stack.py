"""
Stack
    - An ADT that stores items in the order in which they were added
    - Items are added to and removed from the "top" of a stack
    - Order is preserved

Basic Operations
    - Add to the stack
        + .append()
    - Remove from the stack
        + .pop()
    - Check to isee if stack is empty
    - Count the number of items in the stack
    - Determine what is next to be removed

Stack Data
    - Any data tpe that can be stored in a list can be stored in a stack
    - Limited access because we can only access the data from one place    

Examples
    - Last In, First Out (LIFO)
        + Items are added to and removed from the top of a stack
    - A linter in a text editor can detect missing symbols
    - Reversing the characters in a string
"""

class Stack:

    def __init__(self):
        self.items = []
    
    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is 0(1), or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        """
        Removes and return the last item for the list, which is also the
        top item of the Stack.

        The runtime here is constant time, because all it does is index to the
        last item of the list.
        """

        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """"
        Returns the last item in the list, which is also the item at the top
        of the Stack.

        This method runs in constant time because idexing into a list is done
        in constant time.
        """
        if self.items:
            return self.items[-1]
        
        return None

    def size(self):
        """
        Returns the length of the list that is representing the Stack.
        
        This method runs in constant time because finding the length of a list
        also happens in constant time.
        """

        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value describing whether or not the Stack is empty.

        Testing for equality happens in constant time. 
        """

        return self.items == []
