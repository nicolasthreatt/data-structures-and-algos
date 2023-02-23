"""
3 Types of Traversals
    - In-Order:
        + Prints nodes in ascending numerical order (left-root-right)
        + Use Cases:
            > If you know that a tree has an inherent sequence in the nodes and you
              want to flatten the tree back into its original sequence, then an in-order
              traversal should be used
            > For example, used to get the values of the nodes in non-decreasing order in
              a binary search tree
    - Pre-Order
        + Follows a left-first path, so it is common to see nodes initially
          printed in descending order, before being forced to go to the right. (root-left-right)
        + Use Cases"
            > If you know you need to explore the roots before inspecting any leaves
            > Pre-order is used to create a copy of a tree
    - Post-Order
        + Will print leaf nodes first starting on the left (left-right-root)
        + Use Cases:
            > If you know you need to visit all the leaves before visiting any nodes, use
              post-order traversal so you won't waste time insepcting roots in search for leaves
            > Post-order traversal is used to delete leaf nodes from a tree, for examle

max number of nodes = 2^(h+1)-1
min number of nodes = h+1
"""

import argparse
from binarySearchTree import Tree, Node


def createTree():
    # Create Tree with Root Node
    tree = Tree(Node(50), 'Traverse Tree')

    # Assign left and right pointers of tree
    tree.root.left = Node(25)              # Node  must be less than 50
    tree.root.right = Node(75)             # Node value must be greater than 50
    tree.root.left.left = Node(10)         # Node value must be less than 25
    tree.root.left.right = Node(35)        # Node value must be beween 25 and 75
    tree.root.left.right.left = Node(30)   # Node value must between 25 and 35
    tree.root.left.right.right = Node(42)  # Node value must between 35 and 75
    tree.root.left.left.left = Node(5)     # Node value must be less than 10
    tree.root.left.left.right = Node(13)   # Node value must be between 10 and 35
    tree.add(23)
    print()
    tree.print()

    return tree

def preOrderTraverse(tree: Tree) -> None:
    print("\nTraverse Pre-Order:")
    tree.traversePreorder()


def inOrderTraverse(tree: Tree) -> None:
    print("\nTraverse In-Order:")
    tree.traverseInorder()


def postOrderTraverse(tree: Tree) -> None:
    print("\nTraverse Post-Order:")
    tree.traversePostorder()


def parseArgs():
    parser = argparse.ArgumentParser(description='Traversing Trees')

    parser.add_argument('--pre_order', action='store_true', help="Pre-Order Traversal")
    parser.add_argument('--in_order', action='store_true', help='In Order Traversal')
    parser.add_argument('--post_order', action='store_true', help="Post Order Traversal")

    return parser.parse_args()


if __name__ == "__main__":
    args = parseArgs()

    tree = createTree()

    if args.pre_order:
        preOrderTraverse(tree)

    if args.in_order:
        inOrderTraverse(tree)

    if args.post_order:
        postOrderTraverse(tree)
