'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a
descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:
    * The number of nodes in the tree is in the range [2, 105].
    * -109 <= Node.val <= 109
    * All Node.val are unique.
    * p != q
    * p and q will exist in the BST.
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Algorithm Used: Recursion
# Time Complexity: O(log(n))
# Space Complexity: O(1)
def lowestCommonAncestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:

    # Iterate through root
    # If current root is LESS THAN both p and q, search RIGHT subtree
    # If current root is GREATER THAN both p and q, search LEFT subtree
    # If current root is BETWEEN p and q, return current node (LCA)
    current = root
    while current:
        if current.val < p.val and current.val < q.val:
            current = current.right
        elif current.val > p.val and current.val > q.val:
            current = current.left
        else:  # p.val <= current.val <= q.val
            return current
