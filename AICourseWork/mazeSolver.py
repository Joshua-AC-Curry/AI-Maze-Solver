import time
from queue import PriorityQueue
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
Function to check if a space is in a list of spaces by its cords

params: vals: a tuple of current cords, list: the list to be check if the space is in
"""
def checkInList(vals, list):
    for item in list:
        if(vals[0] == item[0] and vals[1] == item[1]):
            return True
        
    return False

#put child nodes in stack
#go to child node
#remove that from stack
#keep going while things in stack
"""
depth first search algorithm for the maze

params: 
    maze: the maze as a 2d array
    start: the cords for the start of the maze
    end: the cords for the end of the maze
"""
def DFS(maze, start, end):

    #Starting timer for the DFS
    startTime = time.time()

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
            print(path)
            print(len(path))

            endTime = time.time()
            runTime = endTime - startTime
            print("Run Time = " + str(runTime))

            return "Found End"

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
    print(maze)

    #Outputting the result of the DFS
    

    print(DFS(maze, start, end))

def aStar(maze, start, end):
    openList = []
    closedList = []

    path = {}

    openList.append(start)
    

    #Looping to end is found
    while(openList):
        #having 0 be x, 1 be y, 2 be f, 3 be h, 4 be g

        #getting the current space
        current = openList[0]
        for space in openList:
            if(space[2] < current[2]):
                current = space

        
        openList.remove(current)

        #checking if its the final node
        if(current[0] == end[0] and current[1] == end[1]):
            print(current)
            #print(path)
            

            pathList = []
            pathList.append(current)
            while(current != start):
                pathList.append(path[current])
                current = path[current]

            #print(pathList)
            print(len(pathList))
            return "Found End"

        closedList.append(current)

        #Getting list of adjacent nodes
        leftSpace = (current[0] - 1, current[1], -1, -1, -1)
        rightSpace = (current[0] + 1, current[1], -1, -1, -1)
        upSpace = (current[0], current[1] - 1, -1, -1, -1)
        downSpace = (current[0], current[1] + 1, -1, -1, -1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace] #list of adjacent spaces
            
        for space in adjacent:
            if(maze[space[0]][space[1]] != '#'):
                if(maze[space[0]][space[1]] == '#'):
                    print("lmao")
                    continue

                if checkInList(space, closedList):
                    continue
            
                #Calculating g, h and f
                spaceList = list(space)
                #g
                spaceList[4] = current[4] + 1
                #h   
                #consider using manhatten equaiton for this
                spaceList[3] = ((space[0] - end[0]) **2) + ((space[1] - end[1]) **2)
                #f
                spaceList[2] = spaceList[4] + spaceList[3]

                space = tuple(spaceList)
                #print(space)

                for openSpace in openList:
                    if(space[0] == openSpace[0] and space[1] == openSpace[1] and space[4] > openSpace[4]):
                        print("Here")
                        path[space] = current
                        continue
            
                openList.append(space)
                path[space] = current

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def aStar2(maze, start, end):

    #Creating start and end nodes
    startNode = Node(None, start)
    startNode.g = 0
    startNode.h = 0
    startNode.f = 0

    endNode = Node(None, end)
    endNode.g = 0
    endNode.h = 0
    endNode.f = 0

    #Initialize openList and closedList
    openList = []
    closedList = []

    #Add startNode
    openList.append(startNode)

    while(openList):

        #Get the current node
        currentNode = openList[0]
        currentIndex = 0

        for index, item  in enumerate(openList):
            if(item.f < currentNode.f):
                currentNode = item
                currentIndex = index
            
        #pop current off openList, add to clsoedList
        openList.pop(currentIndex)
        closedList.append(currentNode)

        #Checking if at end
        if(currentNode == endNode):
            path = []
            current = currentNode
            while(current is not None):
                path.append(current.popsition)
                current = current.parent
            return path[::-1]
        
        #Genearte children
        children = []
        adjacents = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in adjacents:

            #Get node position
            nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

            #Make sure within maze
            if nodePosition[0] > (len(maze) - 1) or nodePosition[0] < 0 or nodePosition[1] > (len(maze[len(maze)-1]) -1) or nodePosition[1] < 0:
                continue
            
            #Checking to see if its a wall
            if maze[nodePosition[0]][nodePosition[1]] != '#':
                continue

            # Create new node
            newNode = Node(currentNode, nodePosition)

            # Append
            children.append(newNode)
            
        #Looping through children
        for child in children:


            #child is in closedList
            for closedChild in closedList:
                if child == closedChild:
                    continue
            
            # Create the f, g, and h values
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue
        
            openList.append(child)


"""
Function to test the a* algorithm

"""
def testAStar():
    #inp = input("Enter Maze ")

    maze = openMazeFile('maze-VLarge.txt')

    #Getting cords for start of maze
    start = ()
    x = 0
    for point in maze[0]:
        if(point == '-'):
            start = (0, x, -1, -1, -1)
            #start = (0, x)

        x+=1    

    #Getting cords for end of maze
    end = ()
    for point in maze[len(maze) - 1]:
        if(point == '-'):
            end = (len(maze)-1, maze[len(maze)-1].index(point))


    #Outputting the maze
    #print(maze)

    #Outputting the result of the DFS
    
    #Its wrong for large and too slow for vLarge
    
    print(aStar(maze, start, end))


#a star is breadth first search
#but with a bit of disjtra
#but instead of distance between nodes its disctance from finish
#start with making breadthfirst

def breadth(maze, start, end):
    queue = PriorityQueue()
    visited = []
    path = {}

    #(y, x, distance to end(f/h))
    queue.put(start, 0)
    visited.append(start)

    while(queue):
        current = queue.get() 

        #check to see if at end of maze
        if current == end:
            path[space] = current
            pathList = []
            pathList.append(current)
            while(current != start):
                pathList.append(path[current])
                current = path[current]

            return pathList[::-1]
        
        leftSpace = (current[0] - 1, current[1])
        rightSpace = (current[0] + 1, current[1])
        upSpace = (current[0], current[1] - 1)
        downSpace = (current[0], current[1] + 1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace] #list of adjacent spaces

        for space in adjacent:
            if(space not in visited):
                if(maze[space[0]][space[1]] != '#'):
                    visited.append(space)
                    path[space] = current
                    queue.append(space)   

def heuristic(current, end):
    return ((current[0] - end[0]) **2) + ((current[1] - end[1]) ** 2)

def aStar3(maze, start, end):
    queue = PriorityQueue()
    visited = []
    path = {}
    costSoFar = {}

    #(y, x, distance to end(f/h))
    queue.put(start, 0)
    costSoFar[start] = 0
    visited.append(start)

    while(queue):
        current = queue.get() 

        #check to see if at end of maze
        if current == end:
            path[space] = current
            pathList = []
            pathList.append(current)
            while(current != start):
                pathList.append(path[current])
                current = path[current]

            return pathList[::-1]
        
        leftSpace = (current[0] - 1, current[1])
        rightSpace = (current[0] + 1, current[1])
        upSpace = (current[0], current[1] - 1)
        downSpace = (current[0], current[1] + 1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace] #list of adjacent spaces

        for space in adjacent:
            newCost = costSoFar[current] + 1
            if(space not in costSoFar or newCost < costSoFar[space]):
                if(maze[space[0]][space[1]] != '#'):
                    costSoFar[space] = newCost
                    priority = newCost + heuristic(space, end)
                    queue.put(space, priority)
                    path[space] = current   


def testAStar3():
    #inp = input("Enter Maze ")

    maze = openMazeFile("maze-VLarge.txt")

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

    #Outputting the result of the DFS
    
    print("starting")
    #print(aStar3(maze, start, end))
    print(len(aStar3(maze, start, end)))
#calling testDFS     
#testDFS()
#calling testA*
#testAStar()

testAStar3()#modify to dijstra
print("so done")
