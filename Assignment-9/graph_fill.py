'''File: graph_fill.py
  Description: Uses BFS and DFS to flood fill a graph; prints the adjacency matrix of the graph.

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: October 16, 2023
  Date Last Modified: October 24, 2023'''

import os
import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

def colored(text, color):
    '''Returns the string wrapped with the color code given a string we
    want to write in a specific color. Color is the name of a color 
    that is looked up in COLOR_DICT'''
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise KeyError(color + " is not a valid color!")
    return COLOR_DICT[color] + text

def print_block(color):
    '''Prints a block (two characters) in the specified color given the color name.'''
    print(colored(BLOCK_CHAR, color)*2, end='')

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


class Stack():
    '''A simple Stack class; used to implement search algorithms'''

    def __init__(self):
        self.stack = []

    def push(self, item):
        '''Add an item to the top of the stack'''
        self.stack.append(item)

    def pop(self):
        '''Remove an item from the top of the stack'''
        return self.stack.pop()

    def peek(self):
        '''Check the item on the top of the stack'''
        return self.stack[-1]

    def is_empty(self):
        '''Check if the stacck is empty'''
        return len(self.stack) == 0

    def size(self):
        '''Return the number of elements in the stack'''
        return len(self.stack)

class Queue():
    '''Queue class; you can use this for your search algorithms.'''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        '''Add an item to the end of the queue'''
        self.queue.append(item)

    def dequeue(self):
        '''Remove an item from the beginning of the queue'''
        return self.queue.pop(0)

    def peek(self):
        '''Checks the item at the top of the queue'''
        return self.queue[0]

    def is_empty(self):
        '''Check if the queue is empty'''
        return len(self.queue) == 0

    def size(self):
        '''Return the size of the queue'''
        return len(self.queue)

class ColorNode:
    '''Class for a graph node; contains x and y coordinates, a color, a list of edges, and a
    flag signaling if the node has been visited (useful for search algorithms). It also contains
    a "previous color" attribute. This might be useful for the flood fill implementation.'''

    def __init__(self, index, x, y, color):
        '''Input: x, y are the location of this pixel in the image; color is the name of a color'''
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    def add_edge(self, node_index):
        '''Adds an edge and sorts the list of edges given an index of the node we want to create
        an edge to in the node list.'''
        self.edges.append(node_index)

    def visit_and_set_color(self, color):
        '''This function visits a node and gives it a new color; it also saves the previous
        color.'''
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))

class ImageGraph:
    '''Class that contains the graph.'''

    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size

    def print_image(self):
        '''Prints the image formed by the nodes on the command line.'''
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):
        '''Sets the visited flag to False for all nodes.'''
        for _, node in enumerate(self.nodes):
            node.visited = False

    def print_adjacency_matrix(self):
        '''Prints adjacency matrix of the graph'''
        print("Adjacency matrix:")
        matrix = [[1 if i in node.edges else 0 for i in range(len(self.nodes))]
                  for node in self.nodes]
        for row in matrix:
            print(*row, sep = '')
        # empty line afterwards
        print()

    def bfs(self, start_index, color):
        '''Utilizes a breadth-first search to fill a graph, given a color to 
        fill the area containing the current node with and a start_index, the index
        of the currently visited node. It also prints the progression of the graph
        flood fill.'''

        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        start_node = self.nodes[start_index]
        my_queue = Queue()
        my_queue.enqueue(start_node)

        original_color = start_node.color
        while my_queue.is_empty() is False:
            node = my_queue.dequeue()
            if not node.visited:
                node.visit_and_set_color(color)
                self.print_image()
            for index in node.edges:
                u = self.nodes[index]
                if not u.visited and u.color == original_color:
                    my_queue.enqueue(u)

    def dfs(self, start_index, color):
        '''Utilizes a depth-first search to fill a graph, given a color to 
        fill the area containing the current node with and a start_index, the index
        of the currently visited node. It also prints the progression of the graph
        flood fill.'''

        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        start_node = self.nodes[start_index]
        original_color = start_node.color
        self._dfs(start_node, color, original_color)

    def _dfs(self, start_node, color, original_color):
        '''Helper function for depth-first search, using recursion to visit unfilled
        nodes.'''
        start_node.visit_and_set_color(color)
        self.print_image()
        for index in start_node.edges:
            u = self.nodes[index]
            if not u.visited and u.color == original_color:
                self._dfs(u, color, original_color)

def create_graph(data):
    '''Creates graph from read in data.'''

    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for _ in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for _ in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color


def main():
    '''This is the main function.'''

    # read input
    data = sys.stdin.read()

    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
