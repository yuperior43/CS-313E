'''File: test_binary_tree.py
  Description: Writes helper methods for the Tree class we developed and test them.
  These methods include range() that returns the range of values stored in a binary
  search tree; get_level() that takes as input the level and returns all of the nodes
  at that level; left_side_view() which given the root of a binary tree, returns the
  values you can see ordered from top to bottom; and sum_leaf_node that returns the
  value of all leaves.

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: October 16, 2023
  Date Last Modified: October 24, 2023'''

import sys

class Node():
    '''Creates a node with data, lchild, and rchild attributes'''
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        '''Printing node if it exists'''
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        '''Returning the depth of the node'''
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1

    def bst_size(self, node):
        '''Helper function - return the number of nodes in bst'''
        if node is None:
            return 0
        return self.bst_size(node.lchild) + 1 + self.bst_size(node.rchild)

class Tree():
    '''Creates a binary search tree with root attribute'''
    def __init__(self):
        self.root = None

    def print(self, level):
        '''Prints the binary search tree'''
        self.root.print_node(level)

    def get_height(self):
        '''Returns the height of the tree'''
        return self.root.get_height()

    def insert(self, data):
        '''Inserts data into the Binary Search Tree and creates a valid BST'''
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        parent = self.root
        curr = self.root
        # finds location to insert new node
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        # inserts new node based on comparision to parent node
        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        return

    def minimum(self):
        '''Helper function - find the node with the smallest value'''
        current = self.root
        parent = current
        while current is not None:
            parent = current
            current = current.lchild
        return parent

    def maximum(self):
        '''Helper function - find the node with the largest value'''
        current = self.root
        parent = current
        while current is not None:
            parent = current
            current = current.rchild
        return parent

    def range(self):
        '''Returns the range of values stored in a binary search tree of integers. The range of
        values equals the maximum value in the binary search tree minus the minimum value. If 
        there is one value in the tree the range is 0. If the tree is empty the range in 
        undefined.'''
        # base cases
        if self.root.bst_size(self.root) == 1:
            return 0
        if self.root.bst_size(self.root) == 0:
            return 'Undefined'

        # calculating range of bst
        maximum = self.maximum()
        minimum = self.minimum()
        return maximum.data - minimum.data

    def get_level(self, level):
        '''Takes the level as input and returns a list of all the nodes at that level from left to 
        right. If that level does not exist return an empty list.'''
        return self._get_level(level, self.root)

    def _get_level(self, level, root):
        '''Helper function - gathers nodes within a given level'''
        # empty tree
        result = []
        if root is None:
            return []
        if level==0:
            return [root]
        if root.lchild is not None:
            result += self._get_level(level - 1, root.lchild)
        if root.rchild is not None:
            result += self._get_level(level - 1, root.rchild)
        return result

    def left_side_view(self):
        '''When given the root of a tree, imagine yourself standing on the left side of it, 
        returns the values of the nodes you can see ordered top to bottom'''
        level = 0
        lst = self.get_level(level)
        left_side = []
        # getting number of levels and creating list of viewable nodes
        while lst:
            left_side.append(lst[0].data)
            level += 1
            lst = self.get_level(level)
        return left_side

    def sum_leaf_nodes(self):
        '''Returns the sum of the value of all leaves. A leaf node does not have any children'''
        return self._sum_leaf_nodes(self.root)

    def _sum_leaf_nodes(self, root):
        '''Helper function - handles summing of leaf nodes'''
        # base case
        if root is None:
            return 0
        # leaf node case
        if root.lchild is None and root.rchild is None:
            return root.data
        # go to next nodes
        return self._sum_leaf_nodes(root.lchild) + self._sum_leaf_nodes(root.rchild)

def make_tree(data):
    '''Creates a binary search tree with a given input'''
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    '''This is the main function'''
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is:", t1.range())
    print("Tree left side view is:", t1.left_side_view())
    print("Sum of leaf nodes is:", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is:", t2.range())
    print("Tree left side view is:", t2.left_side_view())
    print("Sum of leaf nodes is:", t2.sum_leaf_nodes())
    print("##########################")

# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is:", t3.range())
    print("Tree left side view is:", t3.left_side_view())
    print("Sum of leaf nodes is:", t3.sum_leaf_nodes())
    print("##########################")

if __name__ == "__main__":
    main()
