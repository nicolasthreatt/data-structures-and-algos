'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
    *  The root-to-leaf path 1->2 represents the number 12.
    * The root-to-leaf path 1->3 represents the number 13.
    * Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
    * The root-to-leaf path 4->9->5 represents the number 495.
    * The root-to-leaf path 4->9->1 represents the number 491.
    * The root-to-leaf path 4->0 represents the number 40.
    * Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
    * The number of nodes in the tree is in the range [1, 1000].
    * 0 <= Node.val <= 9
    * The depth of the tree will not exceed 10.
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Pre-Order Traversal, Depth First Search
# Time Complexity: O(n)
# Space Complexity: O(log(n)) = O(log(h))
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
    # Pre-Order Depth First Search
    def dfs(current, new_sum):
        # If there is no current node then there is nothing to sum
        if not current:
            return 0
        
        # Each time the tree traverses update the sum
        new_sum = (new_sum * 10) + current.val

        # If the tree has traverse to a bottom node, return the sum for the path
        if not current.left and not current.right:
            return new_sum
        
        # Recursively find the sum for the left and righ subtrees
        return dfs(current.left, new_sum) + dfs(current.right, new_sum)
    
    # Began recursive search with the root node and a 0 for the sum.  This is done
    # so that in the initial case `new_sum = (0 * 10) + current.val = current.val`
    return dfs(root, 0)