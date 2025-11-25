package algorithms.trees;
import java.util.HashSet;
import java.util.Set;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

// Space Complexity: O(n), where n is the number of nodes in the tree
// Time Complexity: O(n), where n is the number of nodes in the tree
public class BinaryTreeTraversal {

    private Set<Integer> visit = new HashSet<>();

    // Algorithm(s) Used: Depth First Search (DFS), In Order Traversal (Left -> Root -> Right)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    private void inOrderTraversal(TreeNode node) {
        if (node != null) {
            inOrderTraversal(node.left);
            visit.add(node.val);
            inOrderTraversal(node.right);
        }
    }

    // Algorithm(s) Used: Depth First Search (DFS), Pre Order Traversal (Root -> Left -> Right)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    private void preOrderTraversal(TreeNode node) {
        if (node != null) {
            visit.add(node.val);
            preOrderTraversal(node.left);
            preOrderTraversal(node.right);
        }
    }

    // Algorithm(s) Used: Depth First Search (DFS), Post Order Traversal (Left -> Right -> Root)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    private void postOrderTraversal(TreeNode node) {
        if (node != null) {
            postOrderTraversal(node.left);
            postOrderTraversal(node.right);
            visit.add(node.val);
        }
    }

    public void run(TreeNode root) {
        inOrderTraversal(root);
        preOrderTraversal(root);
        postOrderTraversal(root);
    }
}
