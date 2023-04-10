'''
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -100 <= Node.val <= 100
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth First Search
# Time Complexity: O(n), n = number of nodes
# Space Complexity: 
def diameterOfBinaryTreeI(root: Optional[TreeNode]) -> int:
    # Initialize a global variable to be viewed by the helper function
    diameter = [0]

    # Post Order Traversal, Depth First Search
    # Returns current height of a tree
    def dfs(root: Optional[TreeNode]) -> int:
        # The height of a null tree will be -1 since its one spot past the last
        # node in the path (Base Case)
        if not root:
            return -1
        
        # Recursively find the height of the left and right subtrees
        # NOTE: Depth first nodes traverses a path all the way down a path
        left = dfs(root.left)
        right = dfs(root.right)

        # Find the maximum diamater.
        # diameter = (leftHeight + 1) + (rightHeight + 1) = leftHeight + rightHeight + 2
        # NOTE: A diameter can be defined as the height of its child nodes
        diameter[0] = max(diameter[0], left + right + 2)

        # Find maximum height of the left and right subtrees,
        # increment it by one to return the current height
        return 1 + max(left, right)
    
    # Began recursive call
    dfs(root)

    # Return the max diameter
    return diameter[0]


# Algorithm Used: 
# Time Complexity: 
# Space Complexity: 
def diameterOfBinaryTreeII(root: Optional[TreeNode]) -> int:
    pass
