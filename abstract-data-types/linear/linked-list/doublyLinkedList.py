"""
When Is a Linked List Suitable?
    - Insert items "in between" other items
    - Collection size is unknown
    - Don't need random access
    - Not concerned about memory usage

Linked Lists Are Recursive
    - A linked list is empty
    - Or it consists of a node that contains data and a pointer to a linked list
"""

class DoubleLinkedListNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return "DoubleLinkedListNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute."""

        return self.data

    def set_data(self, new_data) -> None:
        """Replace the existing value of the self.data attribute with new_data
        parameter"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        
        return self.next

    def set_next(self, new_next) -> None:
        """Replace the existing value of the self.next attribute with new_next
        parameter"""
        
        self.next = new_next

    def get_previous(self):
        """Return the self.prev attribute"""

        return self.prev

    def set_previous(self, new_previous) -> None:
        """Replace the existing value of the self.prev attribute with new_previous
        parameter"""

        self.prev = new_previous


class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        return "<DoubleLinkedList object: head={}>".format(self.head)

    def is_empty(self):
        """Returns True if the Linked List is empty. Otherwise, returns False"""

        return self.head is None

    def size(self) -> int:
        """Traverses the Linked List and returns an integer value representing
        the number of nodes in the Linked List.
        
        The time complexity is O(n) because every Node in the Linked List must
        be visited in order to calculate the size of the Linked List
        """
        size = 0

        if self.head is None:
            return size

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the Linked List and returns True if the data searched for
        is present in one of the Nodes. Otherwise, it returns False.
        
        The time complexity is O(n)
        """

        if self.head is None:
            return "Linked List is empty. No Nodes to search"

        current = self.head
        while current:
            if current.get_data() == data:
                return True
            
            current = current.get_next()
        
        return False

    def add_front(self, new_data) -> None:
        """Add a Node whose data is the new_data argument to the fron of the
        Linked List"""

        # Create a new temporary node with the new data
        # Assign the current head of the Linked List to the temporary next node
        tmp = DoubleLinkedListNode(new_data)
        tmp.set_next(self.head)

        # Check to see if the list is at the head, 1st index, position. 
        # This is because in a doubly linked list the previous only needs
        # to be set after the 1st node
        if self.head is not None:
            self.head.set_previous(tmp)

        # Set the head of the linked list to the temportary node, which had just
        # stored the old head
        self.head = tmp

    def add_middle(self, data) -> None:
        pass

    def remove(self, data):
        """Removes the first occurance of a Node that contains the data argument
        as its self.data attribute. Returns nothing.
        
        The time complexity is O(n) because in the worst case, we have to visit
        every Node before finding the one we want to remove.
        """

        # Check to see if head is empty
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        # Traverse through linked list till the node which contains the data is found
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()
        
        # If the previous is None, then this means Linked List is trying to remove the head,
        # which now must be reassigned
        if current.prev is None:
            self.head = current.get_next()
        else:
            current.prev.set_next(current.get_next())
            current.next.set_previous(current.get_previous())
