"""
Queue
    - An ADT that stores items in the order in which they were added
    - Items in a queue are added to the back and removed from the front
    - Order is preserved

Basic Operations
    - Add to the queue (enqueue)
    - Remove from the queue (dequeue)
    - Check is the queue empty
    - Check the number of items in the queue
    - Check the next to be removed

Queue Data
    - Any data type that can stored in a list can be stored in a queue
    - Limited access, because we can only access the data from once place
        + FRONT ONLY

Recursion
    - A queue is either empty
    - Or it consists of a item, and therest of which is a queue

Examples
    - First-In, First-Out (FIFO)
    - A print queue, so that the documents are printed in the order in
      which they were sent to the machine
"""

class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """
        Takes in an item and insert that item into the 0th inde of the list
        that is representing the Queue.

        The runtime is 0(n), or linear time, because inserting into the 0th
        index of a list forces all the other items in the list to move one
        index to the right.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Returns and removes the front-most item of the Queue, which is represented
        by the last item in the list.

        The runtime is 0(1), or constant time, because indexing to the end of a
        list happens in contstant time
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        Returns the last item in the list, which represents the front-most
        item in the Queue.

        The runtime is constant because we're just indexing to the last item
        of the list and returning the value found there
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        Returns the size of the Queue, which is represented by the length of the
        list.
        
        The runtime is 0(1), or constant time, because we're only returning the
        length.
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value expressing whether or not the list representing
        the Queue is empty.

        Testing for equality happens in constant time. 
        """
        return self.items == []
