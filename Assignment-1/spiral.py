"""
  File: spiral.py
  Description: creates a spiral array based on dimension n and
  sums the adjacent numbers surrounding a given number

  Student Name: Primo M. Marquez
  Student UT EID: pmm2734

  Partner Name: Henry Chen
  Partner UT EID: hhc462

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: August 28, 2023
  Date Last Modified: August 28, 2023
"""

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral diameter"""
    spiral_array = [[0 for j in range(dim)] for i in range(dim)]
    number_increment = 1
    spiral_array[dim//2][dim//2] = number_increment
    x_index = dim // 2
    y_index = dim // 2
    number_increment += 1

    for i in range (1, dim):
        #if number is odd move right and down j number of times
        if i % 2 != 0:
            for j in range(i):
                #moves 1 column right
                x_index += 1
                spiral_array[y_index][x_index] = number_increment
                number_increment += 1

            for j in range(i):
                #moves 1 row down
                y_index += 1
                spiral_array[y_index][x_index] = number_increment
                number_increment += 1

        #if number is even move left and up j number of times
        else:
            for j in range(i):
                #moves 1 column left
                x_index -= 1
                spiral_array[y_index][x_index] = number_increment
                number_increment += 1

            for j in range(i):
                #moves 1 row up
                y_index -= 1
                spiral_array[y_index][x_index] = number_increment
                number_increment += 1

    #adds the final row to the spiral array
    while x_index < dim - 1:
        x_index += 1
        spiral_array[y_index][x_index] = number_increment
        number_increment += 1

    return spiral_array

def sum_sub_grid(grid, val):
    """ returns the sum of the numbers (not including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    max_index = (len(grid))

    #determines if val is outside array
    if val > max_index ** 2:
        return 0

    #finds index of number
    for i in range(max_index):
        for j in range(max_index):
            if grid[i][j] == val:
                row_index = i
                column_index = j

    if row_index == 0:
        if column_index == 0:
            #only add right, bottom right, bottom
            adjacent_sum = grid[row_index][column_index+1] + grid[row_index+1][column_index+1]
            adjacent_sum += grid[row_index+1][column_index]
        elif column_index == max_index-1:
            #only add left, bottom left, bottom
            adjacent_sum = grid[row_index][column_index-1] + grid[row_index+1][column_index-1]
            adjacent_sum += grid[row_index][column_index+1]
        else:
            #only add left, bottom left, bottom, bottom right, right
            adjacent_sum = grid[row_index][column_index-1] + grid[row_index+1][column_index-1]
            adjacent_sum = adjacent_sum + grid[row_index+1][column_index]
            adjacent_sum += grid[row_index+1][column_index+1]
            adjacent_sum += grid[row_index][column_index+1]

    elif row_index == max_index-1:
        if column_index == max_index-1:
            #add only left, top left, top
            adjacent_sum = grid[row_index][column_index-1] + grid[row_index-1][column_index-1]
            adjacent_sum += grid[row_index-1][column_index]
        elif column_index == 0:
            #add only right, top right, top
            adjacent_sum = grid[row_index][column_index+1] + grid[row_index-1][column_index+1]
            adjacent_sum += grid[row_index-1][column_index]
        else:
            #add only left, top left, top, top right, right
            adjacent_sum = grid[row_index][column_index-1] + grid[row_index-1][column_index-1]
            adjacent_sum += grid[row_index-1][column_index]
            adjacent_sum += grid[row_index-1][column_index+1]
            adjacent_sum += grid[row_index][column_index+1]

    elif column_index == 0:
        #add only top, top right, right, bottom right, bottom
        adjacent_sum = grid[row_index-1][column_index] + grid[row_index-1][column_index+1]
        adjacent_sum += grid[row_index][column_index+1]
        adjacent_sum += grid[row_index+1][column_index+1]
        adjacent_sum += grid[row_index+1][column_index]

    elif column_index == max_index-1:
        #add only top, top left, left, bottom left, bottom
        adjacent_sum = grid[row_index-1][column_index] + grid[row_index-1][column_index-1]
        adjacent_sum += grid[row_index][column_index-1]
        adjacent_sum += grid[row_index+1][column_index-1]
        adjacent_sum += grid[row_index+1][column_index]

    else:
        #add all sides
        adjacent_sum = grid[row_index-1][column_index] + grid[row_index-1][column_index+1]
        adjacent_sum += grid[row_index][column_index+1]
        adjacent_sum += grid[row_index+1][column_index+1]
        adjacent_sum += grid[row_index+1][column_index]
        adjacent_sum = adjacent_sum + grid[row_index+1][column_index-1]
        adjacent_sum += grid[row_index][column_index-1]
        adjacent_sum += grid[row_index-1][column_index-1]

    return adjacent_sum

def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
