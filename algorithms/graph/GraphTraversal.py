"""
Breadth-First Search (BFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores all the vertices of a tree/graph in breadth-first order,
      i.e., visiting all the vertices at the same level before moving to the next level. 
    * BFS can be implemented using a queue.
    * BFS is useful for finding the shortest path or exploring all the nodes in a tree or graph.

Depth-First Search (DFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores as far as possible along each branch before backtracking. 
    * DFS can be implemented using recursion or an explicit stack.
    * DFS is often used when searching for a specific node or finding a path between two nodes.
"""

from collections import deque


# Definition for a Node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class GraphTraversal:
    def __init__(self):
        self.visited = set()

    # Algorithm(s) Used: Breadth First Search - Visit Neighbors First
    # Time Complexity: O(V + E)
    # Space Complexiy: O(V)
    def bfs(self, node: Node):
        queue = deque([node])
        while queue:
            n = queue.popleft()
            if n not in self.visited:
                self.visited.add(n)
                for neighbor in n.neighbors:
                    if neighbor not in self.visited:
                        queue.append(neighbor)

    # Algorithm(s) Used: Depth First Search (Iterative) - Follow Path First
    # Time Complexity: O(V + E)
    # Space Complexiy: O(V)
    def interative_dfs(self, node: Node):
        stack = [node]
        while stack:
            n = stack.pop()
            if n not in self.visited:
                self.visited.add(n)
                for neighbor in n.neighbors:
                    stack.append(neighbor)

    # Algorithm(s) Used: Depth First Search (Recursive) - Follow Path First
    # Time Complexity: O(V + E)
    # Splace Complexity:: O(V)
    def recursive_dfs(self, node: Node):
        if not node or node in self.visited:
            return
        self.visited.add(node) # PRE-Order
        for neighbor in node.neighbors:
            if neighbor not in self.visited:
                self.recursive_dfs(neighbor)
        # self.visited.add(node) # POST-Order
