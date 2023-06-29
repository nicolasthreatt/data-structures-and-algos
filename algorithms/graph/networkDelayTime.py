"""
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k.

Return the minimum time it takes for all the n nodes to receive the signal.

If it is impossible for all the n nodes to receive the signal, return -1.

Example 1
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

Example 2
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1

Example 3
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1

Constraints:
    * 1 <= k <= n <= 100
    * 1 <= times.length <= 6000
    * times[i].length == 3
    * 1 <= ui, vi <= n
    * ui != vi
    * 0 <= wi <= 100
    * All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""


from collections import defaultdict
from typing import List
import heapq

# Algorithm: Dijkstra's Algorithm
# Time Complexity: O(E*log(V)), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V^2)
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # Build the graph
    edges = defaultdict(list)
    
    # Iterate through the network times and add the edges
    # A node can have multiple edges (list of tuples)
    # Each edge is a tuple of (neighbor, weight)
    for src, dest, weight in times:
        edges[src].append((dest, weight)) # (neighbor, weight)

    # Initialize the distance
    distance = 0
    
    # Initialize the min heap
    # The heap is a list of tuples of (distance, node)
    # The heap will then be sorted by distance
    minHeap = [(distance, k)] # (distance, node)

    # Initialize the visited set
    visited = set()

    # Iterate through the nodes until the heap becomes empty
    # Process the node with the smallest distance first (recall min heap sorted by distance)
    # If the node has been visited, skip it. No need to process it again.
    # Otherwise, add it to the visited set and update the distance if necessary
    # Then, add the neighbor nodes to the heap
    # If the heap is empty, then all the nodes have been visited
    while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            distance = max(distance, weight)

            for neighbor_node, neighbor_weight in edges[node]:
                if neighbor_node not in visited:
                    heapq.heappush(minHeap, (weight + neighbor_weight, neighbor_node))

    # Return the distance if all the nodes have been visited
    return distance if len(visited) == n else -1
