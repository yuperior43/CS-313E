'''  File: work.py
  Description: Uses linear search and binary search to determine the minimum lines 
  of code to write

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Partner Name: Henry Chen
  Partner UT EID: hhc462

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: October 3, 2023
  Date Last Modified: October 3, 2023'''

import sys
import time

def sum_series (v_1, k_1):
    '''Computes the number of lines of code written based on productivity factor'''
    coffee_p = 1
    num_lines = v_1
    while v_1//k_1**coffee_p != 0:
        num_lines += v_1//k_1**coffee_p
        coffee_p += 1
    return num_lines

def linear_search (n_1, k_1):
    '''Returns v the minimum lines of code to write using linear search'''
    v_1 = 1
    while True:
        if sum_series(v_1, k_1) >= n_1:
            return v_1
        v_1 += 1

def binary_search (n_1, k_1):
    '''Returns v the minimum lines of code to write using binary search'''
    low = 1
    high = n_1
    while low < high:
        mid = (low + high) // 2
        total_lines = sum_series(mid, k_1)
        if total_lines >= n_1:
            high = mid
        else:
            low = mid + 1
    return low



def main():
    '''This is the main function'''
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for _ in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n_1 = int(inp[0])
        k_1 = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n_1, k_1)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n_1, k_1)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
