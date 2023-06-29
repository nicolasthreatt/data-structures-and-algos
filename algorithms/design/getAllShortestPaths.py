"""
A dasher sometimes travels between cities.
To avoid delays, the dasher first checks for the shortest routes.

Given a map of the cities and their bidirectional roads represented by a graph of nodes and edges,
determine which given roads are along any shortest path.

Return an array of strings, one for each road in order,
where the value is YES if the road is along a shortest path or NO if it is not.

The roads or edges are named using their 1-based index within the input arrays.

Example


Example:
    Given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:
        Road from/to/weight
         1     (1, 2, 1)
         2     (2, 3, 1)
         3     (3, 4, 1)
         4     (4, 5, 1)
         5     (5, 1, 3)
         6     (1, 3, 2)
         7     (5, 3, 1)
    Input:
        (5, 
            [1, 2, 3, 4, 5, 1, 5],
            [2, 3, 4, 5, 1, 3, 3],
            [1, 1, 1, 1, 3, 2, 1]
        )
    Output: ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES']
    Explanation:
        The traveller must travel from city 1 to city g_nodes, so from node 1 to node 5 in this case.
        The shortest path is 3 units long and there are three paths of that length:
            - 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.
        Return an array of strings, one for each road in order,
        where the value is YES if a road is along a shortest path or NO if it is not.
        In this case, the resulting array is ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES'].
        The third and fourth roads connect nodes (3, 4) and (4, 5) respectively.
        They are not on a shortest path, i.e. one with a length of 3 in this case.
"""

import heapq

# Algorithm: Dijkstra's Algorithm, Heap
# Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges
# Space Complexity: O(V)
def get_all_shortest_paths(g_nodes, routes):
    # Create adjacency list to represent the graph
    graph = [[] for _ in range(g_nodes + 1)]
    for route in routes:
        g_from, g_to, g_weight = route
        graph[g_from].append((g_to, g_weight))
        graph[g_to].append((g_from, g_weight))

    # Set the start node
    start_node = 1

    # Initialize distances to all nodes as infinity except the start node
    distances = [float('inf')] * (g_nodes + 1)
    distances[start_node] = 0

    # Use a priority queue to get the node with the smallest distance
    priority_queue = [(0, start_node)]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Process nodes until the priority queue becomes empty
    while priority_queue:
        # Get the node with the smallest distance
        current_dist, current_node = heapq.heappop(priority_queue)

        # Ignore outdated entries in the priority queue
        if current_dist > distances[current_node] or current_node in visited:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node]:
            # Calculate the new distance to the neighbor
            new_dist = current_dist + weight

            # Update the distance to the neighbor if it is smaller than the current distance
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

            # Add the neighbor to the visited set
            visited.add(neighbor)

    # Initialize the result array
    valid_shortest_paths = []

    # Iterate through each road and check if it lies on a shortest path
    for route in routes:
        g_from, g_to, g_weight = route

        # Check if the road lies on a shortest path
        # If the distance from the start node to the from node plus the weight of the road
        # is equal to the distance from the start node to the to node, then the road lies on a shortest path
        if (distances[g_from] + g_weight == distances[g_to] or
            distances[g_to] + g_weight == distances[g_from]):
            valid_shortest_paths.append('YES')
        else:
            valid_shortest_paths.append('NO')

    return valid_shortest_paths


if __name__ == "__main__":
    routes = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (4, 5, 1),
        (5, 1, 3),
        (1, 3, 2),
        (5, 3, 1),
    ]
    assert(get_all_shortest_paths(5, routes) == ['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'YES'])