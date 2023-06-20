"""
https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

Example 2:
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

Constraints:
    * n == edges.length
    * 3 <= n <= 1000
    * edges[i].length == 2
    * 1 <= ai < bi <= edges.length
    * ai != bi
    * There are no repeated edges.
    * The given graph is connected.
"""

from typing import List


# Algorithm Used: Graph, Union Find
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def findRedundantConnectionI(edges: List[List[int]]) -> List[int]:
    # Create a parent array
    # This array will be used to keep track of the parent of each node
    parent = [i for i in range(len(edges) + 1)]

    # Create a rank array
    # This array will be used to keep track of the rank of each node.
    # Rank is the number of nodes in the subtree of a node.
    ranks [1] * (len(edges) + 1)

    def find(n):
        # Find the parent of a node
        p = parent[n]

        # If the parent of a node is not itself, then the node is not the root
        # Set the parent of the node to the parent of its parent
        # This will compress the path to the root
        # Keep doing this until the parent of the node is itself
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    
    def union(n1, n2):
        # Find the parent of each node
        p1, p2 = find(n1), find(n2)

        # If the parent of each node is the same, then the nodes are already connected
        if p1 == p2:
            return False

        # Set the parent of the node with the smaller rank to the parent of the node with the larger rank
        # Update the rank of the node with the larger rank
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        
        return True
    
    # Iterate through each edge
    # If the nodes of the edge are already connected, then return the edge, since it is redundant
    # NOTE: The given graph is connected.
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]
    

# Algorithm Used: Graph, Depth First Search
# Time Complexity: O(n^2), where n is the number of nodes
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def findRedundantConnectionII(edges: List[List[int]]) -> List[int]:
    pass


