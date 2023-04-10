'''
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a binary tree.
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree,
return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Constraints:
    * The number of nodes in the tree is in the range [1, 104].
    * 0 <= Node.val <= 10^4
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Post-Order Traversal, Depth First Search
# Time Complexity: O(n), n = number of nodes
# Space Complexity: 
def rob(root: Optional[TreeNode]) -> int:
    
    # NOTE: return pair: [withRoot, withoutRoot]
    def dfs(root: Optional[TreeNode]) -> int:
        # If there is no root node then there is no house to rob (Base Case)
        if not root:
            return [0, 0]
        
        # Recursively traverse down the tree to find each node's
        # potential maximum profit to be made robbing
        leftPair = dfs(root.left)
        rightPair = dfs(root.right)

        # Determine the profit made robbing with and without the root node.
        # Remember from probelm statement that two houses cannot be directly robbed
        # NOTE: pair = [withRoot, withoutRoot]
        withRoot = root.val + leftPair[1] + rightPair[1]
        withoutRoot = max(leftPair) + max(rightPair)

        return [withRoot, withoutRoot]

    # Return the maximum profit made robbing
    return max(dfs(root))