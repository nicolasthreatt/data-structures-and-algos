"""
Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    * The number of nodes in both trees is in the range [2, 10^4].
    * 0 <= Node.val <= 10^5
"""

from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: In-Order Traversal, Depth First Search, Recursion
# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(n), where n is the number of nodes in the tree
class GetMinimumDifference:
    def __init__(self):
        self.prev = None
        self.min_diff = float('inf')

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        
        self.dfs(node.left)

        if self.prev:
            self.min_diff = min(abs(node.val - self.prev.val), self.min_diff)
        self.prev = node

        self.dfs(node.right)

        return self.min_diff if self.min_diff != float('inf') else 0


if __name__ == "__main__":

    def build_first_root():
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        return root
    assert GetMinimumDifference().dfs(build_first_root()) == 1


    def build_second_root():
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        return root
    assert GetMinimumDifference().dfs(build_second_root()) == 1


    def build_third_root():
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(18)
        return root
    assert GetMinimumDifference().dfs(build_third_root()) == 2


    def build_fourth_root():
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        root.right.right.right.right = TreeNode(5)
        return root
    assert GetMinimumDifference().dfs(build_fourth_root()) == 1


    def build_fifth_root():
        # [100, 50, 150, 49, 51]
        root = TreeNode(100)
        root.left = TreeNode(50)
        root.right = TreeNode(150)
        root.left.left = TreeNode(49)
        root.left.right = TreeNode(51)
        return root
    assert GetMinimumDifference().dfs(build_fifth_root()) == 1


    def build_sixth_root():
        root = TreeNode(100000)
        root.left = TreeNode(1)
        root.right = TreeNode(50000)
        return root
    assert GetMinimumDifference().dfs(build_sixth_root()) == 50000


    def build_seventh_root():
        """
             8
           /   \
          3    10
         / \     \
        1   6    14
        """
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.right.right = TreeNode(14)
        return root
    assert GetMinimumDifference().dfs(build_seventh_root()) == 2