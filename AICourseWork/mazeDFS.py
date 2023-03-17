import time
"""
Function for getting a maze from a text file

params: fileName: the name of the maze file
"""
def openMazeFile(fileName):
    maze = []
    with open(fileName, "r") as file:
        for row in file:
            maze.append(row.strip().split())
    return maze

"""
depth first search algorithm for the maze

params: 
    maze: the maze as a 2d array
    start: the cords for the start of the maze
    end: the cords for the end of the maze
"""
def DFS(maze, start, end):

    #check if at end of maze
    
    path = [] #The algorithm has gone

    visited = set() #Set of all the visited cords
    
    stack = [] #stack of nodes thats to be visited
    
    stack.append(start)

    while(stack):
        
        #pop current location from stack
        current = stack.pop()

        if(current == end):
            path.append(current)
            
            return path

        #adding current space to visited set
        if(current not in visited):
            path.append(current)
            visited.add(current)

        
        leftSpace = (current[0] - 1, current[1])
        rightSpace = (current[0] + 1, current[1])
        upSpace = (current[0], current[1] - 1)
        downSpace = (current[0], current[1] + 1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace] #list of adjacent spaces

        #adding non-visited spaces to the stack
        for space in adjacent:
            if(space not in visited):
                if(maze[space[0]][space[1]] != '#'):
                    stack.append(space)


"""
function to test the depth first search algorithm

"""
def testDFS():
    inp = input("Enter Maze ")

    maze = openMazeFile(inp)

    #Getting cords for start of maze
    start = ()
    count = 0
    for point in maze[0]:
        if(point == '-'):
            start = (count, 0)

        count+=1

    #Getting cords for end of maze
    end = ()
    for point in maze[len(maze) - 1]:
        if(point == '-'):
            end = (len(maze)-1, maze[len(maze)-1].index(point))

    #Outputting the maze
    #print(maze)

    #Starting timer for the DFS algorithm
    startTime = time.time()

    #Outputting the result of the DFS
    path = DFS(maze, start, end)
    #print(path)
    print(len(path))

    #Ending timer for the DFS algorithm
    endTime = time.time()
    runTime = endTime - startTime
    print("Run Time = " + str(runTime))


print("Starting")
testDFS()
print("Done")