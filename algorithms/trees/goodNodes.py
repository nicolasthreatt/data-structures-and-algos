'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: 
    - Nodes in blue are good.
    - Root Node (3) is always a good node.
    - Node 4 -> (3,4) is the maximum value in the path starting from the root.
    - Node 5 -> (3,4,5) is the maximum value in the path
    - Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:
    * The number of nodes in the binary tree is in the range [1, 10^5].
    * Each node's value is between [-10^4, 10^4].
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: Depth-First Search, Preorder Traversal, Recursion
# Time Complexity: O(n)
# Space Complexity: O(log(n)) = O(h)
def goodNodes(root: TreeNode) -> int:

    # Pre-Order Depth First Search
    def dfs(node: TreeNode, maxPathValue: int)  -> TreeNode:
        # Base Case:
        #   - Empty nodes are not good nodes
        if not node:
            return 0
        
        # Node exist so determine if its good or bad
        good_nodes = 1 if node.val >= maxPathValue else 0

        # Update the path's max value
        maxPathValue = max(maxPathValue, node.val)

        # Recursive Base (Moving towards base case)
        # Add the left and right subtrees' good nodes to the number of good nodes
        good_nodes += dfs(node.left, maxPathValue)
        good_nodes += dfs(node.right, maxPathValue)

        # Return the count of the number of good nodes found in the tree
        return good_nodes
    
    # Nested Recursive Function Call
    return dfs(root, root.val)