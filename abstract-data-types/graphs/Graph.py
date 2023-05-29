# Undirected graph implementation using adjacency list representation


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


class Graph:
    """
    Graph class represents a graph data structure.
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
            print("Edge cannot be added")

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
