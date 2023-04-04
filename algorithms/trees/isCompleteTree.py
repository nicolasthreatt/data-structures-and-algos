'''
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is
completely filled, and allnodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation:
    - Every level before the last is full
        * ie. levels with node-values {1} and {2, 3}), all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:
    * The number of nodes in the tree is in the range [1, 100].
    * 1 <= Node.val <= 1000
'''

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Breadth First Search, Queue
# Time Complexity: O(n)
# Space Complexity: O(n)
def isCompleteTree(root: Optional[TreeNode]) -> bool:
    # Create a queue (FIFO) for breadth first serach (level order traversal)
    # Add the root to the queue
    queue = deque([root])

    # Breadth First Search
    # Iterate through the queue while its not empty
    while queue:
        # Pop the left most node from the queue to get the earliest node
        node = queue.popleft()

        # If the node exist, append its child to the queue (ORDER MATTERS - FIFO)
        if node:
            queue.append(node.left)
            queue.append(node.right)
        # If the node is null, iterate through the queue and verify the rest of the queue is also null
        # If the any node after the initial null node exist then return False
        else:
            while queue:
                if queue.popleft():
                    return False
    
    # Breadth First Searches has successfully finished
    return True
