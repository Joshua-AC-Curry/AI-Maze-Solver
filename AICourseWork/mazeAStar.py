import time
from queue import PriorityQueue

def openMazeFile(fileName):
    """
    Function for getting a maze from a text file

    params: fileName: the name of the maze file
    """
    
    maze = []
    with open(fileName, "r") as file:
        for row in file:
            maze.append(row.strip().split())
    return maze


def heuristic(current, end):
    """
    A function which calculates the heuristic value at a given point for the a* algorithm
    it currently uses the euclidian heuristic

    params:
        current: cords for current location
        end: cords for end location
    """

    return ((current[0] - end[0]) **2) + ((current[1] - end[1]) ** 2)

def aStar(maze, start, end):
    """
    a* search algorithm for the maze

    params: 
        maze: the maze as a 2d array
        start: the cords for the start of the maze
        end: the cords for the end of the maze
    """

    queue = PriorityQueue() #Priotiy queue ofr spaces in maze
    path = {} #The path the program has travelled
    costSoFar = {} #A dictionary of spaecs and their cost

    #Adding start to the queue and cost
    queue.put(start, 0)
    costSoFar[start] = 0

    #Running as long as queue is not empty
    while(queue):
        #getting current space from queue
        current = queue.get() 

        #check to see if at end of maze
        if current == end:
            #getting path through maze
            path[space] = current
            pathList = []
            pathList.append(current)
            while(current != start):
                pathList.append(path[current])
                current = path[current]

            print("The number of spaces visitied is " , len(path))

            return pathList[::-1]
        
        leftSpace = (current[0] - 1, current[1])
        rightSpace = (current[0] + 1, current[1])
        upSpace = (current[0], current[1] - 1)
        downSpace = (current[0], current[1] + 1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace] #list of adjacent spaces

        for space in adjacent:
            newCost = costSoFar[current] + 1 #getting the cost of the adjacent space

            #checking to see if adjacent space is better
            if(space not in costSoFar or newCost < costSoFar[space]):
                if(maze[space[0]][space[1]] != '#'):
                    #adding new space to the dictionary of costs
                    costSoFar[space] = newCost

                    #working out the priority of the new space
                    priority = newCost + heuristic(space, end)

                    #adding new space to the queue
                    queue.put(space, priority)

                    #adding new space to the path
                    path[space] = current   


def testAStar():
    """
    function to test the a* algorithm

    """

    inp = input("Enter Maze ")
    
    maze = openMazeFile(inp)

    #Getting cords for start of maze
    start = ()
    count = 0
    for point in maze[0]:
        if(point == '-'):
            start = (0, count)

        count+=1

    #Getting cords for end of maze
    end = ()
    for point in maze[len(maze) - 1]:
        if(point == '-'):
            end = (len(maze)-1, maze[len(maze)-1].index(point))

    #Outputting the maze
    #print(maze)

    #Starting timer for a*
    startTime = time.time()

    #running a* algorithm
    path = aStar(maze, start, end)

    #Ending timer for the a* algorithm
    endTime = time.time()
    runTime = endTime - startTime
    print("Run Time = " + str(runTime))

    #Outputting the result of the a*
    #print(path)
    print("Lenght of path found is ", len(path))
   

print("Starting")
testAStar()
print("done")