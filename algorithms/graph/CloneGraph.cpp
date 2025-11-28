/*
Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 
Test case format:
    * For simplicity, each node's value is the same as the node's index (1-indexed).
    * For example, the first node with val == 1, the second node with val == 2, and so on.
    * The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example 1:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 copies in the graph.
        * 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        * 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        * 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        * 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
    Input: adjList = [[]]
    Output: [[]]

Example 3:
    Input: adjList = []
    Output: []

Constraints:
    * The number of copies in the graph is in the range [0, 100].
    * 1 <= Node.val <= 100
    * Node.val is unique for each node.
    * There are no repeated edges and no self-loops in the graph.
    * The Graph is connected and all copies can be visited starting from the given node.
*/

#include <map>
#include <vector>

using namespace std;

// Definition for a Node
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


// Algorithm(s) Used: Graph, Depth First Search, Map
// Time Complexity: O(V + E)
// Space Complexity: O(V)
class CloneGraph {
private:
    map<Node*, Node*> copies = {};

public:
    Node* clone(Node* node) {
        // Base Case - No Node
        if (node == nullptr) {
            return nullptr;
        }

        // Base Case - Node Has Already Been Copied
        if (copies.contains(node)) {
            return copies.at(node);
        }

        // Now it's known that a copy of the node does not exist
        // Create copy of node then add it to the old to new copies map
        Node* copy = new Node(node->val);
        copies.insert({node, copy});

        // Recursively clone all the neighbors of the current node
        for (Node* neighbor : node->neighbors) {
            copy->neighbors.push_back(clone(neighbor));
        }

        return copy;
    }
};
