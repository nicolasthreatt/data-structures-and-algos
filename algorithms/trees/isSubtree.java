/*
Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:
    * The number of nodes in the root tree is in the range [1, 2000].
    * The number of nodes in the subRoot tree is in the range [1, 1000].
    * -10^4 <= root.val <= 10^4
    * -10^4 <= subRoot.val <= 10^4 
*/
package algorithms.trees;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

public class isSubtree {

    // Algorithm(s) Used: Depth First Search, Recursion
    // Time Complexity: O(root * subRoot)
    // Space Complexity: O(root)
    private boolean isSameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;
        if (root.val != subRoot.val) return false;

        return isSameTree(root.left, subRoot.left) && isSameTree(root.right, subRoot.right);
    }

    // Algorithm(s) Used: Depth First Search, Recursion
    // Time Complexity: O(root * subRoot)
    // Space Complexity: O(root)
    public boolean isSubtreeI(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        if (subRoot == null) return true;
        if (isSameTree(root, subRoot) == true) return true;

        return isSubtreeI(root.left, subRoot) || isSubtreeI(root.right, subRoot);
    }
}
