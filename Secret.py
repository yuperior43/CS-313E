#  File: Secret.py

#  Description: Rotates a linked list to the right (clockwise) rot places times number of times

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

import sys

class Link (object):
    # do not change this constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list -- do not change this constructor
    def __init__(self):
        self.first = None

    # helper function to add an item at the end of a list
    # you can use this if you want, but do not delete it
    def insert_last (self, data):
        newLink = Link(data)
        current = self.first

        if current == None:
            self.first = newLink
            return

        while current.next != None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    # you can use this if you want, but do not delete it
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    # you can use this if you want, but do not delete it
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    # COMPLETE THIS FUNCTION
    # return a new linked list that results from the rotation
    # do not change this linked list
    def rotate(self, rot_amt, t):
        links = self.num_links()
        n = (rot_amt * t) % links
        res = self.copy_list()

        while n > 0:
            res.current = res.first.next
            res.previous = res.first

            while res.current.next:
                res.current = res.current.next
                res.previous = res.previous.next
            
            res.current.next = res.first
            res.first = res.current
            res.previous.next = None
            n -= 1
        return res

# DO NOT CHANGE MAIN
def main():
    ll = LinkedList()

    data = list(map(int, input().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    rot_amt, t = list(map(int, input().split()))

    rotated = ll.rotate(rot_amt, t)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)

if __name__ == "__main__":
    main()
