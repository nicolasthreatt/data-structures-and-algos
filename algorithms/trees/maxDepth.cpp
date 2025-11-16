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

#include <iostream>
#include <algorithm>
#include <cassert>
#include <queue>
#include <stack>
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

// Algorithm(s) Used: Level Order Traversal, Breadth First Search, Queue (FIFO)
// Time Complexity: O(n)
// Space Complexity: O(n)
int maxDepthI(TreeNode* root) {
    if (!root) return 0;

    int max_depth = 0;

    // Initialize a queue (FIFO) to hold current nodes at each level
    queue<TreeNode*> q;
    q.push(root);

    // Breadth First Search:
    // Iterate while the queue isn't empty
    //  - For the length of the current queue size, pop the least recent node from the queue (FIFO):
    //  - If node exists, add it to the level and append the node's left and right children to the queue
    // After looping through current nodes in queue, update maxiumum depth
    while (!q.empty()) {
        for (int i = 0; i < q.size(); i++) {
            TreeNode* node = q.front();

            if (node->left != nullptr) {
                q.push(node->left);
            }

            if (node->right != nullptr) {
                q.push(node->right);
            }

            q.pop();
        }
        max_depth += 1;
    }

    return max_depth;
}

// Algorithm(s) Used: Pre Order Traversal, Depth First Search, Iterative, Stack (LIFO)
// Time Complexity: O(n)
// Space Complexity: O(n)
int maxDepthII(TreeNode* root) {
    if (!root) return 0;

    int max_depth = 0;

    // Initialize a stack (LIFO) to hold current nodes at each level
    stack<pair<TreeNode*, int>> stack;  // (node, depth)
    stack.push({root, 1});

    // Iterate while the stack is not empty
    //  - For each iteration pop the last item inserted into the stack,
    //    whcih wil contain a node and its depth within the tree.
    //  - If the nod exist, recompute the maximum depth and its children to the stack
    while (!stack.empty()) {
        pair<TreeNode*, int> curr = stack.top();
        TreeNode* node = curr.first;
        int depth = curr.second;

        if (node != nullptr) {
            max_depth = max(max_depth, depth);
            stack.push({node->left, depth + 1});
            stack.push({node->right, depth + 1});
        }

        stack.pop();
    }

    return max_depth;
}

// Helper function to perform depth first search on a binary tree
static int dfs(TreeNode* node, int height) {
    if (!node) return height;

    return max(dfs(node->left, height + 1), dfs(node->right, height + 1));

}

// Algorithm(s) Used: Depth First Search Resursive
// Time Complexity: O(n)
// Space Complexity: O(n)
int maxDepthIII(TreeNode* root) {
    return dfs(root, 0);
}

// Algorithm(s) Used: Depth First Search Resursive
// Time Complexity: O(n)
// Space Complexity: O(n)
int maxDepthIV(TreeNode* root) {
    if (!root) return 0;

    return 1 + max(maxDepthIV(root->left), maxDepthIV(root->right));
}

// Helper function to build a tree from a level-order vector (-100001 = null sentinel)
TreeNode* buildTree(const vector<int>& arr) {
    if (arr.empty()) return nullptr;

    vector<TreeNode*> nodes(arr.size(), nullptr);

    for (size_t i = 0; i < arr.size(); ++i) {
        if (arr[i] != -100001)
            nodes[i] = new TreeNode(arr[i]);
    }

    for (size_t i = 0; i < arr.size(); ++i) {
        if (!nodes[i]) continue;
        size_t left = 2 * i + 1;
        size_t right = 2 * i + 2;
        if (left < arr.size()) nodes[i]->left = nodes[left];
        if (right < arr.size()) nodes[i]->right = nodes[right];
    }

    return nodes[0];
}

// Struct to hold test case data
struct TestCase {
    vector<int> input;
    int expected;
};

int main() {
    vector<TestCase> testCases = {
        {{3,9,20,-100001,-100001,15,7}, 3},
        {{1,-100001,2}, 2},
        {{}, 0},
        {{1}, 1},
        {{1,2,3,4,5}, 3},
        {{1,2,3,4,-100001,-100001,7}, 3},
        {{1,2,3,4,5,6,7,8,9}, 4}
    };

    for (size_t i = 0; i < testCases.size(); ++i) {
        TreeNode* root = buildTree(testCases[i].input);
        int expected = testCases[i].expected;

        assert(maxDepthI(root) == expected);
        assert(maxDepthII(root) == expected);
        assert(maxDepthIII(root) == expected);
        assert(maxDepthIV(root) == expected);
    }

    return 0;
}
