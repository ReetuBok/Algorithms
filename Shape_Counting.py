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

#############################################################################
#   This function checks that node is within
#   valid bound of 2D matrix of a given size
#   For node(-1,2) is out of bounds for 15x12 sized matrix
#   But node (7,8) is with in valid bounds for 15x12 sized matrix
#############################################################################

def node_meets_matrix_bound(graph, node):
    graph_rows_count = len(graph)
    graph_col_count = len(graph[0])
    
    #node[0] is row location of a node
    #node[1] is column location of a node
    #check row location of node within range of 0 and row size of matrix
    #check col location of node within range of 0 and col size of matrix
    if (node[0]<0 or node[0]>=graph_rows_count):
        return False
    if (node[1]<0 or node[1]>=graph_col_count):
        return False
    return True

#############################################################################
#   This function traverses a 2D matrix.
#   This function would visit a node and its neighbor only if value of node matches 1
#   We maintain a set of visited nodes, any newly visited node gets added in it
#   Function traverses only 4 neighbor of a node (north, south, east, west)
#   Code is based on Flood fill algorithm
#   https://en.wikipedia.org/wiki/Flood_fill
#############################################################################
def traverse(graph, node, visited):

    #if node value is not 1
    if(graph[node[0]][node[1]] != 1):
        return
      
    #all nodes are visited already.
    if (len(visited) == (len(graph) * len(graph[0]))):
        return
    
    
    if node in visited:
        #node is already visited
        #print (node,"== landed on already visited node")
        return
    else:
        #node is not visited earlier
        #node is visited now, hence add it to visited set
        visited.add(node)
        #print (visited ,  "visited and length = " , len(visited))
        
        #Each node has only 4 neighbor as per the requirment
        #This can be expanded to diagonal neighbours if needed.
        north_node = (node[0], node[1]-1)
        south_node = (node[0], node[1]+1)
        west_node = (node[0]-1, node[1])
        east_node = (node[0]+1, node[1])
        
        #check each neighbor of node if it is part of shape or not
        if(node_meets_matrix_bound(graph,north_node) == True):
            traverse(graph, north_node , visited)
            
        if(node_meets_matrix_bound(graph,south_node) == True):
            traverse(graph, south_node, visited)
            
        if(node_meets_matrix_bound(graph,west_node) == True):
            traverse(graph, west_node, visited)

        if(node_meets_matrix_bound(graph,east_node) == True):
            traverse(graph, east_node, visited)
                     
    return

#############################################################################
#   This function finds the connected component
#   It iterates over every unvisited node in 2D matrix
#   whenever it finds 1, it checks all its neighbor using traverse
#   if neighbor also has value 1, its part of the shape otherwise not.
#############################################################################

##################    Important Note:::     ############
#This method may run out of memory when matrix are of really large size,
#non-recursive way to traverse each node of 2D matrix could remediate it
def count_connected_component(graph, visited=None):

    if visited is None:
         visited = set() # Use set instead of list since we just need to search an element in visited set , search is mentioned to be faster in set
         
    shape_count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            node = (i,j)
            if ((node not in visited) and graph[i][j] ==1 ):
                print("Found beginning node of new shape", node)
                traverse(graph,node,visited)
                shape_count+=1
    return shape_count
            

#############################################################################

print ("Total count of shapes = ", count_connected_component(input))
