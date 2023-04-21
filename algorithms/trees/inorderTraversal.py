'''
https://leetcode.com/problems/binary-tree-inorder-traversal/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Inorder Traversal, Stack (LIFO), Depth First Search, Iterative
# Time Complexity: O(n)
# Space Complexity:O(n)
def inorderTraversalI(root: Optional[TreeNode]) -> List[int]:
    # Initialize a list to return the inorder nodes
    nodes = []

    # Initialize a list to implement a stack (LIFO)
    stack = []

    # Iterate through the root node and stack while both are not null
    # For each iteration:
    #   1. Traverse the path as far left as possible, adding each node the the stack (LIFO)
    #   2.  After, pop the node the last node placed on the stack and store it as the current node.
    #      Then add its value to the inorder nodes list.
    #   3. Update the current node to the right then attemp to repeat iteration
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        nodes.append(current.val)
        current = current.right

    # Return the nodes from the inorder traversal
    return nodes


# Algorithm Used: Inorder Traversal, Depth First Search, Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def inorderTraversalII(root: Optional[TreeNode]) -> List[int]:
    # Create a list to store the nodes for the inorder traversal
    nodes = []

    def dfs_inorder(root: Optional[TreeNode]) -> None:
        # If the node does not exist there is nothing to return (Base Case)
        if not root:
            return None
        
        # For an Inorder Traversal Depth First Search:
        #   1. Traverse any left nodes
        #   2. Perform Tree Operations (Append the node's value to the list of nodes)
        #   3. Traverse any right nodes
        #   4. Repeat till all paths in the tree are traversed
        dfs_inorder(root.left)
        nodes.append(root.val)
        dfs_inorder(root.right)

    # Invoke Depth First Seach function to grab the nodes
    dfs_inorder(root)

    # Return the nodes from the inorder traversal
    return nodes
        


