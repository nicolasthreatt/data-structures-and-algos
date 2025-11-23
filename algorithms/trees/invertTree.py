"""
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(n)
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    # Swap Child Nodes
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    # Return the inverted tree
    return root

if __name__ == "__main__":

    # Helper to convert tree to list (level-order) for easy comparison
    def treeToList(root: Optional[TreeNode]) -> list:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None: # Remove trailing None values
            result.pop()
        return result

    root1 = TreeNode(4, 
                     TreeNode(2, TreeNode(1), TreeNode(3)), 
                     TreeNode(7, TreeNode(6), TreeNode(9)))
    invertTree(root1)
    assert treeToList(root1) == [4,7,2,9,6,3,1]

    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    invertTree(root2)
    assert treeToList(root2) == [2,3,1]

    root3 = None
    invertTree(root3)
    assert treeToList(root3) == []
