'''  File: josephus.py
  Description: Uses circular linked list to print out the order in which soldiers
  get eliminated, given the number of soliders, the soldier where the counting 
  starts, and the elimination number

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Partner Name: Henry Chen
  Partner UT EID: hhc462

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: October 11, 2023
  Date Last Modified: October 12, 2023'''

import sys

class Link():
    '''Creates a link with data and pointer attributes'''
    def __init__ (self, data, next_link = None):
        self.data = data
        self.next = next_link

    def print_data(self):
        ''' Print the data contained in this link.'''
        print(self.data)

    def __str__(self):
        return str(self.data)

class CircularList():
    '''Creates a circular linked list with first, last, and size attributes'''
    def __init__ (self):
        '''Constructor'''
        self.first = None
        self.size = 0
        self.last = None

    def insert (self, data):
        '''Adds a new node to linked list'''
        new_link = Link(data)

        if self.size == 0:
            self.first = new_link
            self.last = new_link
        else:
            self.last.next = new_link
            self.last = new_link

        self.last.next = self.first
        self.size += 1

    def find (self, data):
        '''Traverses the list and searches for a given data value'''
        current = self.first
        if current is None:
            return None

		# searching for the data
        while current.data != data:
            if current.next is None:
                return None
            current = current.next
        return current

    def delete (self, data):
        '''Removes a node from linked list or returns None if data is not there'''
        current = self.first
        previous = self.first
        # base case
        if current is None:
            return None
        # searching for data to be deleted
        while current.data != data:
            if current.next == self.first:
                return None
            previous = current
            current = current.next
        # setting pointers based on data location within linked list
        if current == self.last:
            self.last = previous
        if current == self.first:
            # handles deletion of list if only one element is present
            if self.size == 1:
                self.size -= 1
                self.first.next = None
                self.first = None
                self.last = None
            return current
        previous.next = current.next
        self.size -= 1

        return current

    def delete_after (self, start, num):
        '''Deletes the nth link starting from the link start,
        returns the data of the deleted link AND returns the 
        next link after the deleted link in that order'''
        prev = None
        start = self.find(start)

		# iterating through list for num times and deleting soldiers
        for _ in range(num-1):
            prev = start
            start = start.next
        if start == self.last:
            self.last.next = self.first
        elif start == self.first:
            self.first = self.first.next
        prev.next = start.next
        self.size -= 1

        return (start.data, start.next.data)

    def __str__ (self):
        '''Returns a string interpretation of circular list object;
        it will look like a normal Python list'''
        # returns empty list if no data is in linked list
        if self.size == 0:
            return '[]'
        current = self.first.next
        count = 0
        string = '[' + str(self.first)

		# iterate through linked list
        while count < self.size - 1:
            string += ', '
            string += str(current)
            current = current.next
            count += 1

        return string + ']'

def main():
    '''This is the main function'''
	# read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)

	# read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

	# read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

	# create linked list with num_soldiers
    my_list = CircularList()
    for i in range(1, num_soldiers + 1):
        my_list.insert(i)
    print('Current soldiers:', my_list)
    print()

	# deleting soldiers until one remains
    while my_list.first.next != my_list.first:
        soldier, next_soldier = my_list.delete_after(start_count, elim_num)
        print('Executed soldier', soldier)
        print('Remaining soldiers:', my_list)
        print()
        start_count = next_soldier
    # print surviving soldier
    print('Surviving soldier:', my_list.first.data)

if __name__ == "__main__":
    main()
