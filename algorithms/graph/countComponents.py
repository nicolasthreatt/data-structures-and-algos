"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
    Input: n = 5, edges = [[0,1],[1,2],[3,4]]
    Output: 2

Example 2:
    Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
    Output: 1
"""

from typing import List


# Algorithm Used: Graph, Union Find
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def countComponentI(n: int, edges: List[List[int]]) -> int:
    # Initialize the parents and rank arrays
    # All nodes are initially their own parents with a rank of 1
    # The rank is used to determine which node to make the parent when two nodes are unioned
    # Once connected, the rank of the parent is increased by the rank of the child.
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(n):
        """Find the parent of the node.

        Args:
            n (int): The node to find the parent of.

        Returns:
            int: The parent of the node.
        """
        # Iterate through the parents until the initial parent from the path is found.
        # This is done by setting the parent of each node to its grandparent (parents[parents[n]]).
        data = n
        while data != parents[data]:
            parents[data] = parents[parents[data]]  # Path compression
            data = parents[data]  # Traverse up the path
        return data

    def union(n1, n2) -> int:
        """Union the two nodes.

        Args:
            n1 (int): The first node to union.
            n2 (int): The second node to union.

        Returns:
            int: 1 if the nodes were unioned, 0 otherwise.
        """
        # Find the parents of the nodes
        p1, p2 = find(n1), find(n2)

        # If the parents are the same, the nodes are already unioned
        if p1 == p2:
            return 0

        # Union the nodes by setting the parent of the node with the smaller rank
        # to the parent of the node with the larger rank.
        if rank[p2] > rank[p1]:
            parents[p1] = p2
            rank[p2] += rank[p1]
        else:
            parents[p2] = p1
            rank[p1] += rank[p2]

        # Return 1 to indicate that the nodes were unioned.
        # The number of connected components will be decremented by 1.
        return 1

    # Initialize the number of connected components to the number of nodes.
    # Each node is initially its own connected component.
    num_connected_components = n

    # Iterate through the edges and subtract the number of connected components (unions).
    # NOTE: The number of connected components is initially the number of nodes.
    #       So if there are 5 nodes with 3 edges, there are 2 connected components.
    for n1, n2 in edges:
        num_connected_components -= union(n1, n2)

    return num_connected_components


# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def countComponentII(n: int, edges: List[List[int]]) -> int:
    pass
