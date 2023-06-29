"""
Depth-First Search (DFS) is an algorithm for traversing or searching a tree or graph. 
It explores as far as possible along each branch before backtracking. 
In a tree, DFS starts from the root node and explores each branch completely before moving to the next branch.
DFS can be implemented using recursion or an explicit stack.
DFS is often used when searching for a specific node or finding a path between two nodes.
"""

# Algorithm: DFS Graph Traversal, Recursive
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph
# Space Complexity: O(V), where V is the number of vertices in the graph
def dfs_graph(graph, start):
    # Create a set to store the visited nodes
    visited = set()

    # Initialize an empty list to store the traversal order
    traversal_order = []

    # Recursive helper function for DFS traversal
    def dfs_helper(node):
        # Base case
        if node is None or node in visited:
            return

        # Process the current node
        traversal_order.append(node)

        # Add the current node to the visited set
        visited.add(node)

        # Recursively traverse all the adjacent nodes of the current node
        for adjacent_node in graph[node]:
                dfs_helper(adjacent_node)

    # Call the helper function to perform DFS traversal
    dfs_helper(start)

    # Return the traversal order
    return traversal_order
