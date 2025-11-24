"""
Amazon Interview Question

You are given a binary tree, and your task is to return its top and bottom view. 

Top view of a binary tree is set of nodes visible when tree is viewed from top, same from bottom.

Example 1:
       1
      / \
     2   3
      \
       4
Bottom view - [2,4,3]
Top View - [2,1,3]

Example 2:
       1
      / \
     2   3
      \
       4
      /
     5
Bottom view - [5,4,3]
Top View - [2,1,3]
"""

from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Tree BFS, Level-Order Traversal
# Time Complexity: O(n*log(n)), n nodes WITH sorting by horizontal distance
# Space Complexity: O(n), n nodes
def bottomTreeViewBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    bottom_view_nodes = dict()  # {position: -> node.val}
    queue = deque([(root, 0)])

    while queue:
        node, position = queue.popleft()

        bottom_view_nodes[position] = node.val  # Remove previous node with the same horizontal distance

        if node.left: queue.append((node.left, position - 1))
        if node.right: queue.append((node.right, position + 1))
    
    return [val for position, val in sorted(bottom_view_nodes.items(), key=lambda x: x[0])]


# Algorithm Used: Tree DFS, In-Order Traversal (LEFT -> ROOT -> RIGHT)
# Time Complexity: O(n*log(n)), n nodes WITH sorting by horizontal distance
# Space Complexity: O(n), n nodes
def bottomTreeViewDFS(root: Optional[TreeNode]) -> List[int]:
    bottom_view_nodes = dict()  # {"position": -> node.val}

    def dfs(node: Optional[TreeNode], position: int) -> dict:
        if not node:
            return

        bottom_view_nodes[position] = node.val  # Remove previous node with the same horizontal distance
        
        dfs(node.left, position - 1)
        dfs(node.right, position + 1)

        return bottom_view_nodes

    dfs(root, 0)
    return [val for position, val in sorted(bottom_view_nodes.items(), key=lambda x: x[0])]


# Algorithm Used: Tree BFS, Level-Order Traversal
# Time Complexity: O(n*log(n)), n nodes WITH sorting by horizontal distance
# Space Complexity: O(n), n nodes
def topTreeViewBFS(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    top_view_nodes = list()  # (position, node.val)
    queue = deque([(root, 0)])
    visited = set()

    while queue:
        node, position = queue.popleft()  # BFS -> popleft
        if position not in visited:
            visited.add(position)
            top_view_nodes.append((position, node.val))
        if node.left: queue.append((node.left, position  - 1))
        if node.right: queue.append((node.right, position  + 1))

    return [val for position, val in sorted(top_view_nodes, key=lambda x: x[0])]


# Algorithm Used: Tree DFS, In-Order Traversal (LEFT -> ROOT -> RIGHT)
# Time Complexity: O(n*log(n)), n nodes WITH sorting by horizontal distance
# Space Complexity: O(n), n nodes
def topTreeViewDFS(root: Optional[TreeNode]) -> List[int]:
    visited = set()
    top_view_nodes = list()  # (position, node.val)

    def dfs(node: Optional[TreeNode], position: int) -> list:
        if not node:
            return

        if position not in visited:
            top_view_nodes.append((position, node.val))
            visited.add(position)

        dfs(node.left, position - 1)
        dfs(node.right, position + 1)

        return top_view_nodes

    dfs(root, 0)
    return [val for position, val in sorted(top_view_nodes, key=lambda x: x[0])]


if __name__ == "__main__":
    def build_first_tree():
        """
            1
           / \
          2   3
           \
            4
        Bottom: [2,4,3]
        Top:    [2,1,3]
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        return root

    root1 = build_first_tree()
    assert bottomTreeViewBFS(root1) == [2, 4, 3]
    assert bottomTreeViewDFS(root1) == [2, 4, 3]
    assert topTreeViewBFS(root1) == [2, 1, 3]
    assert topTreeViewDFS(root1) == [2, 1, 3]

    def build_second_tree():
        """
            1
           / \
          2   3
           \
            4
           /
          5
        Bottom: [5,4,3]
        Top:    [2,1,3]
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(5)
        return root

    root2 = build_second_tree()
    assert bottomTreeViewBFS(root2) == [5, 4, 3]
    assert bottomTreeViewDFS(root2) == [5, 4, 3]
    assert topTreeViewBFS(root2) == [2, 1, 3]
    assert topTreeViewDFS(root2) == [2, 1, 3]
