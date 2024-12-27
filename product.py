#  File: product.py

#  Description: Determine if there exists at least one of two elements, x and y, 
#	in the list, the product of two elements, (x * y), is also a member of the list and False otherwise.

#  Student Name: 

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

# Input: lst is a list of integers
# Output: return True if there exists at least one of two elements, x and y, which product is also in the list
# return False otherwise
def is_product_in_list(lst):
	''''''	
	for i in range(len(lst)):
		current_index = i
		for j in range(i + 1, len(lst)):
			if lst[current_index] * lst[j] in lst:
				return True

	return False
    


def main():
	# read input
	lst = [int(x) for x in sys.stdin.readline().strip().split(" ")]

	# get result
	result = is_product_in_list(lst)

	# print the result to standard output
	print(result)


if __name__ == "__main__":
	main()
	
