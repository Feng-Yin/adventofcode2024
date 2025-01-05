import re
import copy

def print_input(input_data):
    pass

def do_blink(l, blink):
    for bi in range(blink):
        tmp = []
        for i in range(len(l)):
            if l[i] == 0:
                tmp.append(1)
            elif len(str(l[i])) % 2 == 0:
                num_str = str(l[i])
                str_len = len(num_str)
                start = num_str[0:int(str_len/2)]
                end = num_str[int(str_len/2):]
                tmp.append(int(start))
                tmp.append(int(end))
            else:
                tmp.append(l[i]*2024)
        l = tmp
        #print(l)
    return l

def q1(maze, blink):
    print(maze)
    sum = len(do_blink(maze, blink))
    print(sum)
    

def q2(maze, blink):
    step1 = 40
    step2 = blink - step1
    tmp_maze = [maze[0]]
    while step1 > 0:
        tmp_maze = do_blink(tmp_maze, 1)
        step1 -= 1
        print(40 - step1, len(tmp_maze))
    sum = 0
    for i in range(len(tmp_maze)):
        r = do_blink([tmp_maze[i]], step2)
        sum += len(r)
        print("Progress:", i/len(tmp_maze)*100, "%")
    print(sum)

with open("./input.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        row = [int(ch) for ch in line.split()]
        maze.extend(row)
    #print(maze)[]
    q2(maze, 75)