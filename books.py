#  File: books.py
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:

import sys

max_val = 1000

def findbooks(prices, T):

	N = int(0.1 * T)
	table = [[0 for i in range(N + 1)] for i in range(len(prices) + 1)]
	# print(table)
	for i in range(1, N + 1):
		table[0][i] = max_val

	for i in range(1, len(prices) + 1):
		for j in range(1, N + 1):
			if prices[i - 1] > j:
				table[i][j] = table[i-1][j]

			else:
				table[i][j] = min(table[i-1][j], table[i][j-prices[i-1]]+1)
	if table[i][j] == max_val:
		return -1
	return table[len(prices)][N]



if __name__ == "__main__":

	# Read input list of prices for each book
	prices_str = sys.stdin.readline().split()
	prices = [ int(x) for x in prices_str ]

	# Read total price that the customer spends
	T = int(sys.stdin.readline())

	print(findbooks(prices, T))
