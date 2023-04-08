'''
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100
'''

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm Used: Breadth First Search (Level Order Traversal)
# Time Complexity: O(n), n = number of nodes
# Space Complexity: O(n), n = number of nodes
def rightSideViewI(root: Optional[TreeNode]) -> List[int]:
    # Create a list to store the right side view nodes
    nodes = []

    # Breadth First Search
    # Initialize a queue (FIFO) with just the root
    # Iterate through the queue. Note that the size of the queue will be changing
    queue = deque([root])
    while queue:
        # For each iteration of the queue:
        #   - Initialize a variable for the right side of the tree
        #   - Get the current queue size, which will represent the number of nodes on a level
        rightSide = None
        qLen = len(queue)

        # Iterate through the number of nodes at a given level of a binary tree
        for _ in range(qLen):
            # For each node on each level pop the LEFT/FRONT of the queue (FIFO)
            # If node exist append the left node first followed by the right node.
            # NOTE: We want to pop off the right most node last, then store it in the list of nodes
            node = queue.popleft()
            if node:
                rightSide = node
                queue.append(node.left)
                queue.append(node.right)
        
        # After the loop from above finishes looping through the level nodes,
        # `rightSide` will have the right most node on a given level.
        # NOTE: Check for null nodes from children
        if rightSide:
            nodes.append(rightSide.val)

    # As specified from the problem return the right side nodes
    return nodes


# Algorithm Used: Depth First Search
# Time Complexity: 
# Space Complexity: 
def rightSideViewII(root: Optional[TreeNode]) -> List[int]:
    pass
