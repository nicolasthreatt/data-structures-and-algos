'''
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
    * The left subtree of a node contains only nodes with keys less than the node's key.
    * The right subtree of a node contains only nodes with keys greater than the node's key.
    * Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
    * The number of nodes in the tree is in the range [0, 10^4].
    * -10^4 <= Node.val <= 10^4
    * All the values in the tree are unique.
    * root is guaranteed to be a valid binary search tree.
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Reverse In-Order Traversal, Depth First Search, Recursive
# Time Complexity: O(n)
# Space Complexity: O(h)
def convertBSTI(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Create a global variable that will be used in the resurive depth first seach function
    current_sum = 0

    # Recursive Reverse Depth First Search
    # NOTE: This can be done in a reversed in-order traversal since it is known that in BST
    #       the right node will be greater than its parent node and its sibling left node
    def dfs(node: TreeNode) -> None:
        # If the node does not exist there is nothing to return (Base Case)
        if not node:
            return
        
        # First, recursively traverse down the tree's right nodes until the base case is covered
        # Once this is finished the current sum should be the sum of the entire right subtree values
        dfs(node.right)

        # After traversing down the tree:
        #   * Let the python program be aware of the global/nonlocal variable to keep track of the sum
        #   * Store the node's value in a temporary varaible since it will be used after its updated
        #   * Update the node's value to include the current sum
        #   * Update the current sum to include the node's value
        nonlocal current_sum
        tmp = node.val
        node.val += current_sum
        current_sum += tmp
    
        # Next, recursively traverse down the tree's left nodes until the base cased is covered
        # Once this is finished the tree's node values will all be updated
        dfs(node.left)

    # Began recursive depth first search to get the new nodes' values
    dfs(root)

    # As specified in the problem statement, return the updated tree
    return root
