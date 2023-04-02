'''
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    * The number of the nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100
 

Follow up:
    * Recursive solution is trivial, could you do it iteratively?
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity: O(n)
# Space Complexity: O(1)
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    return postorderTraversalI(root, [])


def postorderTraversalI(root: Optional[TreeNode],  nodes:List[int]) -> List[int]:
    pass


# Algorithm Used: Stack 
# Time Complexity: O(n)
# Space Complexity: O(n)
def postorderTraversalII(root: Optional[TreeNode]) -> List[int]:

    # Initialize a list to store the nodes in post order form
    post_order_nodes = []

    # Initialize a stack to with a two-dimensional tuple:
    #   1. Store the root node
    #   2. Keep track whether a node was visited.
    #       - For now know that a node can be added to the post order list
    #         only if it has been visited.
    stack = [(root, False)]

    # Iterate through the stack while it is not empty
    # Get the current node from the stack and whether it has been visited in the stack:
    #   If the last node from the stack was visited TWICE, add it to the post_order_nodes lists
    #   If the last node from the stack was visisted FIRST, add the parent and child nodes the stack list
    # Recall that stacks are Last-In, First-Out (LIFO) so order matters, thus add right before left
    while stack:
        current, visted = stack.pop()
        if current:
            if visted:
                post_order_nodes.append(current.val)
            else:
                # NOTE: STACK ORDER MATTERS
                stack.append((current, True))
                stack.append((current.right, False))
                stack.append((current.left, False))
    
    return post_order_nodes

