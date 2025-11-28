/*
Breadth-First Search (BFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores all the vertices of a tree/graph in breadth-first order,
      i.e., visiting all the vertices at the same level before moving to the next level. 
    * Implemented by using a queue.
    * Useful for finding the shortest path or exploring all the nodes in a tree or graph.

Depth-First Search (DFS)
    * Algorithm for traversing or searching a tree or graph. 
    * Explores as far as possible along each branch before backtracking. 
    * DFS can be implemented using recursion or an explicit stack.
    * DFS is often used when searching for a specific node or finding a path between two nodes.
*/

#include <unordered_set>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

// Definition for a Node
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node(int val) : val(val) {}
    Node(int val, vector<Node*> neighbors) : val(val), neighbors(neighbors) {}
};

class GraphTraversal {
private:
    unordered_set<Node*> visited;

    // Algorithm(s) Used: Breadth First Search - Visit Neighbors First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    void bfs(Node* node) {
        queue<Node*> q;

        q.push(node);
        while (!q.empty()) {
            Node* n = q.front();
            if (!visited.contains(n)) {
                visited.insert(n);
                for (Node* neighbor : n->neighbors) {
                    if (!visited.contains(neighbor)) {
                        q.push(neighbor);
                    }
                }
            }
            q.pop();
        }
    }

    // Algorithm(s) Used: Depth First Search (Iterative) - Follow Path First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    void iterativeDFS(Node* node) {
        stack<Node*> stack;

        stack.push(node);
        while (!stack.empty()) {
            Node* n = stack.top();
            if (!visited.contains(n)) {
                visited.insert(n);
                for (Node* neighbor : n->neighbors) {
                    if (!visited.contains(neighbor)) {
                        stack.push(neighbor);
                    }
                }
            }
            stack.pop();
        }
    }

    // Algorithm(s) Used: Depth First Search (Recursive) - Follow Path First
    // Time Complexity: O(V + E)
    // Space Complexity: O(V)
    void recursiveDFS(Node* node) {
        if (!node || visited.contains(node)) return;
        visited.insert(node); // PRE-order
        for (Node* neighbor : node->neighbors) {
            recursiveDFS(neighbor);
        }
        // visited.add(node); // POST-order
    }

public:
    void run(Node* node) {
        visited.clear();
        bfs(node);

        visited.clear();
        iterativeDFS(node);

        visited.clear();
        recursiveDFS(node);
    }
};
