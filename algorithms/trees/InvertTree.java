/*
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100 
*/
package algorithms.trees;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

public class InvertTree {

    // Helper function to perform depth first search on a binary tree
    private TreeNode dfs(TreeNode node) {
        if (node == null) return null;

        TreeNode left = dfs(node.left);
        TreeNode right = dfs(node.right);

        node.left = right;
        node.right = left;

        return node;
    }

    // Algorithm(s) Used: Depth First Search, Recursion
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public TreeNode invertTreeI(TreeNode root) {
        return dfs(root);
    }

    // Algorithm(s) Used: Depth First Search, Recursion
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public TreeNode invertTreeII(TreeNode root) {
        if (root == null) return null;

        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;

        invertTreeII(root.left);
        invertTreeII(root.right);

        return root;
    }
}
