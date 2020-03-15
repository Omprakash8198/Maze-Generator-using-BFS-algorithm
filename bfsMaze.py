
import turtle                    
import time
import sys
from collections import deque
from tkinter import *

window = Tk()

window.title("BFS Maze Solving Program")

wn = '' # window declared

# this is the class for the Maze
class Maze(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.setup( width = 0, height = 0, startx = None, starty = None)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.setup( width = 0, height = 0, startx = None, starty = None)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)       #delay in speed..set it to more than 0 for seeing the generating bfs path

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.setup( width = 0, height = 0, startx = None, starty = None)
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(2)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.setup( width = 0, height = 0, startx = None, starty = None)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        turtle.setup( width = 0, height = 0, startx = None, starty = None)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(1)


grid1 = [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + +   + + +",
"+++++ +   + + +",
"+     +   +   +",
"+++++++++++++++",
]

grid2 = [
"+++++++++",
"+ ++s++++",
"+ ++ ++++",
"+ ++ ++++",
"+    ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
]

grid3 = [
 "+++++++++++++++",
 "+             +",
 "+             +",
 "+             +",
 "+     e       +",
 "+             +",
 "+             +",
 "+             +",
 "+ s           +",
 "+++++++++++++++",
 ]
grid4 = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++     ++e ++   ++++++++++ ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++  ++",
"+      ++ ++++++++++     ++          ++     +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y location and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            #blue.goto(cell)        # identify frontier cells
            #blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution," ")

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()
    blue.goto(start_x,start_y)
    blue.stamp()
    blue.goto(end_x,end_y)
    blue.stamp()

def backRoute(x, y):
    final.append((x,y))
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        yellow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        print(x,y)
        final.append((x,y))
        x, y = solution[x, y]               # "key value" now becomes the new key

# set up classes
maze = Maze()
red = Red()
green = Green()
yellow = Yellow()  
blue = Blue()
# setup lists
walls = []
path = []
final=[]
visited = set()
frontier = deque()
solution = {}                           # solution dictionary



def reverse_list(list):                 #reversing the list and moving the turtle in selected bfs path
        print('old list',list)
        list.reverse()
        print('new list',list)
        red.goto(start_x,start_y)
        red.stamp()
        for i in list:
                red.goto(i)
                red.stamp()
        

def setGrid(wrapperValue):
	def wrapper_setGrid(gridNumber = wrapperValue):
		wn = turtle.Screen()        
		wn.bgcolor("black")                
		wn.title("BFS Maze Solving Program")
		wn.setup(1300,700)          
      
		if(gridNumber == 1):
			grid = grid1      #selecting small maze
		elif(gridNumber == 2):
			grid = grid2      #selecting medium maze
		elif(gridNumber == 3):
			grid = grid3	  #selecting large maze
		elif(gridNumber == 4):			
			grid = grid4      #selecting xl maze

		window.destroy()          #closing the tkinter window

		setup_maze(grid)
		search(start_x,start_y)
		backRoute(end_x, end_y)
		reverse_list(final)  
               
		wn.exitonclick()			
	return wrapper_setGrid	



# GUI code
heading = Label(window, text="Welcome to BFS maze solving\nsimulator", font=("Arial", 15))
heading.grid(column=0, row=0, padx = 50)

instruction1 = Label(window, text="Select grid size", font=("Arial", 12))
instruction1.grid(column=0, row=2, pady = 10)

btn1 = Button(window, text="Small maze", command=setGrid(1))
btn1.grid(column=0, row=3, pady = 10)

btn2 = Button(window, text="Medium maze", command=setGrid(2))
btn2.grid(column=0, row=4, pady = 10)

btn3 = Button(window, text="Large maze", command=setGrid(3))
btn3.grid(column=0, row=5, pady = 10)

btn3 = Button(window, text="XL maze", command=setGrid(4))
btn3.grid(column=0, row=6, pady = 10)

window.geometry('350x300')
window.mainloop()
