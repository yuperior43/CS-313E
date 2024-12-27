#  File: LCA.py

#  Description: Determines the lowest common ancestor of two nodes in a binary tree

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

class Node (object):
  def __init__ (self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def lca(root, val1, val2):
    p1 = find_path(root, val1)
    p2 = find_path(root, val2)

    p1idx = len(p1) - 1
    p2idx = len(p2) - 1
    while p1idx >= 0 and p2idx >= 0:
        if p1[p1idx] != p2[p2idx]:
            return p1[p1idx + 1].data
        p1idx -= 1
        p2idx -= 1

    if p1idx < 0 and p2idx >= 0:
        return p1[0].data
    elif p2idx < 0 and p1idx >= 0:
        return p2[0].data
    elif p1idx < 0 and p2idx < 0:
        return p1[0].data

def find_path(root, val):
    if root == None:
        return None

    if root.data == val:
        return []
    else:
        lpath = find_path(root.left, val)
        rpath = find_path(root.right, val)

        correct_path = lpath if lpath is not None else rpath
        return correct_path + [root] if correct_path is not None else None

# ------ DO NOT CHANGE BELOW HERE ------ #
import pickle
import sys

def main():
    val1 = int(input())
    val2 = int(input())

    data_in = ''.join(sys.stdin.readlines())
    root = pickle.loads(str.encode(data_in))

    print(lca(root, val1, val2))

if __name__ == "__main__":
    main()
