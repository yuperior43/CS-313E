#  File: giftcard.py

#  Description: The gift card is worth the amount of N dollars.
#				Mark has to use it all at once without any exchange possible.
#				He wants to maximize the value of the gift card by ordering many different types of dessert
#				in the cafe without duplicates. Most importantly, he wants to spend exactly the amount on the
#				gift card. Is this possible? What are the maximum different deserts he can order?

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:

import sys
import copy


# Input: desert_list is a list which contents price of each desert (non-zero integers)
#		 N is the amount of the gift card
# Output: 6
#		  Return -1 if he can't find a way to order deserts in this way.
def max_giftcard_value(desert_list, total):
	sumsList = summationList(desert_list, total)
	if len(sumsList) == 0:
		return -1
	max_value = 0
	for lst in sumsList:
		if len(lst) > max_value:
			max_value = len(lst)

	return max_value

def summationList(desert_list, total, p=[], sumsList=[]):
	x = copy.deepcopy(p)
	x.sort()
	if total == 0 and x not in sumsList:
		print("adding")
		sumsList.append(x)
	elif total > 0 and len(desert_list) > 0:
		for i in range(len(desert_list)):
			if desert_list[i] <= total:
				r_deserts = desert_list[0:i] + desert_list[i+1:]
				"""print("Total = ", total)
				print("Original: ", desert_list)
				print("Removed ", desert_list[i], ", New: ", r_deserts)"""
				summationList(r_deserts, total - desert_list[i], p + [desert_list[i]], sumsList)

	return sumsList


if __name__ == '__main__':

	desert_list_str = sys.stdin.readline().split()
	desert_list = [ int(x) for x in desert_list_str ]
	N = int(sys.stdin.readline())
	result = max_giftcard_value(desert_list, N)

	print(result)

	#2 3 4 7 2 3 4 5 6 3 7 5 10 12 3 4
