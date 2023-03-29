'''
https://leetcode.com/problems/binary-tree-preorder-traversal/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100
 
Follow up:
    *Recursive solution is trivial, could you do it iteratively?
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity: 
# Space Complexity: O(1)
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    return preorderTraversalI(root, [])


def preorderTraversalI(root: Optional[TreeNode],  nodes:List[int]) -> List[int]:
    # Check if root exist (Base Case)
    if not root:
        return nodes
    
    # Since this is preorder, append the node's value to the list before
    # recursively calling its left and right nodes
    nodes.append(root.val)

    # Preorder requires traversing from the left first,
    # followed by the right nodes (Iterative Case)
    nodes =  preorderTraversalI(root.left, nodes)
    return preorderTraversalI(root.right, nodes)
