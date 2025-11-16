/*
Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

Example 2:
    Input: root = [1,null,2]
    Output: 2

Constraints:
    * The number of nodes in the tree is in the range [0, 104].
    * -100 <= Node.val <= 100

Breadth First Search:
    * Tree traversal algorithm that explores nodes level by level.
    * Using a queue to store frontier nodes supports the behavior of this search.

Depth First Search:
    * Tree traversal algorithm that goes deep into a tree exploring for nodes branch by branch.
    * Using a stack to store frontier nodes supports the behavior of this search.
 */
package algorithms.trees;

import java.util.Queue;
import java.util.Stack;
import java.util.PriorityQueue;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

// Helper class to store a node together with its depth.
class NodeDepth {
    TreeNode node;
    int depth;

    NodeDepth(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}

public class MaxDepth {

    // Algorithm(s) Used: Pre Order Traversal, BREADTH First Seach, Queue (FIFO)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int maxDepthI(TreeNode root) {
        if (root == null) return 0;

        int maxDepth = 0;

        Queue<TreeNode> queue = new PriorityQueue<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            for (int i = 0; i < queue.size(); i++) {
                TreeNode node = queue.remove();
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            maxDepth += 1;
        }

        return maxDepth;
    }

    // Algorithm(s) Used: Pre Order Traversal, DEPTH First Traversal, Iterative, Stack (LIFO)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int maxDepthII(TreeNode root) {
        if (root == null) return 0;

        int maxDepth = 0;

        Stack<NodeDepth> stack = new Stack<>();
        stack.push(new NodeDepth(root, 1));

        while (!stack.isEmpty()) {
            NodeDepth nodeDepth = stack.firstElement();

            TreeNode node = nodeDepth.node;
            if (node != null) {
                int depth = nodeDepth.depth;
                maxDepth = Math.max(maxDepth, depth);

                stack.push(new NodeDepth(node.left, depth + 1));
                stack.push(new NodeDepth(node.right, depth + 1));
            }

            stack.pop();
        }

        return maxDepth;        
    }

    // Helper function to perform depth first search on a binary tree
    private int dfs(TreeNode node, int height) {
        if (node == null) return height;

        return Math.max(dfs(node.left, height + 1), dfs(node.right, height + 1));
    }

    // Algorithm(s) Used: Depth First Traversals, Recursion
    // Time Complexity: O(n)
    // Space Complexity:
    public int maxDepthIII(TreeNode root) {
        return dfs(root, 0);
    }

    // Algorithm(s) Used: Depth First Traversals, Recursion
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int maxDepthIV(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + Math.max(maxDepthIV(root.left), maxDepthIV(root.right)); 
    }
}
