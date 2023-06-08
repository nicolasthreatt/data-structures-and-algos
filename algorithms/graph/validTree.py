"""
https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:
    Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Output: true.

Example 2:
    Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    Output: false.
"""

from typing import List


# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(e + v), where e is the number of edges and v is the number of vertices
# Space Complexity: O(e + v), where e is the number of edges and v is the number of vertices
def validTreeI(n: int, edges: List[List[int]]) -> bool:
    # If there are no nodes, return True.
    # Empty graph is a valid tree.
    if n == 0:
        return True

    # Map each node to its adjacent nodes
    # NOTE: This is an undirected graph, so each node is adjacent to each other
    neighbor_nodes_map = {i: [] for i in range(n)}
    for n1, n2 in edges:
        neighbor_nodes_map[n1].append(n2)  # n1 -> n2
        neighbor_nodes_map[n2].append(n1)  # n2 -> n1

    # Initialize a set to store the visited nodes.
    # This is used to detect cycles in the graph.
    visit = set()

    def dfs(curr_node: int, prev_node: int) -> bool:
        """Depth First Search helper function to traverse the graph.

        If the current node has already been visited, then there is a cycle in the graph.
        Otherwise, recursively call dfs on all the neighbor nodes of the current node after
        adding the current node to the visited set.
        If any of the neighbor nodes is the previous node, then skip it.
        If DFS was able to traverse the entire graph without finding a cycle, then return True.

        Args:
            curr_node (int): The current node to traverse.
            prev_node (int): The previous node that was traversed.

        Returns:
            bool: True if the graph is a valid tree, False otherwise.
        """
        # BASE CASE (INVALID CALL/PATH)
        # If the current node has already been visited, then there is a cycle in the graph.
        if curr_node in visit:
            return False

        # Here, so far there is a valid path since the current node has not been visited.
        # Add the current node to the visited set.
        visit.add(curr_node)

        # Iterate through the neighbor nodes of the current node.
        for neighbor_node in neighbor_nodes_map[curr_node]:
            # If the neighbor node is the previous node, then skip it.
            # This is to prevent the graph from going back to the previous node.
            if neighbor_node == prev_node:
                continue

            # Keep traversing the graph to see if there is a cycle.
            # If there is a cycle, then return False.
            if not dfs(neighbor_node, curr_node):
                return False

        # BASE CASE (VALID PATH)
        # No cycle was found, so return True.
        return True

    # Start traversing the graph from the first node, which is represented by 0, in the graph.
    # The previous node is -1 since there is no previous node.
    # After traversing the graph, check if all nodes were visited, which means all nodes are connected with no cycles.
    return dfs(0, -1) and n == len(visit)


# Algorithm Used: Graph, Breadth First Search
# Time Complexity: O(e + v), where e is the number of edges and v is the number of vertices
# Space Complexity:O(e + v), where e is the number of edges and v is the number of vertices
def validTreeII(n: int, edges: List[List[int]]) -> bool:
    pass
