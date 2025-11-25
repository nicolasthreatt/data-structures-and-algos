#include <unordered_set>

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

class BinaryTreeTraversal {
private:
    unordered_set<int> visit;
    
    // Algorithm(s) Used: Depth First Search (DFS), In Order Traversal (Left -> Root -> Right)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    void inOrderTraversal(TreeNode* node) {
        if (node != nullptr) {
            inOrderTraversal(node->left);
            visit.insert(node->val);
            inOrderTraversal(node->right);
        }
    }
    
    // Algorithm(s) Used: Depth First Search (DFS), Pre Order Traversal (Root -> Left -> Right)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    void preOrderTraversal(TreeNode* node) {
        if (node != nullptr) {
            visit.insert(node->val);
            preOrderTraversal(node->left);
            preOrderTraversal(node->right);
        }
    }

    // Algorithm(s) Used: Depth First Search (DFS), Post Order Traversal (Left -> Right -> Root)
    // Space Complexity: O(n), where n is the number of nodes in the tree
    // Time Complexity: O(n), where n is the number of nodes in the tree
    void postOrderTraversal(TreeNode *node) {
        if (node != nullptr) {
            postOrderTraversal(node->left);
            postOrderTraversal(node->right);
            visit.insert(node->val);
        }
    }

public:
    void run(TreeNode* root) {
        inOrderTraversal(root); // Left -> Root -> Right
        preOrderTraversal(root); // Root -> Left -> Right
        postOrderTraversal(root); // Left -> Right -> Root
    }
};
