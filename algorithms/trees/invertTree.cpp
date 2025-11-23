/*
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []

Constraints:
    * The number of nodes in the tree is in the range [0, 100].
    * -100 <= Node.val <= 100 
*/

#include <cassert>
#include <queue>
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

// Helper function to perform depth first search on a binary tree
TreeNode* dfs(TreeNode* node) {
    if (node == nullptr) return nullptr;

    TreeNode *left = dfs(node->left);
    TreeNode *right = dfs(node->right);

    node->left = right;
    node->right = left;

    return node;
}

// Algorithm(s) Used: Depth First Search, Recursion
// Time Complexity: O(n)
// Space Complexity: O(n)
TreeNode* invertTreeI(TreeNode* root) {
    return dfs(root);
}

// Algorithm(s) Used: Depth First Search, Recursion
// Time Complexity: O(n)
// Space Complexity: O(n)
TreeNode* invertTreeII(TreeNode* root) {
    if (root == nullptr) return nullptr;

    // Swap Nodes
    TreeNode *tmp = root->left;
    root->left = root->right;
    root->right = tmp;

    invertTreeII(root->left);
    invertTreeII(root->right);

    return root;
}

int main() {

    // Level-order to vector helper
    auto treeToList = [](TreeNode* root) -> vector<int> {
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            if (node) {
                result.push_back(node->val);
                q.push(node->left);
                q.push(node->right);
            } else {
                result.push_back(-101); // placeholder for null
            }
        }
        while (!result.empty() && result.back() == -101) result.pop_back();
        return result;
    };

    TreeNode* root1 = new TreeNode(4);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(7);
    root1->left->left = new TreeNode(1);
    root1->left->right = new TreeNode(3);
    root1->right->left = new TreeNode(6);
    root1->right->right = new TreeNode(9);
    invertTreeI(root1);
    assert(treeToList(root1) == vector<int>({4,7,2,9,6,3,1}));
    invertTreeII(root1);
    assert(treeToList(root1) == vector<int>({4,2,7,1,3,6,9}));

    TreeNode* root2 = new TreeNode(2);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(3);
    invertTreeI(root2);
    assert(treeToList(root2) == vector<int>({2,3,1}));
    invertTreeII(root2);
    assert(treeToList(root2) == vector<int>({2,1,3}));

    TreeNode* root3 = nullptr;
    invertTreeI(root3);
    assert(treeToList(root3) == vector<int>({}));
    invertTreeII(root3);
    assert(treeToList(root3) == vector<int>({}));

    return 0;
}
