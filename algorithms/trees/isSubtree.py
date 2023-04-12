'''
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
    * The number of nodes in the root tree is in the range [1, 2000].
    * The number of nodes in the subRoot tree is in the range [1, 1000].
    * -10^4 <= root.val <= 10^4
    * -10^4 <= subRoot.val <= 10^4
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity: O(root * subRoot)
# Space Complexity: O(1)
def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Check if subroot is a null node
    # NOTE: every root will have a null node at some point thus will make it a subtree. (Base Case I)
    if not subRoot:
        return True

    # Check if root is a null node and that the subRoot tree exists.
    # This will mean that there are no more child nodes left to traverse in the root tree
    #   meaning that no match was found.
    # NOTE: from the condition above it is now known that the SUB-ROOT EXISTS (Base Case II)
    if not root:
        return False

    # Now that it is known that the root and subTree both exists,
    # see if the root and subtree are subtrees
    if isSameTree(root, subRoot):
        return True

    # Recurisvely check if the left or right trees contains the specified subtree. (Iterative Case)
    return (
        isSubtree(root.left, subRoot) or
        isSubtree(root.right, subRoot)
    )


# Helper function to see if a tree contains a specific subtree
def isSameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
    if not root and not subRoot:
        return True

    if root and subRoot and root.val == subRoot.val:
        return (
            isSameTree(root.left, subRoot.left) and
            isSameTree(root.right, subRoot.right)
        )

    return False
