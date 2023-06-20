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
# Time Complexity: O(nlog(n)), where n is the number of nodes
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def countComponentI(n: int, edges: List[List[int]]) -> int:
    # Initialize the parents and rank arrays
    # All nodes are initially their own parents with a rank of 1 (i.e. parent[node] = node and rank[node] = 1)
    #    - Each element in the parent array indicates the parent of the node at that index
    #    - A connection is noted by two nodes having the same parent
    # The rank is used to determine which node to make the parent when two nodes are unioned
    #    - Ranks indicates the number of nodes in the connected component
    #    - The node with the larger rank will be the parent of the node with the smaller rank
    #    - Each eleent in the rank array indicates the the number of nodes in the connected component
    #        + i.e. rank[node] = 1 means that the node is the only node in the connected component
    # Once connected, the rank of the parent is increased by the rank of the child.
    # This is done to keep the rank accurate when the parent is unioned with another node.
    parents = [i for i in range(n)]
    rank = [1] * n

    def find(n):
        """Find the root parent of the node.

        Time Complexity: O(n), where n is the number of nodes
        Space Complexity: O(1)

        Args:
            n (int): The node to find the parent of.


        Returns:
            int: The parent of the node.
        """
        # Iterate through the parents until the initial root from the path is found.
        # This is done by setting the parent of each node to its grandparent (parents[parents[n]]).
        # In other words, each node will be set
        data = n
        while data != parents[data]:
            parents[data] = parents[parents[data]]  # Path compression
            data = parents[data]  # Traverse up the path
        return data

    def union(n1, n2) -> int:
        """Union the two nodes.

        Find the parents of the nodes and union them.
        If the parents are the same, the nodes are already unioned.
        Otherwise, union the nodes by setting the parent of the node with the smaller rank

        Time Complexity: O(log(n)), where n is the number of nodes
        Space Complexity: O(n), where n is the number of nodes

        Args:
            n1 (int): The first node to union.
            n2 (int): The second node to union.

        Returns:
            int: 1 if the nodes were unioned, 0 otherwise.
        """
        # Find the parents of the nodes
        p1, p2 = find(n1), find(n2)

        # If the parents are the same, the nodes are already unioned so no need to union.
        # Could also note a cycle if the parents are the same
        if p1 == p2:
            return 0

        # Union the nodes by setting the parent of the node with the smaller rank
        # to the parent of the node with the larger rank.
        # This is done so that the root of the connected component is always the node with the largest rank.
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

    # Return the number of connected components.
    return num_connected_components


# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(e + v), where e is the number of edges and v is the number of vertices
# Space Complexity: O(e + v), where e is the number of edges and v is the number of vertices
def countComponentII(n: int, edges: List[List[int]]) -> int:
    pass
