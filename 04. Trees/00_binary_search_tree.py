import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return str(self.__dict__)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def display(self):
        def _show(node, prefix="", is_left=None):
            if node is None:
                return
            _show(node.right, prefix + ("    " if is_left else "│   "), False)
            print(prefix + ("└── " if is_left is not None else "") + str(node.value))
            _show(node.left, prefix + ("│   " if is_left is False else "    "), True)

        _show(self.root)

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        curr = self.root
        while True:
            if curr.value > value:
                if curr.left is None:
                    curr.left = new_node
                    return
                curr = curr.left
            elif curr.value < value:
                if curr.right is None:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                return

    def lookup(self, value):
        if not self.root:
            return False
        curr = self.root
        while curr:
            if curr.value > value:
                curr = curr.left
            elif curr.value < value:
                curr = curr.right
            elif curr.value == value:
                return True
        return False

    def remove(self, value):
        if self.root == None:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value == currentNode.value:
                # We have a match, get to work!

                # Option 1: No right child:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        # if parent < current value, make left child a right child of parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left

                # Option 2: Right child which doesnt have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        # //if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        # //if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right

                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                return True

    def traverse(self, node: Node):
        tree: Node = Node(node.value)
        tree.left = None if node.left is None else self.traverse(node.left)
        tree.right = None if node.right is None else self.traverse(node.right)
        return tree


my_bst = BinarySearchTree()
my_bst.insert(9)
my_bst.insert(4)
my_bst.insert(6)
my_bst.insert(20)
my_bst.insert(170)
my_bst.insert(15)
my_bst.insert(1)
my_bst.remove(4)

print(my_bst.lookup(170))
print(my_bst.display())
