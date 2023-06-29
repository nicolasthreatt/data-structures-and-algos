"""
Breadth-First Search (BFS) is an algorithm for traversing or searching a tree or graph. 
It explores all the vertices of a tree/graph in breadth-first order,
i.e., visiting all the vertices at the same level before moving to the next level. 
In a tree, BFS starts from the root node and explores all the nodes at each level before moving to the next level.
BFS can be implemented using a queue.
BFS is useful for finding the shortest path or exploring all the nodes in a tree or graph.
"""

from collections import deque

# Algorithm: BFS Graph Traversal
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
# Space Complexity: O(V), where V is the number of vertices in the graph
def bfs_graph(graph, start):
    # Create an empty queue and enqueue the start node
    queue = deque() # FIFO
    queue.append(start)

    # Create a set to store the visited nodes
    visited = set()
    visited.add(start)

    # Initialize an empty list to store the traversal order
    traversal_order = []

    # Process nodes until the queue becomes empty
    while queue:
        # Dequeue the front node
        current_node = queue.popleft()

        # Process the current node
        traversal_order.append(current_node)

        # Enqueue the neighbor nodes of the current node if they haven't been visited
        for neighbor_node in graph[current_node]:
            if neighbor_node not in visited:
                queue.append(neighbor_node)
                visited.add(neighbor_node)

    # Return the traversal order
    return traversal_order
