/*
Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
    Output: false

Constraints:
    * The number of nodes in the root tree is in the range [1, 2000].
    * The number of nodes in the subRoot tree is in the range [1, 1000].
    * -10^4 <= root.val <= 10^4
    * -10^4 <= subRoot.val <= 10^4 
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


// Algorithm(s) Used: Depth First Search, Recursion
// Time Complexity: O(root * subRoot)
// Space Complexity: O(root)
bool isSameTree(TreeNode *node, TreeNode *subNode) {
    if (node == nullptr and subNode == nullptr) {
        return true;
    }

    if (node == nullptr || subNode == nullptr) {
        return false;
    }

    if (node->val != subNode->val) {
        return false;
    }

    return isSameTree(node->left, subNode->left) && isSameTree(node->right, subNode->right);
}

// Algorithm(s) Used: Depth First Search, Recursion
// Time Complexity: O(root * subRoot)
// Space Complexity: O(root)
bool isSubtree(TreeNode *root, TreeNode *subRoot) {
    if (root == nullptr) return false;

    if (subRoot == nullptr) return true;

    if (isSameTree(root, subRoot)) return true;

    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
}

int main() {

    // Helper function to uild example 1 root
    auto build_first_root = []() {
        TreeNode* root = new TreeNode(3);
        root->left = new TreeNode(4);
        root->right = new TreeNode(5);
        root->left->left = new TreeNode(1);
        root->left->right = new TreeNode(2);
        return root;
    };

    // Helper function to  build example 1 subroot
    auto build_first_subroot = []() {
        TreeNode* sub = new TreeNode(4);
        sub->left = new TreeNode(1);
        sub->right = new TreeNode(2);
        return sub;
    };

    TreeNode* r1 = build_first_root();
    TreeNode* s1 = build_first_subroot();
    assert(isSubtree(r1, s1) == true);

    // Helper function to  build example 2 root
    auto build_second_root = []() {
        TreeNode* root = new TreeNode(3);
        root->left = new TreeNode(4);
        root->right = new TreeNode(5);
        root->left->left = new TreeNode(1);
        root->left->right = new TreeNode(2);
        root->left->right->left = new TreeNode(0);
        return root;
    };

    // Helper function to  build example 2 subroot
    auto build_second_subroot = []() {
        TreeNode* sub = new TreeNode(4);
        sub->left = new TreeNode(1);
        sub->right = new TreeNode(2);
        return sub;
    };

    TreeNode* r2 = build_second_root();
    TreeNode* s2 = build_second_subroot();
    assert(isSubtree(r2, s2) == false);

    return 0;
}
