"""
Daily Coding Problem: #755 (Hard) - Google
Date: 07/01/2023

In a directed graph, each node is assigned an uppercase letter.

We define a path's value as the number of most frequently-occurring letter along that path.

For example, if a path in the graph goes through "ABACA", the value of the path is 3,
since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph.
If the largest value is infinite, then return null.

The graph is represented with a string and an edge list.
The i-th character represents the uppercase letter of the i-th node.
Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
Self-edges are possible, as well as multi-edges.

For example, the following input graph:
    ABACA
    [(0, 1),
    (0, 2),
    (2, 3),
    (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:
    A
    [(0, 0)]
Should return null, since we have an infinite loop.
"""

from collections import defaultdict

# Algorith Used: DFS, Graph Traversal
# Time Complexity: O(e + v), where e is the number of edges and v is the number of vertices
# Space Complexity: O(v), where v is the number of vertices
def longest_value_path(path, edges):
    """Return the largest value path of a graph.

    This solution uses a hash table to store the graph and a depth-first search to traverse the graph.
    The depth-first search returns the largest value path of the graph.

    The time complexity is O(e + v), where e is the number of edges and v is the number of vertices,
    since the algorithm iterates through the edges and vertices once.
    The space complexity is O(v), where v is the number of vertices, since the algorithm uses a hash table
    to store the graph.
    """

    # Initialize direct graph
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)

    def cyclic(node: int, visited: set) -> bool:
        """Return True if the graph is cyclic, False otherwise.

        This solution uses a depth-first search to traverse the graph.
        If a node is visited twice, then the graph is cyclic.

        Args:
            node (int): The current node.
            visited (set): The set of visited nodes.
        
        Returns:
            bool: True if the graph is cyclic, False otherwise.
        """
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor in visited or cyclic(neighbor, visited):
                return True
        return False

    def dfs(visited: list, node: int) -> int:
        """Return the largest value path of the graph.

        This solution uses a depth-first search to traverse the graph.
        The depth-first search returns the largest value path of the graph.

        Args:
            visited (list): The list of visited nodes.
            node (int): The current node.

        Returns:
            int: The largest value path of the graph.
        """
        # nonlocal graph
    
        # Add the current node to the visited list
        # This is done to prevent infinite loops as we cannot visit a node twice (loop)
        visited[node] = True

        # Initialize count that will be used to store the largest value path of the graph
        count = 0

        # Traverse all the adjacent nodes of the current node.
        # If the adjacent node is not visited, then recursively call dfs on the adjacent node
        # and update count of the current longest path.
        for dest in graph[node]:
            if not visited[dest]:
                count = max(count, dfs(visited, dest))

        # Return the count of the current longest path
        # If the current node is 'A', then increment count by 1 to account for the current node
        return count + (path[node] == 'A')

    # Check if the graph is cyclic
    if any(cyclic(node, set()) for node in range(len(path))):
        return None

    # Initialize a variable to store the largest value path of the graph.
    max_value = 0

    # Traverse the graph using dfs and update max_value
    for i in range(len(path)): # i = starting node
        visited = [False] * len(path)
        max_value = max(max_value, dfs(visited, i))

    # Return the largest value path of the graph
    return max_value if max_value > 0 else None


if __name__ == "__main__":
    # Example 1
    path = "A"
    graph = [(0, 0)]
    assert longest_value_path(path, graph) == None

    # Example 2
    path = "BAA"
    graph = [(0, 1), (0, 2)]
    assert longest_value_path(path, graph) == 1

    # Example 3
    path = "BAA"
    graph = [(0, 1), (2, 0)]
    assert longest_value_path(path, graph) == 2

    # Example 4
    path = "ABACA"
    graph = [(0, 1), (0, 2), (2, 3), (3, 4)]
    assert longest_value_path(path, graph) == 3
