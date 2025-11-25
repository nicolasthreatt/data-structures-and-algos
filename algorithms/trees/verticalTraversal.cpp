/*
Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the root of a binary tree, return the vertical order traversal of its nodes' values.
From top to bottom, column by column.
If two nodes are in the same row and column, the order should be from left to right.

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
    * The number of nodes in the tree is in the range [0, 1000].
    * -100 <= node.val <= 100
*/

#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <cassert>

using namespace std;

// Definition for a binary tree node
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// Algorithm(s) Used: Breadth First Search (BFS), Queue, Iterative
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<vector<int>> verticalTraversalI(TreeNode* root) {
    if (root == nullptr) return {};

    map<int, vector<int>> columns; // {position:, nodes}

    queue<pair<TreeNode*, int>> queue; // (node, position)
    queue.push({root, 0});

    while (!queue.empty()) {
        size_t n = queue.size();
        for (int i = 0; i < n; i++) {
            TreeNode* node = queue.front().first;
            int position = queue.front().second;

            columns[position].push_back(node->val);

            if (node->left != nullptr) queue.push({node->left, position - 1});
            if (node->right != nullptr) queue.push({node->right, position + 1});

            queue.pop();
        }
    }

    vector<vector<int>> result;
    result.reserve(columns.size());

    for (const auto& entry : columns) {
        vector<int> nodes = entry.second;
        result.push_back(nodes);
    }

    return result;
}

// Helper function to perform depth first search on a binary tree (Bottom View)
// Time Complexity: O(n)
// Space Complexity: O(n)
void dfs(TreeNode* node, int position, map<int, vector<int>>& columns) {
    if (node == nullptr) return;

    columns[position].push_back(node->val);

    dfs(node->left, position - 1, columns);
    dfs(node->right, position + 1, columns);

    return;
}

// Algorithm(s) Used: Depth First Search (DFS), Pre Order Traversal, Recursive
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<vector<int>> verticalTraversalII(TreeNode* root) {
    if (root == nullptr) return {};

    map<int, vector<int>> columns;

    dfs(root, 0, columns);

    vector<vector<int>> result;
    result.reserve(columns.size());

    for (const auto& entry : columns) {
        vector<int> nodes = entry.second;
        result.push_back(nodes);
    }

    return result;
}

// Helper function to compare two vectors
bool equalVec(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    return a == b;
}

// Helper function to build tree for testing
TreeNode* build_example1_root() {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_example2_root() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_example3_root() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(3);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_empty_root() {
    return nullptr;
}

// Helper function to build tree for testing
TreeNode* build_single_root() {
    return new TreeNode(42);
}

int main() {
    TreeNode* r1 = build_example1_root();
    assert(equalVec(verticalTraversalI(r1), {{9}, {3, 15}, {20}, {7}}));
    assert(equalVec(verticalTraversalII(r1), {{9}, {3, 15}, {20}, {7}}));

    TreeNode* r2 = build_example2_root();
    assert(equalVec(verticalTraversalI(r2), {{4}, {2}, {1, 5, 6}, {3}, {7}}));
    assert(equalVec(verticalTraversalII(r2), {{4}, {2}, {1, 5, 6}, {3}, {7}}));


    TreeNode* r3 = build_example3_root();
    assert(equalVec(verticalTraversalI(r3), {{1}, {2}, {3}}));
    assert(equalVec(verticalTraversalII(r3), {{1}, {2}, {3}}));

    TreeNode* r4 = build_empty_root();
    assert(equalVec(verticalTraversalI(r4), {}));
    assert(equalVec(verticalTraversalII(r4), {}));

    TreeNode* r5 = build_single_root();
    assert(equalVec(verticalTraversalI(r5), {{42}}));
    assert(equalVec(verticalTraversalII(r5), {{42}}));

    return 0;
}
