"""
Daily Coding Problem: #3 (Medium) - Google
Date: 07/05/2023

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

The following test should pass:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Preorder Traversal
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), where n is the number of nodes in the tree
def serialize(root: Node) -> str:
    # Base case
    if not root:
        return '-'

    # Preorder traversal
    serialized = root.val + '-' # Add a hyphen to separate the nodes
    serialized += serialize(root.left)
    serialized += serialize(root.right)

    return serialized


# Algorithm Used: Preorder Traversal
# Time Complexity: O(n), where n is the number of nodes in the string
# Space Complexity:O(n), where n is the number of nodes in the string
def deserialize(s: str) -> Node:
    def dfs_preorder(nodes: list) -> Node:
        # Base case (no more nodes left)
        if not nodes:
            return None
        
        # Get the next node
        val = nodes.pop(0)

        # Base case (node is a leaf)
        if not val:
            return None

        # Create the node
        node = Node(val)

        # Recursively create the left and right subtrees
        node.left = dfs_preorder(nodes)
        node.right = dfs_preorder(nodes)

        return node

    # Split the string into a list of nodes
    nodes = s.split('-')

    # Create the tree
    root = dfs_preorder(nodes)

    return root


if __name__ == '__main__':
    # Test case with an empty tree
    assert deserialize(serialize(None)) ==  None

    # Test case with a single node
    node = Node('root')
    assert deserialize(serialize(node)).val == 'root'

    # Test case with a node having only a left child
    node = Node('root', Node('left'))
    assert deserialize(serialize(node)).left.val == 'left'

    # Test case with a node having only a right child
    node = Node('root', None, Node('right'))
    assert deserialize(serialize(node)).right.val == 'right'

    # Test case with a node having both left and right children
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

    # Test case with multiple levels
    node = Node('root', Node('left', Node('left.left')), Node('right', Node('right.left'), Node('right.right')))
    assert deserialize(serialize(node)).right.left.val == 'right.left'
