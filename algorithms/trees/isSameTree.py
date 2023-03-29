'''
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
    * The number of nodes in both trees is in the range [0, 100].
    * -104 <= Node.val <= 104
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity: O(p + q)
# Space Complexity: O(1)
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both p and q are empty, then both trees have finished traversing at the same time
    if not p and not q:
        return True

    # Now that it is known that p and q are BOTH not null:
    #   - Check if p or q is null.
    #       + This means one has finished travering before the other
    #   - Check is p and q differ in values.
    #       + This means the nodes are different
    # For either scenario, return False
    if not p or not q or p.val != q.val:
        return False

    # Here it is known that p.val == q.val
    # Two trees can only be the same if their left and right subtrees are also the same
    return (
        isSameTree(p.left, q.left) and
        isSameTree(p.right, q.right)
    )