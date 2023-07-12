"""
Given the root to a binary tree, return the deepest node.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth-First Search, Postorder Traversal
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), where n is the number of nodes in the tree
def deepest_node_dfs(root: Node) -> tuple[Node, int]:
    def dfs(node: Node, height: int) -> tuple[Node, int]:
        """Recursive helper function for DFS traversal
        
        Args:
            node (Node): The current node
            height (int): The height of the current node

        Returns:
            tuple[Node, int]: The deepest node and its height
        """
        # Base case (node is a leaf)
        if node and not node.left and not node.right:
            return node, height

        # Recursive Case (node has two children)
        left_node, left_height = dfs(node.left, height + 1)
        right_node, right_height = dfs(node.right, height + 1)
    
        # Base/Recursive Case (node has one child)
        if not node.left:
            return right_node, right_height
        elif not node.right:
            return left_node, left_height

        # Find the deepest node in the left and right subtrees
        return max((left_node, left_height), (right_node, right_height), key=lambda x: x[1])
    
    # Return the deepest node and its height
    deepest_node, deepest_height = dfs(root, 0)
    return (deepest_node.val, deepest_height)


# Algorithm Used: Breadth-First Search
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), where n is the number of nodes in the tree
def deepest_node_bfs(root: Node) -> tuple[Node, int]:
    # Initialize the queue with the root node
    queue = [(root, 0)]

    # Initialize the deepest node and its height
    deepest_node = None
    deepest_height = 0

    # Iterate until the queue is empty
    while queue:
        # Dequeue the node and its height
        node, height = queue.pop(0)

        # Check if the current node is deeper than the deepest node
        if height > deepest_height:
            deepest_node = node
            deepest_height = height

        # Enqueue the left and right children of the current node
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))

    # Return the deepest node and its height
    return (deepest_node.val, deepest_height)


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    #   / \
    #  6   7
    root = Node(1, Node(2, Node(4, Node(6), Node(7)), Node(5)), Node(3))
    assert deepest_node_dfs(root) == (6, 3)
    assert deepest_node_bfs(root) == (6, 3)
