"""
Daily Coding Problem: #6 (Hard) - Google
Date: 07/08/2023

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.

Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

Here's an example XOR linked list which meets the above conditions:
A    <->    B    <->    C    <->    D
B         A ⊕ C       B ⊕ D         C

XOR Truth Table:
A    B    A ⊕ B
0    0      0
0    1      1
1    0      1
1    1      0

Therefore both = prev ⊕ next and indicates the direction of the next node.
If both == 1, then the next node is the previous node. If both == 0, then the next node is the next node.

If using a language that has no pointers (such as Python), you can assume you have access
to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""


# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0


# Algorith Used: Linked List
# Time Complexity: O(n)
# Space Complexity: O(n)
class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__nodes = [] # List of nodes that stores the previous and next nodes

    def add(self, element):
        """Adds an element to the end of the list. O(1)"""

        # Create the node
        node = Node(element)

        # If the list is empty set the head and tail to the node
        # Else add the node to the end of the list.
        if not self.head:
            # 1st node in the list
            self.head = node
            self.tail = node
        else:
            # Add the node to the end of the list
            self.tail.both = self.tail.both ^ id(node) # XOR the current tail's both with the id of the new node
            node.both = id(self.tail)
            self.tail = node
    
        # Add the node to the list of nodes
        self.__nodes.append(node)

    def get(self, index):
        """Returns the node at the given index. O(n)"""
    
        # If the index is negative, return None
        if index < 0:
            return None

        # If the list is empty, return None
        if not self.head:
            return None

        # If the index is 0, return the head
        if index == 0:
            return self.head

        # Get the node at the index
        prev_node_id = 0
        current_node = self.head

        # Iterate through the list until we reach the index
        for i in range(index):
            # Get the next node
            next_node_id = prev_node_id ^ current_node.both

            # If the next node is None, then the index is invalid
            if not next_node_id:
                return None

            # Get the next node
            prev_node_id = id(current_node)
            current_node = self.__get_node(next_node_id)

        # Return the node at the index
        return current_node

    def __get_node(self, node_id):
        # Iterate through the list of nodes and return the node with the given id
        for node in self.__nodes:
            if id(node) == node_id:
                return node

        # If the node is not found, return None
        return None


if __name__ == '__main__':
    # Create an instance of the XOR linked list
    xor_linked_list = XORLinkedList()

    # Adding elements to the XOR linked list
    xor_linked_list.add(10)
    xor_linked_list.add(20)
    xor_linked_list.add(30)
    xor_linked_list.add(40)
    xor_linked_list.add(50)

    # Getting nodes at specific indices
    node_0 = xor_linked_list.get(0)
    node_2 = xor_linked_list.get(2)
    node_4 = xor_linked_list.get(4)

    # Test Case: Validating the nodes at the given indices
    assert node_0.val == 10, "Incorrect value at index 0"
    assert node_2.val == 30, "Incorrect value at index 2"
    assert node_4.val == 50, "Incorrect value at index 4"

    # Test Case: Validating the node at an invalid index
    invalid_index_node = xor_linked_list.get(6)
    assert invalid_index_node is None, "Invalid index node should be None"

    print("All test cases passed successfully.")
