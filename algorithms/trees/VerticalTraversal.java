/*
Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the root of a binary tree, return the vertical order traversal of its columns' values.
From top to bottom, column by column.
If two columns are in the same row and column, the order should be from left to right.

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
    * The number of columns in the tree is in the range [0, 1000].
    * -100 <= node.val <= 100
*/

package algorithms.trees;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.SortedMap;
import java.util.TreeMap;

// Definition for a binary tree node.
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

public class VerticalTraversal {

    // Map<Integer, List<Integer>>  columns = new HashMap<>();
    private SortedMap<Integer, List<Integer>> columns = new TreeMap<>();

    // Helper function to perform binary search of a binary tree
    // Time Complexity: O(n)
    // Space Complexity:  O(n)
    private void dfs(TreeNode node, Integer position) {
        if (node == null) return;

        if (!columns.containsKey(position)) {
            columns.put(position, new ArrayList<>());
        }

        List<Integer> nodes = columns.get(position);
        nodes.add(node.val);
        columns.put(position, nodes);

        dfs(node.left, position - 1);
        dfs(node.right, position + 1);
    }

    // Algorithm(s) Used: Breadth First Search (BFS), Queue, Iterative
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public List<List<Integer>> verticalTraversalI(TreeNode root) {
        if (root == null) return new ArrayList<>();

        Queue<PairNodeInt<TreeNode, Integer>> queue = new LinkedList<>(); // (node, position)
        queue.add(new PairNodeInt<>(root, 0));

        while (!queue.isEmpty()) {
            int n = queue.size();
            for (int i = 0; i < n; i++) {
                PairNodeInt<TreeNode, Integer> pair = queue.poll();

                TreeNode node = pair.node;
                Integer position = pair.position;

                if (!columns.containsKey(position)) {
                    columns.put(position, new ArrayList<>());
                }

                List<Integer> nodes = columns.get(position);
                nodes.add(node.val);
                columns.put(position, nodes);

                if (node.left != null) queue.add(new PairNodeInt<>(node.left, position - 1));
                if (node.right != null) queue.add(new PairNodeInt<>(node.right, position + 1));
            }
        }

        List<List<Integer>> result = new ArrayList<>(columns.size());
        for (List<Integer> nodes : columns.values()) {
            result.add(nodes);
        }

        return result;
    }

    // Algorithm(s) Used: Depth First Search (DFS), Pre Order Traversal, Recursive
    // Time Complexity: O(nlog(n))
    // Space Complexity: O(n)
    public List<List<Integer>> verticalTraversalII(TreeNode root) {
        if (root == null) return new ArrayList<>();

        dfs(root, 0);

        List<List<Integer>> result = new ArrayList<>(columns.size());
        for (List<Integer> nodes : columns.values()) {
            result.add(nodes);
        }

        return result;
    }
}
