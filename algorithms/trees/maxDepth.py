'''
Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    * The number of nodes in the tree is in the range [0, 104].
    * -100 <= Node.val <= 100

Breadth First Search:
    * Tree traversal algorithm that explores nodes level by level.
    * Using a queue to store frontier nodes supports the behavior of this search.

Depth First Search:
    * Tree traversal algorithm that goes deep into a tree exploring for nodes branch by branch.
    * Using a stack to store frontier nodes supports the behavior of this search.
'''

import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Level Order Traversal, Breadth First Search, Queue (FIFO)
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepthI(root: Optional[TreeNode]) -> int:
    # Empty nodes do not have a depth
    if not root:
        return 0

    # Breath-First Search:
    # Initialize a queue (FIFO) to hold current nodes at each level
    # Iterate while the queue is non-empty
    # For the length of the queue size, pop the least recent node from the queue (FIFO):
    #   - If a node exists, add it to the level and append the node's left and right child to the queue
    #   - Note, here the queue's size is being updated
    # After looping through the queue size, update levels
    queue = collections.deque([root])
    levels = 0
    while queue:
        queue_size = len(queue)
        for _ in range(queue_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels += 1

    return levels


# Algorithm Used: Pre-Order Depth First Traversals, Iterative, Stack (LIFO)
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepthII(root: Optional[TreeNode]) -> int:
    # Empty nodes do not have a depth
    if not root:
        return 0
    
    # Set the initial maximum depth to be 1
    max_depth = 0

    # Create a stack to store the nodes when performing pre-order traversal
    # stack = [[node, depth]]
    stack = [[root, 1]]

    # Iterate while the stack is not empty
    #   - For each iteration pop the last item inserted into the stack, which
    #     will contain a node and its depth within the tree
    #   - If the node exist, recompute the maximum depth and add its childen to the stack
    # NOTE: root is originally in stack
    while stack:
        node, depth = stack.pop()

        if node:
            max_depth = max(max_depth, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return max_depth


# Algorithm Used: Depth First Traversals, Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxDepthIII(root: Optional[TreeNode]) -> int:
    # Empty nodes do not have a depth
    if not root:
        return 0
    
    return 1 + max(maxDepthIII(root.left), maxDepthIII(root.right))
