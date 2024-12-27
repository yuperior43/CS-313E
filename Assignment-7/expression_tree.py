'''File: expression_tree.py
  Description: Takes an expression and breaks it into tokens, 
  creating an expression tree. Evaluate the expression and print
  the result, writing the prefix and postfix versions of the same
  expression without any parentheses.

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: October 12, 2023
  Date Last Modified: October 15, 2023'''

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack ():
    '''Creates a stack with push and pop methods and checks if it's
    empty'''
    def __init__(self):
        self.stack = []

    def push(self, data):
        '''Pushes an item onto the stack'''
        self.stack.append (data)

    def pop(self):
        '''Pops an item from the stack'''
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        '''Check if the stack is empty'''
        return len(self.stack) == 0

class Node ():
    '''Creates a node on expression tree with data, l_child, and r_child
    attributes'''
    def __init__ (self, data = None, l_child = None, r_child = None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child

    # simple getter methods
    @property
    def get_data(self):
        '''Return node's data'''
        return self.data

    @property
    def get_l_child(self):
        '''Return node's left child'''
        return self.l_child

    @property
    def get_r_child(self):
        '''Return node's right child'''
        return self.r_child

class Tree():
    '''Creates an expression tree with evaluate, preorder traversal, 
    and postorder traversal methods'''
    def __init__ (self):
        self.root = None

    def create_tree (self, expr):
        '''This function takes in the input string expr and
        creates the expression tree'''
        tokens = expr.split()
        current = self.root = Node()
        my_stack = Stack()

        # uses algorithm given to iterate through expression and
        # create expression tree
        for token in tokens:
            if token == '(':
                current.l_child = Node()
                my_stack.push(current)
                current = current.l_child
            elif token in operators:
                current.data = token
                my_stack.push(current)
                current.r_child = Node()
                current = current.r_child
            elif token == ')':
                if not my_stack.is_empty():
                    current = my_stack.pop()
            else:
                current.data = token
                current = my_stack.pop()

    def evaluate (self, a_node):
        '''This function should evaluate the tree's expression
        returns the value of the expression after being calculated'''
        # store operators and operands
        if a_node.data not in operators:
            return float(a_node.data)
        left_child = self.evaluate(a_node.l_child)
        right_child = self.evaluate(a_node.r_child)
        operator = a_node.data

        # performs operations as appropriate and raises necessary errors
        if operator == '+':
            result = left_child + right_child
        elif operator == '-':
            result = left_child - right_child
        elif operator == '*':
            result = left_child * right_child
        elif operator == '/':
            if right_child == 0:
                raise ZeroDivisionError
            result = left_child / right_child
        elif operator == '//':
            if right_child == 0:
                raise ZeroDivisionError
            result = left_child // right_child
        elif operator == '%':
            if right_child == 0:
                raise ZeroDivisionError
            result = left_child % right_child
        elif operator == '**':
            result = left_child ** right_child

        return result

    def pre_order (self, a_node):
        '''This function should generate the preorder notation of
        the tree's expression returns a string of the expression 
        written in preorder notation'''
        preorder_notation = ''

        # add node data to string based on preorder traversal
        if a_node is not None:
            preorder_notation += f'{a_node.data}' + ' '
            preorder_notation += self.pre_order(a_node.l_child) + ' '
            preorder_notation += self.pre_order(a_node.r_child) + ' '

        return preorder_notation.strip()

    def post_order (self, a_node):
        '''This function should generate the postorder notation of
        the tree's expression returns a string of the expression 
        written in postorder notation'''
        postorder_notation = ''

        # add node data to string based on postorder traversal
        if a_node is not None:
            postorder_notation += self.post_order(a_node.l_child) + ' '
            postorder_notation += self.post_order(a_node.r_child) + ' '
            postorder_notation += f'{a_node.data}' + ' '

        return postorder_notation.strip()

def main():
    '''This is the main function'''
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
