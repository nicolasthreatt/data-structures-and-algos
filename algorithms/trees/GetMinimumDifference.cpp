/*
Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Given the root of a Binary Search Tree (BST), return the minimum absolute
difference between the values of any two different nodes in the tree.

Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

Constraints:
    * The number of nodes in both trees is in the range [2, 10^4].
    * 0 <= Node.val <= 10^5
*/

#include <cassert>
#include <iostream>
#include <queue>
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

// Algorithm(s) Used: In-Order Traversal, Depth First Search, Recursion
// Time Complexity: O(n)
// Space Complexity:  O(n)
class GetMinimumDifference {
private:
    int diff = INT_MAX;
    TreeNode* prev = nullptr;
public:
    // Helper function to perform IN ORDER (Left -> Root -> Right) depth first seach
    int dfs(TreeNode* root) {
        if (!root) return 0;

        dfs(root->left);
        if (prev != nullptr) {
            diff = min(diff, abs(prev->val - root->val));
        }
        prev = root;
        dfs(root->right);

        return diff;
    }
};

// Helper function to build tree for testing
TreeNode* build_first_root() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(6);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_second_root() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(0);
    root->right = new TreeNode(48);
    root->right->left = new TreeNode(12);
    root->right->right = new TreeNode(49);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_third_root() {
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(15);
    root->left->left = new TreeNode(3);
    root->left->right = new TreeNode(7);
    root->right->left = new TreeNode(12);
    root->right->right = new TreeNode(18);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_fourth_root() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(3);
    root->right->right->right = new TreeNode(4);
    root->right->right->right->right = new TreeNode(5);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_fifth_root() {
    TreeNode* root = new TreeNode(100);
    root->left = new TreeNode(50);
    root->right = new TreeNode(150);
    root->left->left = new TreeNode(49);
    root->left->right = new TreeNode(51);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_sixth_root() {
    TreeNode* root = new TreeNode(100000);
    root->left = new TreeNode(1);
    root->right = new TreeNode(50000);
    return root;
}

// Helper function to build tree for testing
TreeNode* build_seventh_root() {
    TreeNode* root = new TreeNode(8);
    root->left = new TreeNode(3);
    root->right = new TreeNode(10);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(6);
    root->right->right = new TreeNode(14);
    return root;
}

int main() {
    GetMinimumDifference getMinimumDifference;

    assert(getMinimumDifference.dfs(build_first_root()) == 1);
    assert(getMinimumDifference.dfs(build_second_root()) == 1);
    assert(getMinimumDifference.dfs(build_third_root()) == 2);
    assert(getMinimumDifference.dfs(build_fourth_root()) == 1);
    assert(getMinimumDifference.dfs(build_fifth_root()) == 1);
    assert(getMinimumDifference.dfs(build_sixth_root()) == 50000);
    assert(getMinimumDifference.dfs(build_seventh_root()) == 2);

    return 0;
}
