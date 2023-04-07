'''
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater than the node's key.
    * Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
    * The number of nodes in the tree is in the range [1, 104].
    * -2^31 <= Node.val <= 2^31 - 1
'''

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth First Search, Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def isValidBST(root: Optional[TreeNode]) -> bool:

    # Helper Function which validates the node of a binary tree
    def valid(node, left, right):
        # If the node does not exist then this means that the tree has finished
        # traversing down a particular path, thus return true
        if not node:
            return True

        # A binary search tree can only have its node val between it's left and right parent node
        # If this is not the case, return False
        if not (left < node.val < right):
            return False

        # Recursively work way down the tree
        # Valid the left the right subtrees
        return (
            valid(node.left, left, node.val) and
            valid(node.right, node.val, right)
        )

    return valid(root, float('-inf'), float('inf'))
