"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

You are given a directed graph of n nodes numbered from 0 to n - 1,
where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n,
indicating that there is a directed edge from node i to node edges[i].
If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2,
such that the maximum between the distance from node1 to that node,
and from node2 to that node is minimized.
If there are multiple answers, return the node with the smallest index,
and if no possible answer exists, return -1.

Note that edges may contain cycles.

Example 1:
    Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    Output: 2
    Explanation:
        - The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
        - The maximum of those two distances is 1.
        - It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

Example 2:
    Input: edges = [1,2,-1], node1 = 0, node2 = 2
    Output: 2
    Explanation:
        - The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
        - The maximum of those two distances is 2.
        - It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

Constraints:
    * n == edges.length
    * 2 <= n <= 10^4
    * edges.length == n
    * 0 <= edges[i] <= n - 1
    * 0 <= node1, node2 <= n - 1
"""

from collections import deque
from typing import List


# Algorithm Used: Graph, Breadth First Search, Hashmap
# Time Complexity: O(n)
# Space Complexity: O(n)
def findClosestNodeI(edges: List[int], node1: int, node2: int) -> int:
    def bfs(src: int, dist_map: dict) -> None:
        """Breadth First Search helper function to traverse the graph.

        Args:
            src (int): The source node to start the traversal from.
            dist_map (dict): The map to store the distance from the source node to each node.
        """
        # Initialize a queue to store the nodes to visit.
        # Queue will store a list of [node, distance from src]
        queue = deque()
        queue.append([src, 0])  # [node, distance from src]

        # Initialize the distance from the source node to itself to be 0.
        dist_map[src] = 0

        # While the queue is not empty, traverse the graph.
        while queue:
            # Pop the first node along with its distance from the source node from the queue.
            node, dist_from_src = queue.popleft()

            # Get the neighbor node of the current node.
            # NOTE: This is a directed graph, so each node has at most one outgoing edge.
            neighbor_node = edges[node]

            # If the neighbor node has not been visited:
            #   - Add the neighbor node to the queue.
            #   - Update the distance from the source node to the neighbor node.
            if neighbor_node not in dist_map:
                queue.append([neighbor_node, dist_from_src + 1])
                dist_map[neighbor_node] = dist_from_src + 1

    # Map each node to its adjacent nodes
    node1_dist = {}  # Map node: distance from node1
    node2_dist = {}  # Map node: distance from node2

    # Traverse the graph from node1 and node2
    bfs(node1, node1_dist)
    bfs(node2, node2_dist)

    # Initialize the node and distance to return
    node = -1
    distance = float("inf")

    # Iterate through the nodes and find the node with the minimum distance from node1 AND node2.
    # The distance is the maximum of the distance from node1 and node2 since the graph is directed.
    for i in range(len(edges)):
        # If the node is reachable from both node1 and node2, then update the node and distance.
        if i in node1_dist and i in node2_dist:
            curr_dist = max(node1_dist[i], node2_dist[i])

            # If the current distance is less than the minimum distance, then update the node and distance.
            # NOTE: From problem statement: "If there are multiple answers, return the node with the smallest index"
            if curr_dist < distance:
                node = i
                distance = curr_dist

    # Return the node with the minimum distance from node1 AND node2.
    return node


# Algorithm Used: Graph, Depth First Search, Hashmap
# Time Complexity: O(n + e), where n is the number of nodes and e is the number of edges
# Space Complexity: O(n + e), where n is the number of nodes and e is the number of edges
def findClosestNodeI(edges: List[int], node1: int, node2: int) -> int:
    pass
