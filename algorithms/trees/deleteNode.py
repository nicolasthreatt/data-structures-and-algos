'''
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
    1. Search for a node to remove.
    2. If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 104].
    * -10^5 <= Node.val <= 10^5
    * Each node has a unique value.
    * root is a valid binary search tree.
    * -10^5 <= key <= 10^5

Follow up:
    * Could you solve it with time complexity O(height of tree)?
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursive
# Time Complexity: O(h)
# Space Complexity: O(1)
def deleteNodeI(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # If the root is null then there is nothing to delete (Base Case)
    if not root:
        return root

    # If the key to delete is GREATER than the current tree value, recursively update the RIGHT node
    if key > root.val:
        root.right = deleteNodeI(root.right, key)

    # If the key to delete is LESS than the current tree value, recursively update the LEFT node
    elif key < root.val:
        root.left = deleteNodeI(root.left, key)

    # If the key value is found and
    #   - There is no left subtree then return the right subtree to the deleted node
    #   - There is no right subtree then return the left subtree to the deleted node
    #   - Both subtress exists, then update the node to be deleted to the right node's subtree minimum value 
    #       * After the right subtree will have to be recursively updated/deleted to remove duplicate values
    else:
        if not root.left: # No left node, then return right node
            return root.right
        elif not root.right: # No right node, then return left node
            return root.left
        
        # Both nodes (left and right) exists so find the minimum value from right subtree,
        # which due to the definition of a BST is done by traversing left
        current = root.right
        while current.left:
            current = current.left
        
        # Since the node to be deleted is found and both subtrees exist, replace its value 
        # with the minimum value found in the right subtree
        # NOTE: THIS WILL CAUSE DUPLICATE VALUES
        root.val = current.val

        # There are now duplicate values in the tree so recursively update the tree
        root.right = deleteNodeI(root.right, root.val) # NOTE: DELETING THE ROOT VALUE NOT THE KEY

    return root


# Algorithm Used: Iterative
# Time Complexity: 
# Space Complexity: 
def deleteNodeII(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    pass
