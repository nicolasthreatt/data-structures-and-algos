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
    distances[start] = 0 # source node distance is 0

    # Create a set to keep track of visited nodes
    visited = set()

    while len(visited) != len(graph):
        # Find the node with the smallest tentative distance
        min_distance = float('inf')
        min_node = None

        # Loop through all the nodes of the graph
        # If the node is not visited and the tentative distance is smaller than
        #  the current minimum distance, update the minimum distance and minimum node
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Mark the current node as visited
        visited.add(min_node)

        # Update the distances of the neighboring nodes
        for neighbor in graph[min_node]:
            # Calculate the new tentative distance
            new_distance = distances[min_node] + graph[min_node][neighbor]

            # Update the distance if it's smaller than the current distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# Example usage
if __name__ == '__main__':
    # Example graph represented as an adjacency dictionary
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
