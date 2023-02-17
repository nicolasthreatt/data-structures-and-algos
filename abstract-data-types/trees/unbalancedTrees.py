"""
4 Types of Imbalances
    - left-left   (right rotation)
    - left-right  (left rotaion on left node then right rotation on new root)
    - right-left  (right rotation of right node then left rotation on new root)
    - right-right (left roation)
"""
import argparse
from binarySearchTree import Tree, Node, rotateRight, rotateLeft


def unbalanceLeftLeft():
    unbalancedLeftLeft = Tree(Node(30), 'UNBALANCED LEFT LEFT')
    unbalancedLeftLeft.root.left = Node(20)
    unbalancedLeftLeft.root.left.right = Node(21)
    unbalancedLeftLeft.root.left.left = Node(10)
    unbalancedLeftLeft.root.left.left.left = Node(9)
    unbalancedLeftLeft.root.left.left.right = Node(11)
    unbalancedLeftLeft.print()

    unbalancedLeftLeft.root = rotateRight(unbalancedLeftLeft.root)
    unbalancedLeftLeft.name = 'REBALANCED LEFT LEFT'
    unbalancedLeftLeft.print()


def unbalanceRightRight():
    unbalancedRightRight = Tree(Node(10), 'UNBALANCED RIGHT RIGHT')
    unbalancedRightRight.root.right = Node(20)
    unbalancedRightRight.root.right.left = Node(19)
    unbalancedRightRight.root.right.right = Node(30)
    unbalancedRightRight.root.right.right.left = Node(29)
    unbalancedRightRight.root.right.right.right = Node(31)
    unbalancedRightRight.print()

    unbalancedRightRight.root = rotateLeft(unbalancedRightRight.root)
    unbalancedRightRight.name = 'REBALANCED RIGHT RIGHT'
    unbalancedRightRight.print()


def unbalanceLeftRight():
    unbalancedLeftRight = Tree(Node(30), 'UNBALANCED LEFT RIGHT')
    unbalancedLeftRight.root.right = Node(31)
    unbalancedLeftRight.root.left = Node(10)
    unbalancedLeftRight.root.left.right = Node(20)
    unbalancedLeftRight.root.left.left = Node(9)
    unbalancedLeftRight.root.left.right.left = Node(19)
    unbalancedLeftRight.root.left.right.right = Node(21)
    unbalancedLeftRight.print()

    unbalancedLeftRight.root.left = rotateLeft(unbalancedLeftRight.root.left)
    unbalancedLeftRight.root = rotateRight(unbalancedLeftRight.root)
    unbalancedLeftRight.name = 'REBALANCED LEFT RIGHT'
    unbalancedLeftRight.print()


def unbalanceRightLeft():
    unbalancedRightLeft = Tree(Node(30), 'UNBALANCED RIGHT LEFT')
    unbalancedRightLeft.root.left = Node(31)
    unbalancedRightLeft.root.right = Node(10)
    unbalancedRightLeft.root.right.left = Node(20)
    unbalancedRightLeft.root.right.right = Node(9)
    unbalancedRightLeft.root.right.left.right = Node(19)
    unbalancedRightLeft.root.right.left.left = Node(21)
    unbalancedRightLeft.print()

    unbalancedRightLeft.root.right = rotateRight(unbalancedRightLeft.root.right)
    unbalancedRightLeft.root = rotateLeft(unbalancedRightLeft.root)
    unbalancedRightLeft.name = 'REBALANCED RIGHT LEFT'
    unbalancedRightLeft.print()


def parseArgs():
    parser = argparse.ArgumentParser(description='Rebalancing Unbalanced Trees')

    parser.add_argument('--ll', action="store_true", help='Rebalance Unbalanced Left Left Tree')
    parser.add_argument('--rr', action="store_true", help='Rebalance Unbalanced Right Right Tree')
    parser.add_argument('--lr', action="store_true", help='Rebalance Unbalanced Left Right Tree')
    parser.add_argument('--rl', action="store_true", help='Rebalance Unbalanced Right Left Tree')

    return parser.parse_args()


if __name__ == "__main__":
    args = parseArgs()

    if args.ll:
        print()
        unbalanceLeftLeft()
    
    if args.rr:
        print()
        unbalanceRightRight()

    if args.lr:
        print()
        unbalanceLeftRight()

    if args.rl:
        print()
        unbalanceRightLeft()
