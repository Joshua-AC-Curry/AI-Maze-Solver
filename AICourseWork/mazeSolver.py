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


#put child nodes in stack
#go to child node
#remove that from stack
#keep going while things in stack

def DFS(maze, start, end):

    #check if at end of maze
    

    visited = set()
    
    stack = []
    
    stack.append(start)

    while(stack):
        
        #pop current location from stack
        start = stack.pop()

        if(start == end):
            print(start)
            return "Found End"

        if(start not in visited):
            #print(start)
            visited.add(start)

        #adjacent spaces
        leftSpace = (start[0] - 1, start[1])
        rightSpace = (start[0] + 1, start[1])
        upSpace = (start[0], start[1] - 1)
        downSpace = (start[0], start[1] + 1)

        adjacent = [leftSpace, rightSpace, upSpace, downSpace]

        for space in adjacent:
            if(space not in visited):
                if(maze[space[0]][space[1]] != '#'):
                    stack.append(space)


maze = openMazeFile('maze-Easy.txt')

end = ()
for point in maze[len(maze) - 1]:
    if(point == '-'):
        end = (len(maze)-1, maze[len(maze)-1].index(point))

print(maze)

print(DFS(maze, (0, 1), end))
