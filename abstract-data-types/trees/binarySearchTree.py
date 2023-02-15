"""
What Are Trees?
    - One roote node
    - Each node has any number of children
    - Each node (except root) has one parent
        + A node cannot be its own paren

Optional Tree Featrue
    - Nodes are associated with some data
    - Rules about how many children a node can have
    - Rules about how nodes are connected based on their data

Binary Search Tree
    - Each node has, at most, two children:
        + Left
        + Right
    - Each node has a numeric value associated with it
    - Children to the left must have lesser values than their parents
    - Children to the right must have greater values than their parents
    - No duplicate values
"""

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def traversePreorder(self) -> None:
        print(self.data)

        if self.left:
            self.left.traversePreorder()
        
        if self.right:
            self.right.traversePreorder()

    # Prints nodes from smallest to largest
    def traverseInorder(self) -> None:
        if self.left:
            self.left.traverseInorder()

        print(self.data)
        
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self) -> None:
        if self.left:
            self.left.traversePostorder()
        
        if self.right:
            self.right.traversePostorder()

        print(self.data)

    def search(self, target):
        if self.data == target:
            print("Found it.")
            return self

        if self.left and target < self.data:
            return self.left.search(target)
        
        if self.right and target > self.data:
            return self.right.search(target)

        print("Value not in tree")
    
    def add(self, data) -> None:
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:    
                self.left.add(data)
                self.left = self.left.fixImbalanceIfExists()
        
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
                self.right = self.right.fixImbalanceIfExists()

    def delete(self, target):

        if self.data == target:
            if self.left and self.right:
                #RTFM = Right Tree Find Minimum
                minValue = self.right.findMin()
                self.data = minValue()
                self.right = self.right.delete(minValue)

                return self
            else: 
                # If the target is found and the parent node is missing only
                # one child node, then return the other child one
                return self.left or self.right
        
        if self.right and target > self.data:
            self.right = self.right.delete(target)

        if self.left and target < self.data:
            self.left = self.left.delete(target)

        return self.fixImbalanceIfExists()

    def findMin(self):
        if self.left:
            return self.left.left.findMin()
        return self.data

    def findMax(self):
        if self.right:
            return self.right.right.findMax()
        return self.data

    def isBalance(self) -> bool:
        leftHeight = self.left.height() + 1 if self.left else 0
        rightHeight = self.right.height() + 1 if self.right else 0

        return abs(leftHeight - rightHeight) < 2

    def getNodesAtDepth(self, depth, nodes=[]) -> list:
        # If depth is 0, then we are at the root of the tree
        if depth == 0:
            nodes.append(self.data)
            return nodes
        
        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:  # Add value to node list even if the node doesn't exist
            nodes.extend([None]*2**(depth -1))
    
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:  # Add value to node list even if the node doesn't exist
            nodes.extend([None]*2**(depth -1))  

        return nodes
    
    def height(self, h=0) -> int:
        # height = 1 + Floor(log base 2(number of nodes))
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h

        return max(leftHeight, rightHeight)

    def isBalance(self) -> bool:
        leftHeight = self.left.height()+1 if self.left else 0
        rightHeight = self.right.height()+1 if self.right else 0

        return abs(leftHeight - rightHeight) < 2

    def getLeftRightHeightDifference(self):
        leftHeight = self.left.height()+1 if self.left else 0
        rightHeight = self.right.height()+1 if self.right else 0

        return leftHeight - rightHeight

    def fixImbalanceIfExists(self):

        # left imbalance
        if self.getLeftRightHeightDifference() > 1:
            #left-left imbalance
            if self.left.getLeftRightHeightDifference() > 0:
                return rotateRight(self)
            #left-right imbalance
            else:
                self.left = rotateLeft(self.left)
                return rotateRight(self)
        
        # right imbalance
        if self.getLeftRightHeightDifference() < -1:
            # right-right imbalance
            if self.right.getLeftRightHeightDifference() < 0:
                return rotateLeft(self)
            # right-left imbalance
            else:
                self.right = rotateRight(self.right)
                return rotateLeft(self)

        return self

    def rebalance(self) -> None:
        if self.left:
            self.left.rebalance()
            self.left = self.left.fixImbalanceIfExists()
        if self.right:
            self.right.rebalance()
            self.right = self.right.fixImbalanceIfExists()


class Tree:
    def __init__(self, root, name='') -> None:
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' ' * spacing)
        spacing = spacing - len(str(n)) + 1
        
        return str(n) + (' ' * spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def traversePreorder(self) -> None:
        self.root.traversePreorder()

    def traverseInorder(self) -> None:
        self.root.traverseInorder()

    def traversePostorder(self) -> None:
        self.root.traversePostorder()

    def getNodesAtDepth(self, depth) -> list:
        return self.root.getNodesAtDepth(depth)

    def search(self, target):
        return self.root.search(target)

    def height(self) -> int:
        return self.root.height()

    def add(self, data) -> None:
        self.root.add(data)
        self.root = self.root.fixImbalanceIfExists()

    def delete(self, target):
        self.root = self.root.delete(target)

    def isBalance(self) -> bool:
        return self.root.isBalance()

    def rebalance(self) -> None:
        self.root.rebalance()
        self.root = self.root.fixImbalanceIfExists()


def rotateRight(root) -> Node:
    pivot = root.left
    reattachNode = pivot.right
    root.left = reattachNode
    pivot.right = root

    return pivot


def rotateLeft(root) -> Node:
    pivot = root.right
    reattachNode = pivot.left
    root.right = reattachNode
    pivot.left = root

    return pivot
