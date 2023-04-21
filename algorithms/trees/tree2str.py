'''
https://leetcode.com/problems/construct-string-from-binary-tree/

Given the root of a binary tree, construct a string consisting of parenthesis and integers
from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping
relationship between the string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation:
    * Originally, it needs to be "1(2(4)())(3()())", but need to omit all the unnecessary empty parenthesis pairs.
      And it will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation:
    * Almost the same as the first example,
      except we cannot omit the first parenthesis pair to break the one-to-one mapping
      relationship between the input and the output.
 

Constraints:
    * The number of nodes in the tree is in the range [1, 10^4].
    * -1000 <= Node.val <= 1000
'''

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Algorithm Used: 
# Time Complexity: O(n)
# Space Complexity: O(n)
def tree2str(root: Optional[TreeNode]) -> str:
    # Create a list to store the string representation of the tree
    root_str = []

    def dfs_preorder(root: TreeNode) -> None:
        # If the node does not exist there is nothing to return (Base Case)
        if not root:
            return
        
        # For each node in the tree add an opening parenthesis followed by the node's value
        root_str.append("(")
        root_str.append(str(root.val))

        # If the left child is null but the right child is not null,
        # add an empty parenthesis set indicating a missing left child
        if not root.left and root.right:
            root_str.append("()")

        # Traverse down the root's left subtree follow by its right subtree
        dfs_preorder(root.left)
        dfs_preorder(root.right)
        
        # After each recursive dfs preorder call add a closing parenthesis indicating
        # the end of a path
        root_str.append(")")

    # Invoke the recursive function to get the string representation of the tree
    dfs_preorder(root)

    # Convert list to a string
    return "".join(root_str)[1:-1]
