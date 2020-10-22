#IMPORTED STUFF
import queue
import time

#MAZES
def myMaze1():
    maze = []
    maze.append(["|","O", "|", "|", "|", "|","|"])
    maze.append(["|"," ", " ", " ", "|", " ","|"])
    maze.append(["|"," ", "|", " ", "|", " ","|"])
    maze.append(["|"," ", "|", " ", " ", " ","|"])
    maze.append(["|"," ", "|", "|", "|", "|","|"])
    maze.append(["|"," ", " ", " ", " ", " ","|"])
    maze.append(["|","|", "X", "|", "|", "|","|"])

    return maze

def myMaze2():
    maze = []
    maze.append(["|","|", "|", "|", "|", "O", "|", "|", "|"])
    maze.append(["|"," ", " ", " ", " ", " ", " ", " ", "|"])
    maze.append(["|"," ", "|", "|", " ", "|", "|", " ", "|"])
    maze.append(["|"," ", "|", " ", " ", " ", "|", " ", "|"])
    maze.append(["|"," ", "|", " ", "|", " ", "|", " ", "|"])
    maze.append(["|"," ", "|", " ", "|", " ", "|", " ", "|"])
    maze.append(["|"," ", "|", " ", "|", " ", "|", "|", "|"])
    maze.append(["|"," ", " ", " ", " ", " ", " ", " ", "|"])
    maze.append(["|","X", "|", "|", "|", "|", "|", "|", "|"])

    return maze


def setMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("* ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "|"):
            return False

    return True


def findEnd(maze, moves):
    

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        setMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
choice=int(input("Enter the maze you want to choose. 1/2."))
if choice==1:
    maze=myMaze1()
elif choice==2:
    maze=myMaze2()
else:
    print("Invalid option.")

starttime=time.time()
for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
while not findEnd(maze, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

print("Total Time=",time.time()-starttime)