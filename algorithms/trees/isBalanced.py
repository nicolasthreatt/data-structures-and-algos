'''
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.
    - A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
    * The number of nodes in the tree is in the range [0, 5000].
    * -10^4 <= Node.val <= 10^4
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: 
# Time Complexity: O(n^2)
# Space Complexity: 
def isBalancedI(root: Optional[TreeNode]) -> bool:
    pass


# Algorithm Used: Depth-First Search, Recursion
# Time Complexity: O(n)
# Space Complexity: 
def isBalancedII(root: Optional[TreeNode]) -> bool:
    
    # Nested Recursion Function for Depth-First Search
    def dfs(root: Optional[TreeNode]) -> list:
        # Base Case:
        #   - Check if the root node is null
        #       * If so, return True to indicate its balanced and 0 for its height
        #       * This signifies that the recursion function has reached a null node
        # NOTE: Empty trees are balanced
        if not root:
            return [True, 0]
        
        # Recursive Case:
        #   - Recusively call depth first search function to reach botton nodes 
        left = dfs(root.left)
        right = dfs(root.right)

        # Check that the left and right subtrees are height balanced by:
        #   1. Verifying that both currrent left and right subtrees are balanced
        #   2. Verifying that the left and right subtrees height differ by at-most one
        # NOTE: A height-balanced binary tree is a binary tree in which the depth
        #       of the two subtrees of every node never differs by more than one.
        balanced = (
            left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
        )

        # For each recursive call return if the subtrees are balanced and the current height.
        # Moving towards base case.
        return [balanced, 1 + max(left[1], right[1])]

    # NOTE: From problem statement, "determine if it is height-balanced"
    #       This is can be found in the first elemenent of dfs() return value
    return dfs(root)[0]
