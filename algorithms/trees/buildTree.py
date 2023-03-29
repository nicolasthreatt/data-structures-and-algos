'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
    * 1 <= preorder.length <= 3000
    * inorder.length == preorder.length
    * -3000 <= preorder[i], inorder[i] <= 3000
    * preorder and inorder consist of unique values.
    * Each value of inorder also appears in preorder.
    * preorder is guaranteed to be the preorder traversal of the tree.
    * inorder is guaranteed to be the inorder traversal of the tree.
'''


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity: 
# Space Complexity: O(n)
def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Base Case:
    #   - Check if either of the two lists are empty
    #   - If so, return Null.
    #   - This marks the end of a path when building a tree
    if not preorder or not inorder:
        return None
    
    # From the definition of PRE-ORDER Traversal, the root node
    # will always be the first node when travsersing
    root = TreeNode(preorder[0])
    
    # From the definition of IN-ORDER Traversal, the root node will
    # always be at the index which seperates the left and right sub nodes
    mid = inorder.index(preorder[0])

    # When building the left subtree (Iterative Case):
    #   - Skip the list first index of the preorder list since it is the root node and
    #     slice the list until the mid point is reached.
    #   - Slice the inorder list from the beginning up until on spot before the mid point
    # Note that the mid point is the index of the root node in the in order list
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])


    # When building the right subtree (Iterative Case):
    #   - Slice the preorder and inorder lists from one spot past mid point
    #     until the end of the inorder list
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root