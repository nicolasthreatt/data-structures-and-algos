'''
https://leetcode.com/problems/trim-a-binary-search-tree/

Given the root of a binary search tree and the lowest and highest boundaries as low and high,
trim the tree so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that will remain in the tree
(i.e., any node's descendant should remain a descendant).
It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree.
Note that the root may change depending on the given bounds.

Example 1:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * 0 <= Node.val <= 10^4
    * The value of each node in the tree is unique.
    * root is guaranteed to be a valid binary search tree.
    * 0 <= low <= high <= 10^4
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Post-Order Depth First Search, Recursion
# Time Complexity: O(n), where n is number of nodes
# Space Complexity: O(n), where n is number of nodes
def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    # If the node does not exist there is nothing to return (Base Case)
    if not root:
        return None
    
    # If the root's value is greater than the `high` bound, then its known that its
    # entire right substree nodes will all be too high so need to traverse the tree left
    # NOTE: This recurive call traverse the tree till it is inbounds or null, thus trimming
    if root.val > high:
        return trimBST(root.left, low, high)
    
    # If the root's value is less than than the `low` bound, then its known that its
    # entire left substree nodes will all be too low so need to traverse the tree right
    # NOTE: This recurive call traverse the tree till it is inbounds or null, thus trimming
    if root.val < low:
        return trimBST(root.right, low, high)
    
    # Its known that the root node will be included in the result, so update its left and right sub-trees.
    # This is moving towards the base case because eventually a node with either be between the low and 
    # high markings or null
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    # Return the trimmed tree
    return root
