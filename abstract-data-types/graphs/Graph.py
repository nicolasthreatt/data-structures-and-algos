class Node:
    """
    The Node class represents a node/vertex in a graph.

    Attributes:
        val (int): The value of the node.
        neighbors (list): The list of neighbors of the node.
    """

    def __init__(self, val=0, neighbors=None):
        """Constructor for a node"""
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        """String representation of the node"""
        return f"Node({self.val}, {self.neighbors})"

    def add_neighbor(self, neighbor):
        """Adds a neighbor to the node"""
        self.neighbors.append(neighbor)

    def has_neighbors(self):
        """Checks if the node has any neighbors"""
        return len(self.neighbors) > 0

    def has_neighbor(self, neighbor):
        """Checks if the node has a neighbor"""
        return neighbor in self.neighbors


class GraphUndirect:
    """
    Undirect Graph class represents a graph data structure.
    Contains a list of nodes witha all the nodes in the graph.

    Attributes:
        nodes (list): The list of nodes in the graph.
    """

    def __init__(self, nodes=None):
        """Constructor for a graph"""
        self.nodes = nodes if nodes is not None else []

    def __repr__(self):
        """String representation of the graph"""
        return f"Graph({self.nodes})"

    def find_node(self, val) -> Node:
        """Finds the node with the given value"""
        for node in self.nodes:
            if node.val == val:
                return node
        return None

    def add_edge(self, value1, value2, weight=1):  # union
        """Adds an edge between two nodes

        Args:
            value1 (int): The value of the first node.
            value2 (int): The value of the second node.
            weight (int, optional): The weight of the edge. Defaults to 1.

        Raises:
            ValueError: If the nodes do not exist in the graph.
        """
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighbor(node2)
            node2.add_neighbor(node1)
        else:
            raise ValueError("Nodes do not exist in the graph.")

    def are_connected(self, value1, value2) -> bool:
        """Checks if two nodes are connected

        Args:
            value1 (int): The value of the first node.
            value2 (int): The value of the second node.

        Returns:
            bool: True if the nodes are connected, False otherwise.
        """
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            return node1.has_neighbor(node2)
        else:
            return False

    def num_nodes(self) -> int:
        """Returns the number of nodes in the graph"""
        return len(self.nodes)

    def has_cycle(self) -> bool:
        """Detects if the graph has a cycle"""

        # Initialize a set to store the visited nodes.
        visited = set()

        def dfs(curr_node: Node, prev_node: Node) -> bool:
            """Depth First Search helper function to traverse the graph.

            Args:
                curr_node (Node): The current node to traverse.
                prev_node (Node): The previous node that was traversed.

            Returns:
                bool: True if the graph has a cycle, False otherwise.
            """
            # BASE CASE (INVALID CALL/PATH)
            # If the current node has already been visited, then there is a cycle in the graph.
            # Return False.
            if curr_node in visited:
                return False

            # Here, so far there is a valid path since the current node has not been visited.
            # Add the current node to the visited set.
            visited.add(curr_node)

            # Iterate through the neighbor nodes of the current node.
            for neighbor_node in curr_node.neighbors:
                # If the neighbor node is the previous node, then skip it.
                if neighbor_node == prev_node:
                    continue

                # Keep traversing the graph to see if there is a cycle.
                # If there is a cycle, then return False.
                if not dfs(neighbor_node, curr_node):
                    return False

            # No cycle was found, so return True.
            return True

        # Start traversing the graph from the first node in the graph.
        # The previous node is None since there is no previous node.
        # After traversing the graph, check if all nodes were visited, which means all nodes are connected with no cycles.
        return dfs(self.nodes[0], None) and len(visited) == len(self.nodes)


class GraphDirect:
    """
    Direct Graph class represents a graph data structure.

    Attributes:
        edges (list): The list of edges in the graph.
        graph_dict (dict): The dictionary representation of the graph.

    Example:
        >>> routes = [
        ...     ("Mumbai", "Paris"),
        ...     ("Mumbai", "Dubai"),
        ...     ("Paris", "Dubai"),
        ...     ("Paris", "New York"),
        ...     ("Dubai", "New York"),
        ...     ("New York", "Toronto"),
        ... ]
        >>> routes_graph = Graph(routes)
    """

    def __init__(self, edges=None):
        """Constructor for a graph"""
        self.edges = edges if edges is not None else []
        self.graph_dict = self.create_graph_dict()

    def __repr__(self):
        """String representation of the graph"""
        return f"Graph({self.edges})"

    def create_graph_dict(self) -> dict:
        """Creates a dictionary representation of the graph"""

        # Iterate through the edges and map each node to its adjacent nodes
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        return self.graph_dict

    def add_node(self, node):
        """Adds a node to the graph"""
        self.graph_dict[node] = []

    def find_node(self, val) -> Node:
        """Finds the node with the given value"""
        for node in self.nodes:
            if node.val == val:
                return node
        return None

    def are_connected(self, start, end) -> bool:
        """Checks if two nodes are connected

        Args:
            start (int): The start node.
            end (int): The end node.

        Returns:
            bool: True if the nodes are connected, False otherwise.
        """
        return end in self.graph_dict[start]

    def add_edge(self, start, end):
        """Adds an edge between two nodes

        Args:
            start (int): The start node.
            end (int): The end node.
        """
        if start in self.graph_dict:
            self.graph_dict[start].append(end)
        else:
            self.graph_dict[start] = [end]

    def get_paths(self, start, end):
        """Gets all the paths from the start node to the end node."""

        def get_paths_helper(current_node, end, path=[]) -> list:
            """Depth First Search helper function to traverse the graph.

            Args:
                current_node (int): The start node.
                end (int): The end node.
                path (list, optional): The current path. Defaults to [].

            Returns:
                list: The list of paths from the start node to the end node.

            Example:
                >>> start, end = "Mumbai", "New York"
                >>> print(f"All paths from {start} to {end}: " routes_graph.get_paths(start, end))
            """
            # Set the path to the current path.
            # NOTE: This is necessary because we are using recursion because we need to keep track of the current path.
            path = path + [current_node]

            # Base Case (INVALID PATH)
            # If the current node is not in the graph, then return an empty list.
            if current_node not in self.graph_dict:
                return []

            # BASE CASE (VALID PATH)
            # If the current_node node is the end node, then return the path.
            # This happens when the initial node has traversed all the nodes in the graph
            # and has reached the end node.
            if current_node == end:
                return [path]

            # Here, so far there is a valid path since the current node has not been visited.
            # Initialize a list to store all the paths from the current_node node to the end node.
            paths = []

            # Recursively call get_paths_helper on all the destination nodes of the current_node node.
            # If any of the destination nodes are the end node, then add the path to the list of paths.
            for next_node in self.graph_dict[current_node]:
                if next_node not in path:
                    new_paths = get_paths_helper(next_node, end, path)
                    for p in new_paths:
                        paths.append(p)

            return paths

        return get_paths_helper(start, end, [])

    def get_shortest_path(self, start, end):
        """Gets the shortest path from the start node to the end node."""

        def get_shortest_path_helper(current_node, end, path=[]):
            """Depth First Search helper function to traverse the graph.

            Args:
                current_node (int): The start node.
                end (int): The end node.
                path (list, optional): The current path. Defaults to [].

            Returns:
                list: The shortest path from the start node to the end node.

            Example:
                >>> start, end = "Mumbai", "New York"
                >>> print(f"Shortest path from {start} to {end}: " routes_graph.get_shortest_path(start, end))
            """
            # Base Case (INVALID PATH)
            # If the current node is not in the graph, then return None.
            if current_node not in self.graph_dict:
                return None

            # Set the path to the current path.
            # Include the current node in the path since we are using recursion.
            path = path + [current_node]

            # BASE CASE (VALID PATH)
            # If the current_node node is the end node, then return the path.
            # This happens when the initial node has traversed all the nodes in the graph
            if current_node == end:
                return path

            # Here, so far there is a valid path since the current node has not been visited.
            # Initialize a variable to store the shortest path from the current_node node to the end node.
            # NOTE: This is necessary because we are using recursion because need to also keep track of the current path.
            shortest_path = None

            # Recursively call get_shortest_path_helper on all the destination nodes of the current_node node.
            for next_node in self.graph_dict[current_node]:
                # If the next node has not been visited, then recursively call get_shortest_path_helper on it.
                if next_node not in path:
                    current_path = get_shortest_path_helper(next_node, end, path)

                    # If the current path is shorter than the shortest path, then update the shortest path.
                    if current_path and (shortest_path is None or len(current_path) < len(shortest_path)):
                        shortest_path = current_path

            # Return the shortest path.
            return shortest_path

        return get_shortest_path_helper(start, end)
