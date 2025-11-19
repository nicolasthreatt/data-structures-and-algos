/*
Same Tree
https://leetcode.com/problems/same-tree

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
    * The number of nodes in both trees is in the range [0, 100].
    * -10^4 <= Node.val <= 10^4
*/

#include <iostream>
#include <vector>
#include <queue>
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

// Algorithm Used: Pre-Order Traversal, Depth First Search, Recursion
// Time Complexity: O(p + q)
// Space Complexity: Time Complexity: O(p + q)
bool isSameTree(TreeNode* p, TreeNode* q) {
    // Base Case: If both p and q are empty, both trees have finished traversing at the same time
    if (p == nullptr && q == nullptr) return true;

    // NOTE: Now that it is known that p and q BOTH EXIST
    // Base Case: If only one of either p and q are empty, then p and q can't be the same
    if (p == nullptr || q == nullptr) return false;

    // NOTE: Now that it is known that p and q are BOTH NOT NULL
    // Base Case: If the current node of p and q aren't the same, then p and q can't be the same
    if (p->val != q->val) return false;

    // NOTE: Now that it is known that p and q nodes have the same value
    // Two trees can only be the same if their left and right subtrees are also the same
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

// Helper function to build a tree from a level-order vector (-100001 = null sentinel)
TreeNode* buildTree(const vector<int>& vals) {
    if (vals.empty()) return nullptr;

    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;

    while (!q.empty() && i < vals.size()) {
        TreeNode* node = q.front();
        q.pop();

        if (i < vals.size() && vals[i] != -100001) {
            node->left = new TreeNode(vals[i]);
            q.push(node->left);
        }
        i++;

        if (i < vals.size() && vals[i] != -100001) {
            node->right = new TreeNode(vals[i]);
            q.push(node->right);
        }
        i++;
    }

    return root;
}

// Struct to hold test case data
struct TestCase {
    vector<int> p;
    vector<int> q;
    bool expected;
};

int main() {
    vector<TestCase> testCases = {
        {{1,2,3}, {1,2,3}, true},
        {{1,2}, {1,-100001,2}, false},
        {{1,2,1}, {1,1,2}, false},
        {{}, {}, true},
        {{1}, {}, false},
        {{1,2,3,4,5,6,7}, {1,2,3,4,5,6,7}, true},
        {{1,2,3,4,5}, {1,2,3,4,6}, false}
    };

    for (size_t i = 0; i < testCases.size(); ++i) {
        TreeNode* p = buildTree(testCases[i].p);
        TreeNode* q = buildTree(testCases[i].q);
        bool result = isSameTree(p, q);
        assert(result == testCases[i].expected);
    }

    return 0;
}
