#  File: MST.py

#  Description: Determine the sum of edge weights in a maximal spanning tree

#  Student Name: 

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 

# Find set of vertex i
def find(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i
 
# Does union of i and j. It returns
# false if i and j are already in same
# set.
def union(i, j, parent):
    a = find(i, parent)
    b = find(j, parent)
    parent[a] = b
 

# Input: matrix is a 2d square list of integer elements representing edge weights; 0 represents a nonexistent edge
# Output: return the sum of edge weights of the maximal spanning tree
def mst_edge_sum(matrix):
    V = len(matrix)
    parent = [i for i in range(V)]

    max_cost = 0 # Cost of min MST
 
    # Initialize sets of disjoint sets
    for i in range(V):
        parent[i] = i
 
    # Include maximum weight edges one by one
    for _ in range(V - 1):
        u, v = max_weight_edge(matrix, V, parent)
        if find(u, parent) != find(v, parent):
            max_cost += matrix[u][v]
            union(u, v, parent)

    return max_cost

def max_weight_edge(matrix, V, parent):
    max_weight = 0
    max_edge = (-1, -1)
    for i in range(V):
        for j in range(i + 1, V):
            if matrix[i][j] > max_weight and find(i, parent) != find(j, parent):
                max_weight = matrix[i][j]
                max_edge = (i, j)

    return max_edge

def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to mst_edge_sum()
    result = mst_edge_sum(matrix)

    # print the result to standard output
    print(result)


if __name__ == "__main__":
    main()