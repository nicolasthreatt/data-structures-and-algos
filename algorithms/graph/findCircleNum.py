"""
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

Example 2:
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

Constraints:
    * 1 <= n <= 200
    * n == isConnected.length
    * n == isConnected[i].length
    * isConnected[i][j] is 1 or 0.
    * isConnected[i][i] == 1
    * isConnected[i][j] == isConnected[j][i]
"""

from typing import List


# Algorithm Used: Graph, Union-Find
# Time Complexity: O(n)
# Space Complexity: O(n)
def findCircleNumI(isConnected: List[List[int]]) -> int:
    # Create parent and rank arrays
    # Parent array is used to keep track of the parent/root of each node
    # Rank array is used to keep track of the size of each set
    parent = [i for i in range(len(isConnected))]
    rank = [1] * len(isConnected)

    def find(n):
        """Find the parent/root of a node"""

        # Initialize the parent of each node to itself
        p = parent[n]

        # Traverse up the tree until the parent of the node is itself
        while p != parent[p]:
            parent[p] = parent[parent[p]] # Path compression
            p = parent[p] # Traverse up the tree
        return p # Return the parent/root of the node
    
    def union(n1, n2):
        """Union two nodes"""

        # Find the parent of each node
        p1, p2 = find(n1), find(n2)

        # If the parent of each node is the same, then they are already connected.
        # Return 0 to indicate that no union was performed.
        if p1 == p2:
            return 0
        
        # Set the parent of the node with the smaller rank to the parent of the node with the larger rank
        # Update the rank of the node with the larger rank
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        
        # Return 1 to indicate that a union was performed
        return 1
    
    # Initialize the number of connected cities to the number of provinces
    provinces = len(isConnected)

    # Iterate through the matrix
    # If a connection is found, then union the two cities and decrement the number of connected cities.
    # Recall from union-find that the number of connected components is equal to the number of sets.
    for i in range(len(isConnected)):
        for j in range(i, (len(isConnected))):
            if isConnected[i][j] == 1:
                provinces -= union(i, j)

    # Return the number of provinces
    return provinces


# Algorithm Used: Graph, DFS
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def findCircleNumII(isConnected: List[List[int]]) -> int:
    pass
