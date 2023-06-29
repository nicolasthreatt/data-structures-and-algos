"""
Breadth-First Search (BFS) is an algorithm for traversing or searching a tree or graph. 
It explores all the vertices of a tree/graph in breadth-first order,
i.e., visiting all the vertices at the same level before moving to the next level. 
In a tree, BFS starts from the root node and explores all the nodes at each level before moving to the next level.
BFS can be implemented using a queue.
BFS is useful for finding the shortest path or exploring all the nodes in a tree or graph.
"""

from collections import deque

# Algorithm: BFS Tree Traversal, Preorder
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n), where n is the number of nodes
def bfs_tree(root):
    # Create an empty queue and enqueue the root node
    queue = deque() # FIFO
    queue.append(root)

    # Initialize an empty list to store the traversal order
    traversal_order = []

    # Process nodes until the queue becomes empty
    while queue:
        # Dequeue the front node
        current_node = queue.popleft()

        # Process the current node
        traversal_order.append(current_node.value)

        # Enqueue the child nodes of the current node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    # Return the traversal order
    return traversal_order
