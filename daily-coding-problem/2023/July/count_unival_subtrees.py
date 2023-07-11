"""
Daily Coding Problem: #8 (Easy) - Google
Date: 07/10/2023

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
     0
    / \
   1   0
       / \
      1   0
     / \
    1   1

The unival subtrees are:
    - Node(1) (leaf)
    - Node(1) (leaf)
    - Node(1) (leaf)
    - Node(1, Node(1), Node(1)) (root)
    - Node(0) (root)
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth-First Search, Postorder Traversal
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), where n is the number of nodes in the tree
def count_unival_subtrees(root: Node) -> int:

    def dfs(node: Node) -> int:
        """Postorder traversal"""

        # Base case (no node)
        # Return zero so later the sum does not include the current (null) node
        if not node:
            return 0

        # Get the number of unival subtrees in the left and right subtrees
        left = dfs(node.left)
        right = dfs(node.right)

        # Check if the current node is a unival subtree
        # The current node is a unival subtree if:
        #   - The left and right subtrees are unival subtrees
        #   - The left and right subtrees have the same value as the current node
        # NOTE: `not node.left` and `not node.right` are used to check if the left/right subtrees exist.
        #       If they don't exist, then they are considered unival subtrees.
        valid_left = not node.left or node.left.val == node.val
        valid_right = not node.right or node.right.val == node.val

        # Return the number of unival subtrees in the left and right subtrees
        # plus 1 if the current node is a unival subtree. Otherwise, return
        # the number of unival subtrees in the left and right subtrees.
        if valid_left and valid_right:
            return left + right + 1
        else:
            return left + right
    
    # Invoke the helper function
    return dfs(root)


if __name__ == "__main__":
    # Tree with multiple unival subtrees
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert count_unival_subtrees(root) == 5

    # Tree with no nodes
    root = None
    assert count_unival_subtrees(root) == 0

    # Tree with a single node
    root = Node(1)
    assert count_unival_subtrees(root) == 1

    # Tree with two nodes (not unival)
    root = Node(1, Node(2), Node(3))
    assert count_unival_subtrees(root) == 2

    # Tree with two nodes (unival)
    root = Node(1, Node(1), Node(1))
    assert count_unival_subtrees(root) == 3

    # Tree with multiple unival subtrees
    root = Node(1, Node(1), Node(1, Node(1), Node(1)))
    assert count_unival_subtrees(root) == 5

    # Tree with no unival subtrees
    root = Node(1, Node(2), Node(3))
    assert count_unival_subtrees(root) == 2

    # Tree with unival subtrees at different levels
    root = Node(1, Node(1, Node(1), Node(1)), Node(1, None, Node(1)))
    assert count_unival_subtrees(root) == 6
