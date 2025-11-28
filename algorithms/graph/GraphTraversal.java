/*
Breadth-First Search (BFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores all the vertices of a tree/graph in breadth-first order,
      i.e., visiting all the vertices at the same level before moving to the next level. 
    * BFS can be implemented using a queue.
    * BFS is useful for finding the shortest path or exploring all the nodes in a tree or graph.

Depth-First Search (DFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores as far as possible along each branch before backtracking. 
    * DFS can be implemented using recursion or an explicit stack.
    * DFS is often used when searching for a specific node or finding a path between two nodes.
*/
package algorithms.graph;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;


// Definition for a Node
class Node {
    int val;
    List<Node> neighbors;

    Node(int val, List<Node> neighbors) {
        this.val = val;
        this.neighbors = (neighbors != null) ? neighbors : new ArrayList<>();
    }

    Node(int val) {
        this(val, null);
    }
}


public class GraphTraversal {

    private Set<Node> visited = new HashSet<>();

    // Algorithm(s) Used: Breadth First Search - Visit Neighbors First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    private void bfs(Node node) {
        Queue<Node> queue = new LinkedList<>();

        queue.add(node);
        while (!queue.isEmpty()) {
            Node n = queue.poll();
            if (!visited.contains(n)) {
                visited.add(n);
                for (Node neighbor : n.neighbors) {
                    if (!visited.contains(neighbor)) {
                        queue.add(neighbor);
                    }
                }
            }
        }
    }

    // Algorithm(s) Used: Depth First Search (Iterative) - Follow Path First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    private void iterativeDFS(Node node) {
        Stack<Node> stack = new Stack<>();

        stack.push(node);
        while (!stack.isEmpty()) {
            Node n = stack.pop();
            if (!visited.contains(n)) {
                visited.add(n);
                for (Node neighbor : n.neighbors) {
                    if (!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
            }
        }
    }

    // Algorithm(s) Used: Depth First Search (Recursive) - Follow Path First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    private void recursiveDFS(Node node) {
        if (node == null || visited.contains(node)) return;

        visited.add(node); // PRE-order
        for (Node neighbor : node.neighbors) {
            if (!visited.contains(neighbor)) {
                recursiveDFS(neighbor);
            }
        }
        // visited.add(node); // POST-order
    }

    public void run(Node node) {
        visited = new HashSet<>();
        bfs(node);

        visited = new HashSet<>();
        iterativeDFS(node);

        visited = new HashSet<>();
        recursiveDFS(node);
    }
}
