# Algorithms

This python based code basically finds the connected component in a 2D matrix of 0 and 1.
It uses DFS (Depth First Search) algorithm to traverse a particular connected component.



#Built on Python3.8 on Mac
#Author: @Reetu Bok
#Date: Nov 3, 2019
#############################################################################
#   To run on terminal >> python3.8 Shape_Counting.py
#   You will see something like following when run successfully
#   >python3.8 Shape_Counting.py
#   Found beginning node of new shape (2, 2)
#   Found beginning node of new shape (2, 10)
#   Found beginning node of new shape (6, 2)
#   Found beginning node of new shape (6, 9)
#   Found beginning node of new shape (9, 5)
#   Total count of shapes =  5
#############################################################################


input = [[1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,0,0,0,0,0,0,1,1],
         [1,0,1,1,0,0,0,0,0,0,1,1],
         [1,0,0,1,1,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,1,1,0,0,0,0,1,1,1],
         [1,0,1,1,1,0,0,0,0,0,0,1],
         [1,0,1,1,1,0,0,0,0,0,0,1],
         [1,0,0,0,0,1,1,0,0,0,0,1],
         [1,0,0,0,0,1,1,0,0,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1]]
