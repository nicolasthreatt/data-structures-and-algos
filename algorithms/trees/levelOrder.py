'''
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 2000].
    * -1000 <= Node.val <= 1000
'''

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Breadth First Search, Queue (FIFO)
# Time Complexity: O(n), n = number of nodes
# Space Complexity: O(n)
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # Initialize a list to return the node values from each level
    nodes = []

    # Initialize a queue (FIFO) to hold the current nodes at each level
    queue = deque([root])

    # Breath-First Search
    # Iterate while the queue is non-empty
    # For the length of the queue size, pop the least recent node from the queue (FIFO):
    #   - If a node exists, add it to the level and append the node's left and right child to the queue
    #   - Note, here the queue's size is being updated
    # After looping through the queue size, add the level nodes to the original nodes list
    while queue:
        queue_size = len(queue)
        level = []
        for _ in range(queue_size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level:
            nodes.append(level)

    return nodes
