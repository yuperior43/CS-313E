#  File: marbles.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

'''
A row of magic marbles can magically move to the right or left based on their magic.
We use an array of nonzero integers to represent the magic strength of each marble.
A magic marble can move to the right if its magic strength is positive and left otherwise.
The power of each marble is computed by squared its magic strength.
Assuming that each marble moves at the same speed, some marble will meet.
If two marbles meet, the one with less power disappears.
If both marbles have the same power, both marbles disappear.
Return the array after all such meetings have occurred.
Two marbles moving in the same direction will not meet.
'''

import sys

# Input:  marbles is a list of nonzero integers
# Output: return a list representing marbles after all meetings have occurred


def get_marble_list(marbles):
    num_marbles = len(marbles)
    i = 0
    while i < num_marbles - 1:
        if (marbles[i] > 0 and marbles[i + 1] < 0):
            if marbles[i] ** 2 > marbles[i + 1] ** 2:
                marbles.remove(marbles[i + 1])
                num_marbles -= 1
                i = 0
                print(marbles)
            elif marbles[i] ** 2 == marbles[i + 1] ** 2:
                marbles.remove(marbles[i + 1])
                marbles.remove(marbles[i])
                num_marbles -= 2
                i = 0
                print(marbles)
            else:
                marbles.remove(marbles[i])
                num_marbles -= 1
                i = 0
                print(marbles)
        else:
            i += 1

    return marbles

def main():
	#marbles = [int(r) for r in sys.stdin.readline().strip().split(" ")]
	marbles = [int(r) for r in input().split()]
	result = get_marble_list(marbles)
	print(result)

if __name__ == "__main__":
	main()
