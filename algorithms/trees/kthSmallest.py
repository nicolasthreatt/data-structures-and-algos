'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
    * The number of nodes in the tree is n.
    * 1 <= k <= n <= 10^4
    * 0 <= Node.val <= 10^4
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Recursion
# Time Complexity:
# Space Complexity:
def kthSmallestI(root: Optional[TreeNode], k: int) -> int:
    pass


# Algorithm Used: In-Order Traversal, Stack, Iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
def kthSmallestII(root: Optional[TreeNode], k: int) -> int:
    # Create a variable to keep track of nth smallest value of the tree during traversal
    n = 0

    # Initialize a stack
    stack = []

    # Began iterating through the tree while the current node and stack both exist
    current = root
    while current and stack:

        # For each traversal, append the left node the stack and traverse as far left as possible.
        #   - This ensures that during each traversal the smallest node value will be the last node in stack.
        # NOTE Stacks are Last In, First Out (LIFO)
        while current:
            stack.append(current)
            current = current.left

        # As mentioned above, since stacks are LIFO, the element being popped will be the nth
        # smallest node where n represents the number of traversals
        current = stack.pop()

        # After popping, update the current nth smallest node
        n += 1

        # If the nth smallest node is equal to the kth smallest index return the value
        if n == k:
            return current.val
        
        # Update the current pointer to the right pointer of the nth smallest value.
        # This is because the right value is always the nth + 1 node
        current = current.right

    return 0
