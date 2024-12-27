# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name:

# Student UT EID:

# Course Name: CS 313E

# Unique Number: 86610

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

  # get the distance to another Point object
  def dist (self, other):
      self.dist =  math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
      return self.dist

class Triangle (Point):
    # constructor
    def __init__(self, PointA, PointB, PointC):

        self.PointA = PointA
        self.PointB = PointB
        self.PointC = PointC

    # check congruence of Triangles with equality
    # returns True or False (bolean)
    def __eq__(self, other):
        return ((abs(self.length1 - other.length1) == 0) and
                (abs(self.length2 - other.length2) == 0) and 
                (abs(self.length3 - other.length3) == 0))

    # returns whether or not the triangle is valid
    # returns True or False (bolean)
    def is_triangle(self):
        self.length1 = self.PointA.dist(self.PointB)
        self.length2 = self.PointB.dist(self.PointC)
        self.length3 = self.PointC.dist(self.PointA)
        return ((self.length1 + self.length2 > self.length3) and (self.length2 + self.length3 > self.length1) and
                (self.length1 + self.length3 > self.length2))

    # return the area of the triangle:
    def area(self):
        #|[x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)]/2| 
        area = abs((self.PointA.x * (self.PointB.y - self.PointC.y) + 
                    self.PointB.x * (self.PointC.y - self.PointA.y)
                   + self.PointC.x * (self.PointA.y - self.PointB.y))/2)
        return float(area)

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA.area())
    print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
