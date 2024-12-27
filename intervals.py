"""
  File: intervals.py
  Description: Takes an unsorted list of tuples denoting intervals
  and outputs a list of merged tuples sorted by the lower number of
  the interval

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Partner Name: Henry Chen
  Partner UT EID: hhc462

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: September 2, 2023
  Date Last Modified: September 6, 2023
"""
import sys

def merge_tuples (tuples_list):
    '''Merge the tuples'''
    tuples_list.sort()
    merged_tuples_list = []
    #index 0 serves as a reference tuple for upcoming loop
    ref_interval = tuples_list[0]

    #iterates from index 1 to last index
    for interval in tuples_list[1:]:
        if interval[0] <= ref_interval[1]:
            #new interval with ref_interval[0] and whatever is larger at index 1
            ref_interval = (ref_interval[0], max(ref_interval[1], interval[1]))
        else:
            #interval cannot be merged
            merged_tuples_list.append(ref_interval)
            #creates a new reference interval
            ref_interval = interval

    #adds all ref_intervals to list
    merged_tuples_list.append(ref_interval)

    return merged_tuples_list

def range_of_tuples (tuples_list):
    '''Outputs each number within tuple range'''
    array_tuples = []
    for tup in tuples_list:
        #converts each tuple into list
        tup_list = list(tup)
        count = tup[0] + 1
        #while count != last number in tuple
        while count < tup[1]:
            #append numbers between 1st and last number
            tup_list.append(count)
            count += 1
        #sorts numbers in each interval and adds to 2d list
        tup_list.sort()
        array_tuples.append(tup_list)

    return array_tuples

def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """
    new_tuples_list = []
    #returns each number within each merged tuple
    range_tuples = range_of_tuples(merge_tuples(tuples_list))

    #selection sorting method
    for i in range(len(range_tuples)):
        small_int = i
        for j in range(i + 1, len(range_tuples)):
            if len(range_tuples[small_int]) > len(range_tuples[j]):
                small_int = j
        range_tuples[i], range_tuples[small_int] = range_tuples[small_int], range_tuples[i]

    #creates tuples and adds them to new tuple list
    for i in range_tuples:
        new_tuple = tuple((i[0], i[len(i)-1]))
        new_tuples_list.append(new_tuple)

    return new_tuples_list # Replace this.

def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
