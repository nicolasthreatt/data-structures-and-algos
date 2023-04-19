'''
https://leetcode.com/problems/binary-search-tree-iterator/

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
    - BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
      The root of the BST is given as part of the constructor.
      The pointer should be initialized to a non-existent number smaller than any element in the BST.
    - boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
      otherwise returns false.
    - int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid.
That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input:
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

Constraints:
    * The number of nodes in the tree is in the range [1, 105].
    * 0 <= Node.val <= 106
    * At most 105 calls will be made to hasNext, and next.
 

Follow up:
    - Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory,
      where h is the height of the tree?
'''

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: In-Order Traversal, Depth First Search, Iterative
# Time Complexity: O(n)
# Space Complexity: O(h) 
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Initialize a list to implement a stack (LIFO)
        self.stack = []

        # When a new tree is initlize, add its nodes from left most path to the end of the stack 
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # Pop the last element from the stack to get the last in node
        parent = self.stack.pop()

        # For inorder traversal its neccessary to traverse right after traversing left, but
        # before traversing right, add the right most node(s) to the end of the stack
        right_child = parent.right
        while right_child:
            self.stack(right_child)
            right_child = right_child.left

        # Return the value after moving pointer to the right node in-order
        return parent.val

    def hasNext(self) -> bool:
        # If the stack is empty then it means there is nothing next to traverse
        return self.stack != []
