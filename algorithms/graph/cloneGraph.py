"""
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list.
The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:
    * The number of nodes in the graph is in the range [0, 100].
    * 1 <= Node.val <= 100
    * Node.val is unique for each node.
    * There are no repeated edges and no self-loops in the graph.
    * The Graph is connected and all nodes can be visited starting from the given node.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Algorithm Used: Graph, Depth First Search, Hashmap
# Time Complexity: O(n), where n is the number of nodes + edges in the graph
# Space Complexity: O(n), where n is the number of nodes + edges in the graph
def cloneGraph(node: Node) -> Node:
    # Create a hashmap to store the mapping of old nodes to their copy
    oldToNewMapping = {}

    def clone_dfs(curr_node: Node) -> Node:
        """Depth First Search helper function to clone the graph.

        Checks if a copy of the node already exist in the hashmap.
        If it does, then return the copy of the node.
        Otherwise, create a copy of the node and add it to the hashmap.
        Then recursively clone all the neighbors of the node.

        Args:
            node (Node): The current node to clone.

        Returns:
            Node: The copy of the node.
        """

        # BASE CASE (NO NODE)
        # If current node does not exist, which will most likely occur at the beginning at the graph,
        # then there is nothing to return.
        if not curr_node:
            return None

        # BASE CASE (CLONE EXIST):
        # If the current node already exist in the hashamp, then a copy has been made.
        # Thus all that is needed is to return the COPY of the node.
        # This is similar to checking if a node has been visited in a graph.
        if curr_node in oldToNewMapping:
            return oldToNewMapping[curr_node]

        # Here it is known that a copy of the node does not exist, so make a clone
        # of it then add it to the hashmap that maps old nodes to their copy
        copy = Node(curr_node.val)
        oldToNewMapping[node] = copy

        # Recursively clone all the neighbors of the current node.
        # This is done by iterating through each of a node's neighbors calling the clone_dfs function on each neighbor.
        for neighbor in curr_node.neighbors:
            copy.neighbors.append(clone_dfs(neighbor))

        # Return the copy of the node after all its neighbors have been cloned.
        return copy

    return clone_dfs(node)
