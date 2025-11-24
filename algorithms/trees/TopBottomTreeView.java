/*
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
*/

package algorithms.trees;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) { this.val = val; }
}

// Definition for a pair holding a TreeNode and its horizontal distance
class PairNodeInt<T, U> {
    TreeNode node;
    Integer position;

    PairNodeInt(TreeNode node, Integer position) {
        this.node = node;
        this.position = position;
    }
}

// Definition for a pair holding a horizontal position and node value
class PairIntInt<T, U> {
    Integer position;
    Integer val;

    PairIntInt(Integer position, Integer val) {
        this.position = position;
        this.val = val;
    }
}

public class TopBottomTreeView {

    private HashSet<Integer> seen = new HashSet<>(); 
    private Map<Integer, Integer> bottomViewNodes = new HashMap<>(); // {"position": -> node.val}
    private List<PairIntInt<Integer, Integer>> topViewNodes = new ArrayList<>(); // (position, node.val)

    // Algorithm(s) Used: Level Order Traversal, BREADTH First Search, Queue, Iterative
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public int[] bottomTreeViewBFS(TreeNode root) {
        if (root == null) return new int[0];

        Queue<PairNodeInt<TreeNode, Integer>> queue = new LinkedList<>();
        queue.add(new PairNodeInt<>(root, 0));

        while (!queue.isEmpty()) {
            PairNodeInt<TreeNode, Integer> pair = queue.poll();

            TreeNode node = pair.node;
            int horizontal_depth = pair.position;

            // Overwrite bottom-most node at each horizontal distance
            bottomViewNodes.put(horizontal_depth, node.val);

            if (node.left != null) queue.add(new PairNodeInt<>(node.left, horizontal_depth - 1));
            if (node.right != null) queue.add(new PairNodeInt<>(node.right, horizontal_depth + 1));
        }

        List<Integer> horizontalDistances = new ArrayList<>(bottomViewNodes.keySet());
        Collections.sort(horizontalDistances); // nlog(n)

        int[] result = new int[horizontalDistances.size()];
        for (int i = 0; i < horizontalDistances.size(); i++) {
            result[i] = bottomViewNodes.get(horizontalDistances.get(i));
        }

        return result;
    }

    // Helper function to perform depth first search on a binary tree (Bottom View)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public Map<Integer, Integer> bottomViewDFS(TreeNode node, int horizontal_depth) {
        if (node == null) return null;

        // Overwrite bottom-most node at each horizontal distance
        bottomViewNodes.put(horizontal_depth, node.val);

        bottomViewDFS(node.left, horizontal_depth - 1);
        bottomViewDFS(node.right, horizontal_depth + 1);

        return bottomViewNodes;
    }

    // Algorithm(s) Used: In Order Traversal (Left -> Root -> Right), Depth First Search, Recursion
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public int[] bottomTreeViewDFS(TreeNode root) {
        bottomViewDFS(root, 0);

        List<Integer> horizontalDistances = new ArrayList<>(bottomViewNodes.keySet());
        Collections.sort(horizontalDistances); // nlog(n)

        int[] result = new int[horizontalDistances.size()];
        for (int i = 0; i < horizontalDistances.size(); i++) {
            result[i] = bottomViewNodes.get(horizontalDistances.get(i));
        }

        return result;
    }

    // Algorithm(s) Used: Level Order Traversal, BREADTH First Search, Queue, Iterative
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public int[] topTreeViewBFS(TreeNode root) {
        if (root == null) return new int[0];

        Queue<PairNodeInt<TreeNode, Integer>> queue = new LinkedList<>();
        queue.add(new PairNodeInt<>(root, 0));

        while (!queue.isEmpty()) {
            PairNodeInt<TreeNode, Integer> pair = queue.poll();

            TreeNode node = pair.node;
            int horizontal_depth = pair.position;

            if (!seen.contains(horizontal_depth)) {
                seen.add(horizontal_depth);
                topViewNodes.add(new PairIntInt<>(horizontal_depth, node.val));
            }

            if (node.left != null) queue.add(new PairNodeInt<>(node.left, horizontal_depth - 1));
            if (node.right != null) queue.add(new PairNodeInt<>(node.right, horizontal_depth + 1));
        }

        topViewNodes.sort(Comparator.comparingInt(p -> p.position));

        int[] result = new int[topViewNodes.size()];
        for (int i = 0; i < topViewNodes.size(); i++) {
            result[i] = topViewNodes.get(i).val;
        }

        return result;
    }

    // Helper function to perform depth first search on a binary tree (Top View)
    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public List<PairIntInt<Integer, Integer>> topViewDFS(TreeNode node, int horizontal_depth) {
        if (node == null) return null;

        if (!seen.contains(horizontal_depth)) {
            topViewNodes.add(new PairIntInt<>(horizontal_depth, node.val));
            seen.add(horizontal_depth);
        }

        topViewDFS(node.left, horizontal_depth - 1);
        topViewDFS(node.right, horizontal_depth + 1);

        return topViewNodes;
    }

    // Algorithm(s) Used: In Order Traversal (Left -> Root -> Right), Depth First Search, Recursion
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public int[] topTreeViewDFS(TreeNode root) {
        topViewDFS(root, 0);

        topViewNodes.sort(Comparator.comparingInt(p -> p.position));

        int[] result = new int[topViewNodes.size()];
        for (int i = 0; i < topViewNodes.size(); i++) {
            result[i] = topViewNodes.get(i).val;
        }

        return result;
    }       
}
