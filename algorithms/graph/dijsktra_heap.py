"""
Dijkstra's Algorithm

Dijkstra's algorithm is a graph traversal algorithm that guanrentees to finds
the shortest path between a given source node and all other nodes in a weighted graph.

It uses a greedy approach, always choosing the node with the smallest tentative distance from the source.

This algorithm is commonly used in various applications such as
    - Network routing protocols
    - GPS navigation systems
    - Pathfinding in video games.
"""

import heapq


# Algorithm: Dijkstra's Algorithm
# Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V)
def dijkstra(graph, start):
    """
    Dijkstra's algorithm implementation.

    Args:
        graph: The graph represented as an adjacency matrix or dictionary.
        start: The starting node for the algorithm.
    
    Returns:
        A dictionary with the shortest distance from the start node to each node in the graph.
    """

    # Create a dictionary to store the shortest distances from the start node to all other nodes
    # To start with, all distances are infinity so that we it can be updated with the shortest distances later
    distances = {node: float('inf') for node in graph}

    # Set the distance from the start node to itself to 0
    # This is because the distance from the start node to itself is 0
    distances[start] = 0

    # Create a priority queue (heap) to keep track of nodes with their tentative distances
    priority_queue = [(0, start)] # (distance, next_node)

    while priority_queue:
        # Pop the node with the smallest tentative distance from the priority queue
        curr_distance, curr_node = heapq.heappop(priority_queue)

        # Update the distances of the neighboring nodes
        for neighbor, weight in graph[curr_node].items():
            # Calculate the new tentative distance
            new_distance = curr_distance + weight

            # Update the distance if it's smaller than the current distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


# Example usage
if __name__ == '__main__':
    # Example graph represented as an adjacency dictionary with weighted edges
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 3, 'B': 2, 'D': 6},
        'D': {'B': 1, 'C': 6}
    }

    start_node = 'A'

    # Run Dijkstra's algorithm
    shortest_distances = dijkstra(graph, start_node)

    # Print the shortest distances from the start node to all other nodes
    for node, distance in shortest_distances.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")
