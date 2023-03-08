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

class SingleLinkedListNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return "SingleNode object: data={}".format(self.data)

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


class SingleLinkedList:

    def __init__(self):
        self.head = None
        # self.next = SingleLinkedListNode()

    def __repr__(self) -> str:
        return "SingleLinkedList object: head={}".format(self.head)

    def is_empty(self) -> bool:
        """Returns True if the Linked List is empty. Otherwise, returns False"""

        return self.head is None

    def add_front(self, new_data):
        """Add a Node whose data is the new_data argument to the fron of the
        Linked List"""

        # Create a new temporary node with the new data
        # Assign the current head of the Linked List to the temporary next node
        tmp = SingleLinkedListNode(new_data)
        tmp.set_next(self.head)

        # Set the head of the linked list to the temportary node, which had just
        # stored the old head
        self.head = tmp

    def add_between(self, new_data):
        pass

    def add_rear(self, new_data):
        pass

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument
        as its self.data variable. Return nothing.
        
        The time complexity is 0(n) because in the worst case we have to visit
        every None before we find the one we need to remove."""

        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current = self.head
        previous = None
        found = False

        # Traverse through list until, if possibe, the proper data is found
        while not found:
            if current.get_data() == data:
                found = True
            else:
                # If current.get_next() then we now know that we've reached
                # the end of the linked list.
                if current.get_next() == None:
                    return "A node with that data value is not present."

                # If we still need to traverse through the linked list update
                # previous to the current value and then update current to the 
                # next value.
                else:
                    previous = current
                    current = current.get_data()

        # If the previous is None, then this means Linked List is trying to remove the head,
        # which now must be reassigned
        if previous is None:
            self.head = current.get_next()
        # If not trying to remove the head, then the current node must be removed by
        # reassigning the pointer before it to the pointer after it
        # previou
        else:
            previous.set_next(current.get_next())

    def reverseI(self):
        """
        Iteratively reverses the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be vsisted in order to reverse the Linked List.

        The space complexity is O(1).
        """

        # Initialize a previous and current ListNode
        previous = None
        current = self.head

        # Iterate through the linked list
        #   - Store the next ListNode in a temporary varaible
        #   - Swap the next pointer with previous pointer
        #   - Swap the previous and curent pointers
        #   - Update the current pointer
        while current:
            next = current.next

            current.set_next(previous)
            previous = current

            current = next

        return previous

    def reverseII(self):
        """
        Recursively reverses the Linked List.

        The time complexity is O(n) because every Node in the Linked List must
        be vsisted in order to reverse the Linked List.

        The space complexity is O(1).
        """

        # Base Case:
        #   - Return nothing if there is no head. This ensure no more recursive calls
        if not self.head:
            return None

        # Recursive Case
        #   - Check if the the head has a next node
        #   - If there is a next node, and if so recursively swap links
        #   - After set the head's next node to none.
        #     This marks the end of the reversed linked list
        newHead = self.head
        if self.head.next:
            newHead = self.reverseII(self.head.next)
            self.head.next.set_next(self.head)
        self.head = None

        return newHead

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
        while current:
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
