"""
Depth-First Search (DFS) is an algorithm for traversing or searching a tree or graph. 
It explores as far as possible along each branch before backtracking. 
In a tree, DFS starts from the root node and explores each branch completely before moving to the next branch.
DFS can be implemented using recursion or an explicit stack.
DFS is often used when searching for a specific node or finding a path between two nodes.
"""

# Algorithm: DFS Tree Traversal, Preorder
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(n), where n is the number of nodes
def dfs_tree(root):
    # Initialize an empty list to store the traversal order
    traversal_order = []

    # Recursive helper function for DFS traversal
    def dfs_helper(node):
        # Base case
        if node is None:
            return

        # Process the current node
        traversal_order.append(node.value)

        # Recursively traverse the left subtree
        dfs_helper(node.left)

        # Recursively traverse the right subtree
        dfs_helper(node.right)

    # Call the helper function to perform DFS traversal
    dfs_helper(root)

    # Return the traversal order
    return traversal_order
