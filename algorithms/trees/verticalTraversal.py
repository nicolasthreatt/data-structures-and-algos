"""
Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the root of a binary tree, return the vertical order traversal of its nodes' values.
From top to bottom, column by column.
If two nodes are in the same row and column, the order should be from left to right.

Example 1:
    Input: 
        3
       / \
      9  20
         / \
        15  7
    Output: [[9],[3,15],[20],[7]]

Example 2:
    Input: 
        1
       / \
      2   3
     / \ / \
    4  5 6  7
    Output: [[4],[2],[1,5,6],[3],[7]]

Example 3:
    Input: 
        1
         \
          2
           \
            3
    Output: [[1],[2],[3]]

Constraints:
    * The number of nodes in the tree is in the range [0, 1000].
    * -100 <= node.val <= 100
"""
from collections import defaultdict, OrderedDict
from typing import Optional, List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Breadth First Search (BFS), Queue, Iterative
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
def verticalTraveralI(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    columns = defaultdict(list) # {position: node.vals[]}
    queue = [(root, 0)] # (node, position)

    while queue:
        n = len(queue)
        for _ in range(n):
            node, position = queue.pop(0)
            columns[position] = columns.get(position, []) + [node.val]
            if node.left:
                queue.append((node.left, position - 1))
            if node.right:
                queue.append((node.right, position + 1))

    od = OrderedDict(sorted(columns.items()))
    return list(od.values())


# Algorithm Used: Depth First Search (DFS), Pre Order Traversal, Recursive
# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
def verticalTraversalII(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    columns = defaultdict(list) # {position: node.vals[]}

    def dfs(node: Optional[TreeNode], position: int):
        if not node:
            return

        columns[position].append(node.val) # Append value to the list for this column
        dfs(node.left, position - 1)
        dfs(node.right, position + 1)

    dfs(root, 0)

    return [columns[pos] for pos in sorted(columns.keys())]


if __name__ == "__main__":

    def build_example1_root():
        """
            3
           / \
          9  20
             / \
            15  7
        """
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root
    r1 = build_example1_root()
    assert verticalTraveralI(r1) == [[9], [3, 15], [20], [7]]
    assert verticalTraversalII(r1) == [[9], [3, 15], [20], [7]]

    def build_example2_root():
        """
               1
              / \
             2   3
            / \ / \
           4  5 6  7
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        return root
    r2 = build_example2_root()
    assert verticalTraveralI(r2) == [[4], [2], [1, 5, 6], [3], [7]]
    assert verticalTraversalII(r2) == [[4], [2], [1, 5, 6], [3], [7]]

    def build_example3_root():
        """
        1
         \
          2
           \
            3
        """
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        return root
    r3 = build_example3_root()
    assert verticalTraveralI(r3) == [[1], [2], [3]]
    assert verticalTraversalII(r3) == [[1], [2], [3]]

    def build_empty_root():
        return None
    r4 = build_empty_root()
    assert verticalTraveralI(r4) == []
    assert verticalTraversalII(r4) == []

    def build_single_root():
        return TreeNode(42)
    r5 = build_single_root()
    assert verticalTraveralI(r5) == [[42]]
    assert verticalTraversalII(r5) == [[42]]
