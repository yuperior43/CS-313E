"""
File: dna.py
Description: Takes a pair of strings and determines the longest substring within the pair.
If there are multiple common substrings with the same length, return all substrings.
Student Name: Primo M. Marquez
Student UT EID: pmm2734
Partner Name: Henry Chen
Partner UT EID: hhc462
Course Name: CS 313E
Unique Number: 52590
Date Created: August 23, 2023
Date Last Modified: August 28, 2023

"""

def longest_subsequence(string_1, string_2):
    '''returns a list of all longest common substrings'''

    subsequences = []
    #call length_subsequence
    length = length_subsequence(string_1, string_2)

    #iterates through all possible substrings in string_1
    for i in range (len(string_1)):
        for j in range(len(string_1)+1):
            if string_1[i:j] in string_2:
                #extra credit - if substring is already in list, do not append to list
                if string_1[i:j] in subsequences:
                    continue
                if len(string_1[i:j]) == length:
                    subsequences.append(string_1[i:j])
    subsequences.sort()

    #creates empty list if no common substrings
    if subsequences[0] == '':
        subsequences = []

    return subsequences

def length_subsequence(string_1, string_2):
    '''returns the length of the longest common substring'''

    subsequence = ''

    #iterates through all possible substrings in string_1
    for i in range (len(string_1)):
        for j in range(len(string_1)+1):
            if string_1[i:j] in string_2:
                if len(string_1[i:j]) > len(subsequence):
                    subsequence = string_1[i:j]

    return len(subsequence)


def main():
    ''' reads data and formats results'''

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
