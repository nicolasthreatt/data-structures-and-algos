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

#include <algorithm>
#include <cassert>
#include <queue>
#include <map>
#include <set>
#include <iostream>
#include <vector>

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

// Algorithm(s) Used: Level Order Traversal, BREADTH First Search, Queue, Iterative
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<int> bottomTreeViewBFS(TreeNode* root) {
    if (root == nullptr) return {};

    map<int, int> bottomViewNodes = {};

    queue<pair<TreeNode*, int>> queue = {};
    queue.push({root, 0});

    while (!queue.empty()) {
        pair<TreeNode*, int> pair = queue.front();

        TreeNode *node = pair.first;
        int position = pair.second;

        bottomViewNodes[position] = node->val;

        if (node->left != nullptr) queue.push({node->left, position - 1});
        if (node->right != nullptr) queue.push({node->right, position + 1});

        queue.pop();
    }

    vector<int> positions = {};
    for (const auto& node : bottomViewNodes) {
        positions.push_back(node.first);
    }
    ranges::sort(positions);

    vector<int> result = {};
    for (int position : positions) {
        result.push_back(bottomViewNodes[position]);
    }

    return result;
}

// Helper function to perform depth first search on a binary tree (Bottom View)
// Time Complexity: O(n)
// Space Complexity: O(n)
void bottomViewDFS(TreeNode* node, int position, map<int, int>& bottomViewNodes) {
    if (node == nullptr) return;

    bottomViewNodes[position] = node->val;

    bottomViewDFS(node->left, position - 1, bottomViewNodes);
    bottomViewDFS(node->right, position + 1, bottomViewNodes);

    return;
}

// Algorithm(s) Used: In Order Traversal (Left -> Root -> Right), Depth First Search, Recursion
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<int> bottomTreeViewDFS(TreeNode* root) {
    if (root == nullptr) return {};

    map<int, int> bottomViewNodes = {};

    bottomViewDFS(root, 0, bottomViewNodes);

    vector<int> positions;
    for (const auto& node : bottomViewNodes) {
        positions.push_back(node.first);
    }
    ranges::sort(positions);

    vector<int> result = {};
    for (int position : positions) {
        result.push_back(bottomViewNodes[position]);
    }

    return result;
}

// Algorithm(s) Used: Level Order Traversal, BREADTH First Seaerch, Queue, Iteration
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<int> topTreeViewBFS(TreeNode* root) {
    if (root == nullptr) return {};

    vector<pair<int, int>> topViewNodes; // (position, node.val)

    set<int> seen = {}; // position
    queue<pair<TreeNode*, int>> queue = {};  // (node, position)
    queue.push({root, 0});

    while (!queue.empty()) {
        const auto& pair = queue.front();

        TreeNode* node = pair.first;
        int position = pair.second;

        if (!seen.contains(position)) {
            seen.insert(position);
            topViewNodes.push_back({position, node->val});
        }

        if (node->left != nullptr) queue.push({node->left, position - 1});
        if (node->right != nullptr) queue.push({node->right, position + 1});

        queue.pop();
    }

    sort(topViewNodes.begin(), topViewNodes.end());

    vector<int> result;
    for (const auto& node : topViewNodes) {
        result.push_back(node.second);
    }

    return result;
}

// Helper function to perform depth first search on a binary tree (Top View)
// Time Complexity: O(n)
// Space Complexity: O(n)
void topViewDFS(TreeNode* node,
                int position,
                set<int>& seen,
                vector<pair<int, int>>& topViewNodes) {
    if (node == nullptr) return;

    if (!seen.contains(position)) {
        topViewNodes.push_back({position, node->val});
        seen.insert(position);
    }

    topViewDFS(node->left,  position - 1, seen, topViewNodes);
    topViewDFS(node->right, position + 1, seen, topViewNodes);
}

// Algorithm(s) Used: In Order Traversal (Left -> Root -> Right), Depth First Search, Recursion
// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
vector<int> topTreeViewDFS(TreeNode* root) {
    if (root == nullptr) return {};

    set<int> seen = {}; // position
    vector<pair<int, int>> topViewNodes; // (position, node.val)

    topViewDFS(root, 0, seen, topViewNodes);
    sort(topViewNodes.begin(), topViewNodes.end());

    vector<int> result;
    for (const auto& node : topViewNodes) {
        result.push_back(node.second);
    }

    return result;
}

int main() {

    auto buildFirstTree = []() -> TreeNode* {
        /*
                1
               / \
              2   3
               \
                4
        Bottom: [2,4,3]
        Top:    [2,1,3]
        */
        TreeNode* root = new TreeNode(1);
        root->left = new TreeNode(2);
        root->right = new TreeNode(3);
        root->left->right = new TreeNode(4);
        return root;
    };

    TreeNode* root1 = buildFirstTree();
    vector<int> expectedBottom1 = {2, 4, 3};
    vector<int> expectedTop1 = {2, 1, 3};
    assert(bottomTreeViewBFS(root1) == expectedBottom1);
    assert(bottomTreeViewDFS(root1) == expectedBottom1);
    assert(topTreeViewBFS(root1) == expectedTop1);
    assert(topTreeViewDFS(root1) == expectedTop1);

    auto buildSecondTree = []() -> TreeNode* {
        /*
                1
               / \
              2   3
               \
                4
               /
              5
        Bottom: [5,4,3]
        Top:    [2,1,3]
        */
        TreeNode* root = new TreeNode(1);
        root->left = new TreeNode(2);
        root->right = new TreeNode(3);
        root->left->right = new TreeNode(4);
        root->left->right->left = new TreeNode(5);
        return root;
    };

    TreeNode* root2 = buildSecondTree();
    vector<int> expectedBottom2 = {5, 4, 3};
    vector<int> expectedTop2 = {2, 1, 3};
    assert(bottomTreeViewBFS(root2) == expectedBottom2);
    assert(bottomTreeViewDFS(root2) == expectedBottom2);
    assert(topTreeViewBFS(root2) == expectedTop2);
    assert(topTreeViewDFS(root2) == expectedTop2);

    return 0;
}
