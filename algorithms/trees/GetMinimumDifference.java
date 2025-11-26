/*
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
 */
package algorithms.trees;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

// Algorithm Used: In-Order Traversal, Depth First Search, Recursion
// Time Complexity: O(n), where n is the number of nodes in the tree
// Space Complexity: O(n), where n is the number of nodes in the tree
public class GetMinimumDifference {
    private TreeNode prev = null;
    private int min_diff = Integer.MAX_VALUE;

    public int run(TreeNode root) {
        dfs(root);
        return min_diff == Integer.MAX_VALUE ? 0 : min_diff;
    }

    private void dfs(TreeNode node) {
        if (node == null) {
            return;
        }

        dfs(node.left);

        if (prev != null) {
            min_diff = Math.min(min_diff, Math.abs(node.val - prev.val));
        }
        prev = node;

        dfs(node.right);
    }
}
