'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]

Explanation:
    * Given the above perfect binary tree (Figure A), your function should populate each next pointer
      to point to its next right node, just like in Figure B.
    * The serialized output is in level order as connected by the next pointers,
      with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 212 - 1].
    * -1000 <= Node.val <= 1000
'''

from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Algorithm Used: Breadth First Search, Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)
def connect(root: Optional[Node]) -> Optional[Node]:
    # Initialize a pointer to keep track of the current node when travesersing the tree
    current = root

    # Initialize a pointer to keep track of the next node when traversing the tree
    next = root.left if root else None

    # Traversing through tree while the current and next pointers are not null
    # For each iteration:
    #   1. Set the current node's left next pointer to the current node's right pointer
    #   2. Set the current node's right next pointer to the current's next left pointer
    #       * This is possible due to step 1, but wont be needed until the a new level is reached
    #   3. Update the current pointer to be the next node in the tree
    #   4. If the updated current pointer does not exists, reset the current pointer to be the left most
    #      node on the same level and the next pointer on the level below the current pointer
    #       * This will mark the end of a level
    while current and next:
        current.left.next = current.right # Step 1
        if current.next: # Step 2
            current.right.next = current.next.left

        current = current.next # Step 3 
        if not current: # Step 4
            current = next
            next = current.left
    
    # Return the newly connected tree
    return root
