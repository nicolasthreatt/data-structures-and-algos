"""
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

Constraints:
    * 1 <= n <= 19
"""


# Algorithm Used: Dynamic Programming, Top-Down, Fibonacci
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def numTrees(n: int) -> int:
    """Define numTree[n] as the number of unique BSTs for n nodes.

        numTree[4] = (
            numTree[0] * numTree[3] +
            numTree[1] * numTree[2] +
            numTree[2] * numTree[1] +
            numTree[3] * numTree[0]
        )

    The number of unique BSTs for n nodes is the sum of the number of unique BSTs for each root node.
    For example, if n = 4, then the number of unique BSTs is the sum of the number of unique BSTs for
    each root node (1, 2, 3, 4).

    Recall that a BST has the following properties:
        1. The left subtree of a node contains only nodes with keys less than the node's key.
        2. The right subtree of a node contains only nodes with keys greater than the node's key.
        3. Both the left and right subtrees must also be binary search trees.
    """

    # Initialize a list to store the number of unique BSTs for each number of nodes
    # NOTE: Base Cases
    #   - 0 nodes = 1 tree (null node)
    #   - 1 nodes = 1 tree
    numTree = [1] * (n + 1)  # n + 1 since 0 start index

    # Iterate through the number of nodes
    #   - Start at 2 since 0 and 1 nodes are already initialized (base case)
    for nodes in range(2, n):
        # Initialize a variable to store the total number of unique BSTs for the current number of nodes
        total = 0

        # Iterate through the number of nodes and consider each node as the root node
        for root in range(1, nodes + 1):
            # Left subtree contains nodes less than the root node
            # Example: If n = 4 and root = 2, then the left subtree contains nodes 1 and 2
            left = root - 1

            # Right subtree contains nodes greater than the root node
            # Example: If n = 4 and root = 2, then the right subtree contains nodes 3 and 4
            right = nodes - root

            # Find the number of unique BSTs for the left and right subtrees
            # NOTE: Multipllication since finding combinations
            total += numTree[left] * numTree[right]

        # Store the total number of unique BSTs for the current number of nodes
        # NOTE: This is the sum of the number of unique BSTs for each root node
        numTree[nodes] = total

    # Return the number of unique BSTs for n nodes
    # NOTE: n is the index of the number of nodes whi
    return numTree[n]
