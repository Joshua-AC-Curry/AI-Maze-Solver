# AI-Maze-Solver
Using Searching Algorithms to Solve a Maze
<h4> Github: https://github.com/Joshua-AC-Curry/AI-Maze-Solver </h4>

<h3> About </h3>
This project searches through a maze text file and outputs the perforamance of the algorithm used. Currently the algorithms for the maze are depth first search and a*

<h3> Requirements </h3>
python 3 installed. Preferably Python 3.9.13 or later

<h3> How to run </h3>
Instructions given are for windows
- download the repository 
- open command prompt
- cd to directory containing mazeDFS and mazeAStar
- for running DFS algorithm enter command python mazeDFS.py
- for running A* algorithm enter command python AStar.py

<he> Output </h3>
When running the program it ask the user to enter the name of the maze file. When doing this do not include spaces and be sure to include the file extention. Note the program is designed to work with text files. 
Here is an example of what to put: maze-Large.txt

After this the program will run the search algorithm. It then outputs the number of spaces in the maze the program has visited, the run time of the program and the length of the path found. If you want to program to output that path itself you'll have to uncommne the print statement on line 109 for mazeDFS.py and line 133 for mazeAStar.py.
