'''
https://leetcode.com/problems/find-bottom-left-tree-value/

Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -2^31 <= Node.val <= 2^31 - 1
'''

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Breadth First Search, Iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
def findBottomLeftValueI(root: Optional[TreeNode]) -> int:
    # Breath-First Search
    # Initialize a queue (FIFO) to hold the current nodes at each level
    # Iterate while the queue is non-empty
    # During each iteration, pop the least recent node from the queue (FIFO):
    #   - If a node exists append the node's right and left child to the queue
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.right:
            queue.append(root.right)
        if node.left:
            queue.append(root.left)
    
    return node.val


# Algorithm Used: Depth First Search, Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def findBottomLeftValueII(root: Optional[TreeNode]) -> int:
    pass
