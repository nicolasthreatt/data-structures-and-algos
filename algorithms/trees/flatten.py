'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Given the root of a binary tree, flatten the tree into a "linked list":
    * The "linked list" should use the same TreeNode class where the right child pointer points
      to the next node in the list and the left child pointer is always null.
    * The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
    * The number of nodes in the tree is in the range [0, 2000].
    * -100 <= Node.val <= 100
 
Follow up:
    * Can you flatten the tree in-place (with O(1) extra space)?
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Breath First Search, Iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
def flattenI(root: Optional[TreeNode]) -> None:
    pass


# Algorithm Used: Post Order Traversal, Depth First Search, Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)
def flattenII(root: Optional[TreeNode]) -> None:

    def dfs(root: Optional[TreeNode]) -> Optional[ListNode]:
        # If the node does not exist there is nothing to return
        if not root:
            return None
        
        # Recursively traverse left and right sub trees
        leftTail = flattenII(root.left)
        rightTail = flattenII(root.right)


        # Since the root's right branch will be used to create the linked list
        # there needs to be a linked between right and left nodes.
        # After creating links between the left and right nodes set the root's left node is null 
        # NOTE: leftTail = root.left
        if root.left:
            leftTail.right = root.right # leftTail.next = root.right
            root.right = root.left
            root.left = None

        # The last tail can be found in 4 different scenarios
        #   - If original root node has both left and right subtrees, then right tail will be last tail
        #   - If original root node has only a right subtree, then right tail will be last tail
        #   - If original root node has only a left subtree, then left tail will be last tail
        #   - If the original root has no substrees, then the root node will be last tail
        # NOTE: Order of returns matter
        lastTail = rightTail or leftTail or root

        return lastTail
    
    dfs(root)


# Algorithm Used: 
# Time Complexity: 
# Space Complexity: O(1)
def flattenIII(root: Optional[TreeNode]) -> None:
    pass
