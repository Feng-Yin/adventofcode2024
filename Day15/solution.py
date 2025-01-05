import re
import copy

def print_input(input_data):
    for row in input_data:
        print("".join(row))

def find_robot(maze):
    for i in range(len(maze)):
        if '@' in maze[i]:
            return(i, maze[i].index('@'))

def can_move(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    #print("can move1", m, new_pos, maze[new_pos[0]][new_pos[1]])
    while maze[new_pos[0]][new_pos[1]] == 'O':
        new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
        #print("can move2", m, new_pos, maze[new_pos[0]][new_pos[1]])
    if maze[new_pos[0]][new_pos[1]] == '.': 
        #print(m, new_pos, "can move")
        return True
    if maze[new_pos[0]][new_pos[1]] == '#':
        #print(m, new_pos, "can't move") 
        return False

def move_robot(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    #print(robot, m, delta)
    maze[robot[0]][robot[1]] = '.'
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    while maze[new_pos[0]][new_pos[1]] == 'O':
        new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
    if maze[new_pos[0]][new_pos[1]] == '.':
        maze[new_pos[0]][new_pos[1]] = 'O'
        robot = (robot[0] + delta[0], robot[1] + delta[1])
        maze[robot[0]][robot[1]] = '@'
    return maze, robot

def get_sum(maze):
    sum = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'O':
                sum += (i * 100 + j)
    print(sum)

def get_sum_v2(maze):
    sum = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '[':
                sum += (i * 100 + j)
    print(sum)

def q1(maze, move):
    robot = find_robot(maze)
    for m in move:
        if can_move(maze, robot, m):
            maze, robot = move_robot(maze, robot, m)
    #print_input(maze)
    get_sum(maze)

def build_new_maze(maze):
    new_maze = []
    for row in maze:
        new_row = []
        for ch in row:
            if ch == '#': 
                new_row.append('#')
                new_row.append('#')
            if ch == 'O':
                new_row.append('[')
                new_row.append(']')
            if ch == '.': 
                new_row.append('.')
                new_row.append('.')
            if ch == '@':
                new_row.append('@')
                new_row.append('.')
        new_maze.append(new_row)
    #print_input(maze)
    #print_input(new_maze)
    return new_maze

def can_move_v2(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    #print("can move1", m, new_pos, maze[new_pos[0]][new_pos[1]])
    if m == '<' or m == '>':
        while maze[new_pos[0]][new_pos[1]] == '[' or maze[new_pos[0]][new_pos[1]] == ']' :
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            #print("can move2", m, new_pos, maze[new_pos[0]][new_pos[1]])
        if maze[new_pos[0]][new_pos[1]] == '.': 
            #print(m, new_pos, "can move")
            return True
        if maze[new_pos[0]][new_pos[1]] == '#':
            #print(m, new_pos, "can't move") 
            return False
    if m == 'v' or m == '^': 
        if maze[new_pos[0]][new_pos[1]] == '.': 
            return True
        if maze[new_pos[0]][new_pos[1]] == '#': 
            return False
        if maze[new_pos[0]][new_pos[1]] == '[':
            while maze[new_pos[0]][new_pos[1]] == '[' and maze[new_pos[0]][new_pos[1] + 1] == ']':
                new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            if maze[new_pos[0]][new_pos[1]] == '.' and maze[new_pos[0]][new_pos[1] + 1] == '.': 
                return True
            if maze[new_pos[0]][new_pos[1]] == '#' or maze[new_pos[0]][new_pos[1] + 1] == '#': 
                return False
        if maze[new_pos[0]][new_pos[1]] == ']':
            while maze[new_pos[0]][new_pos[1]] == ']' and maze[new_pos[0]][new_pos[1] - 1] == '[':
                new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            if maze[new_pos[0]][new_pos[1]] == '.' and maze[new_pos[0]][new_pos[1] - 1] == '.': 
                return True
            if maze[new_pos[0]][new_pos[1]] == '#' or maze[new_pos[0]][new_pos[1] - 1] == '#': 
                return False

def can_move_v3(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    #print("can move1", m, new_pos, maze[new_pos[0]][new_pos[1]])
    if m == '<' or m == '>':
        while maze[new_pos[0]][new_pos[1]] == '[' or maze[new_pos[0]][new_pos[1]] == ']' :
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            #print("can move2", m, new_pos, maze[new_pos[0]][new_pos[1]])
        if maze[new_pos[0]][new_pos[1]] == '.': 
            #print(m, new_pos, "can move")
            return True
        if maze[new_pos[0]][new_pos[1]] == '#':
            #print(m, new_pos, "can't move") 
            return False
    if m == 'v' or m == '^': 
        if maze[new_pos[0]][new_pos[1]] == '.': 
            return True
        if maze[new_pos[0]][new_pos[1]] == '#': 
            return False
        stack = []
        check_nodes = []
        if maze[new_pos[0]][new_pos[1]] == '[': 
            stack = [new_pos, (new_pos[0], new_pos[1]+1)]
        if maze[new_pos[0]][new_pos[1]] == ']': 
            stack = [(new_pos[0], new_pos[1]-1), new_pos]
        if m == '^':
            while len(stack) > 0:
                pos = stack.pop(0)
                check_nodes.append(pos)
                if maze[pos[0]-1][pos[1]] == '[': 
                    if (pos[0]-1, pos[1]) not in stack:
                        stack.append((pos[0]-1, pos[1]))
                    if (pos[0]-1, pos[1]+1) not in stack:
                        stack.append((pos[0]-1, pos[1]+1))
                if maze[pos[0]-1][pos[1]] == ']':
                    if (pos[0]-1, pos[1]) not in stack:
                        stack.append((pos[0]-1, pos[1]))
                    if (pos[0]-1, pos[1]-1) not in stack:
                        stack.append((pos[0]-1, pos[1]-1))
            for y, x in check_nodes:
                if maze[y-1][x] == '#':
                    return False
            return True
        if m == 'v':
            while len(stack) > 0:
                pos = stack.pop(0)
                check_nodes.append(pos)
                if maze[pos[0]+1][pos[1]] == '[': 
                    if (pos[0]+1, pos[1]) not in stack:
                        stack.append((pos[0]+1, pos[1]))
                    if (pos[0]+1, pos[1]+1) not in stack:
                        stack.append((pos[0]+1, pos[1]+1))
                if maze[pos[0]+1][pos[1]] == ']':
                    if (pos[0]+1, pos[1]) not in stack:
                        stack.append((pos[0]+1, pos[1]))
                    if (pos[0]+1, pos[1]-1) not in stack:
                        stack.append((pos[0]+1, pos[1]-1))
            for y, x in check_nodes:
                if maze[y+1][x] == '#':
                    return False
            return True

def move_robot_v3(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    maze[robot[0]][robot[1]] = '.'
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    new_robot = (robot[0] + delta[0], robot[1] + delta[1])
    #print("can move1", m, new_pos, maze[new_pos[0]][new_pos[1]])
    if m == '<' or m == '>':
        while maze[new_pos[0]][new_pos[1]] == '[' or maze[new_pos[0]][new_pos[1]] == ']':
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            #print("can move2", m, new_pos, maze[new_pos[0]][new_pos[1]])
        if maze[new_pos[0]][new_pos[1]] == '.': 
            if m == '<': 
                #print(new_pos[1], new_robot[1])
                for i in range(new_pos[1], new_robot[1]):
                    if (new_pos[1] - i) % 2 == 0:
                        maze[new_pos[0]][i] = '['
                    else:
                        maze[new_pos[0]][i] = ']'
            if m == '>': 
                for i in range(new_robot[1] + 1, new_pos[1] + 1):
                    if (new_robot[1] + 1 - i) % 2 == 0:
                        maze[new_pos[0]][i] = '['
                    else:
                        maze[new_pos[0]][i] = ']'
    if m == 'v' or m == '^':
        stack = []
        check_nodes = []
        if maze[new_pos[0]][new_pos[1]] == '[': 
            stack = [new_pos, (new_pos[0], new_pos[1]+1)]
        if maze[new_pos[0]][new_pos[1]] == ']': 
            stack = [(new_pos[0], new_pos[1]-1), new_pos]
        if m == '^':
            while len(stack) > 0:
                pos = stack.pop(0)
                check_nodes.append(pos)
                if maze[pos[0]-1][pos[1]] == '[': 
                    if (pos[0]-1, pos[1]) not in stack:
                        stack.append((pos[0]-1, pos[1]))
                    if (pos[0]-1, pos[1]+1) not in stack:
                        stack.append((pos[0]-1, pos[1]+1))
                if maze[pos[0]-1][pos[1]] == ']':
                    if (pos[0]-1, pos[1]) not in stack:
                        stack.append((pos[0]-1, pos[1]))
                    if (pos[0]-1, pos[1]-1) not in stack:
                        stack.append((pos[0]-1, pos[1]-1))
            new_nodes = []
            for y, x in check_nodes:
                new_nodes.append((y-1, x, maze[y][x]))
            for y, x in check_nodes:
                maze[y][x] = '.'
            for y, x, ch in new_nodes:
                maze[y][x] = ch

        if m == 'v':
            while len(stack) > 0:
                pos = stack.pop(0)
                check_nodes.append(pos)
                if maze[pos[0]+1][pos[1]] == '[': 
                    if (pos[0]+1, pos[1]) not in stack:
                        stack.append((pos[0]+1, pos[1]))
                    if (pos[0]+1, pos[1]+1) not in stack:
                        stack.append((pos[0]+1, pos[1]+1))
                if maze[pos[0]+1][pos[1]] == ']':
                    if (pos[0]+1, pos[1]) not in stack:
                        stack.append((pos[0]+1, pos[1]))
                    if (pos[0]+1, pos[1]-1) not in stack:
                        stack.append((pos[0]+1, pos[1]-1))
            new_nodes = []
            for y, x in check_nodes:
                new_nodes.append((y+1, x, maze[y][x]))
            for y, x in check_nodes:
                maze[y][x] = '.'
            for y, x, ch in new_nodes:
                maze[y][x] = ch
        
    maze[new_robot[0]][new_robot[1]] = '@'
    if maze[new_robot[0]][new_robot[1]-1] == '[':
        maze[new_robot[0]][new_robot[1]-1] = '.'
    if maze[new_robot[0]][new_robot[1]+1] == ']':
        maze[new_robot[0]][new_robot[1]+1] = '.'
    return maze, new_robot

def move_robot_v2(maze, robot, m):
    delta = (0, 0)
    if m == '<':
        delta = (0, -1)
    if m == '>':
        delta = (0, 1)
    if m == '^':
        delta = (-1, 0)
    if m == 'v':
        delta = (1, 0)
    maze[robot[0]][robot[1]] = '.'
    new_pos = (robot[0] + delta[0], robot[1] + delta[1])
    new_robot = (robot[0] + delta[0], robot[1] + delta[1])
    #print("can move1", m, new_pos, maze[new_pos[0]][new_pos[1]])
    if m == '<' or m == '>':
        while maze[new_pos[0]][new_pos[1]] == '[' or maze[new_pos[0]][new_pos[1]] == ']':
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            #print("can move2", m, new_pos, maze[new_pos[0]][new_pos[1]])
        if maze[new_pos[0]][new_pos[1]] == '.': 
            if m == '<': 
                #print(new_pos[1], new_robot[1])
                for i in range(new_pos[1], new_robot[1]):
                    if (new_pos[1] - i) % 2 == 0:
                        maze[new_pos[0]][i] = '['
                    else:
                        maze[new_pos[0]][i] = ']'
            if m == '>': 
                for i in range(new_robot[1] + 1, new_pos[1] + 1):
                    if (new_robot[1] + 1 - i) % 2 == 0:
                        maze[new_pos[0]][i] = '['
                    else:
                        maze[new_pos[0]][i] = ']'
    if m == 'v' or m == '^':
        if maze[new_pos[0]][new_pos[1]] == '[':
            #maze[new_robot[0]][new_robot[1]+1] = '.'
            while maze[new_pos[0]][new_pos[1]] == '[' and maze[new_pos[0]][new_pos[1] + 1] == ']':
                new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
            if maze[new_pos[0]][new_pos[1]] == '.' and maze[new_pos[0]][new_pos[1] + 1] == '.': 
                if m == '^': 
                    for i in range(new_pos[0], new_robot[0]):
                        maze[i][new_pos[1]] = '['
                        maze[i][new_pos[1]+1] = ']'
                else:
                    for i in range(new_robot[0] + 1, new_pos[0] + 1):
                        maze[i][new_pos[1]] = '['
                        maze[i][new_pos[1]+1] = ']'
        if maze[new_pos[0]][new_pos[1]] == ']': 
            #print("1", new_pos)
            #maze[new_robot[0]][new_robot[1]-1] = '.'
            while maze[new_pos[0]][new_pos[1]] == ']' and maze[new_pos[0]][new_pos[1] - 1] == '[':
                new_pos = (new_pos[0] + delta[0], new_pos[1] + delta[1])
                #print("2", new_pos)
            if maze[new_pos[0]][new_pos[1]] == '.' and maze[new_pos[0]][new_pos[1] - 1] == '.': 
                if m == '^': 
                    #print(new_pos, new_robot)
                    for i in range(new_pos[0], new_robot[0]):
                        maze[i][new_pos[1]] = ']'
                        maze[i][new_pos[1]-1] = '['
                else:
                    for i in range(new_robot[0] + 1, new_pos[0] + 1):
                        maze[i][new_pos[1]] = ']'
                        maze[i][new_pos[1]-1] = '['
    maze[new_robot[0]][new_robot[1]] = '@'
    if maze[new_robot[0]][new_robot[1]-1] == '[':
        maze[new_robot[0]][new_robot[1]-1] = '.'
    if maze[new_robot[0]][new_robot[1]+1] == ']':
        maze[new_robot[0]][new_robot[1]+1] = '.'
    return maze, new_robot

def q2(maze, move):
    new_maze = build_new_maze(maze)
    robot = find_robot(new_maze)
    #print_input(new_maze)
    for m in move:
        #print(m)
        #input("next move")
        if can_move_v3(new_maze, robot, m):
            #print("can move:", m)
            new_maze, robot = move_robot_v3(new_maze, robot, m)
            #print_input(new_maze)
            #break
        #else:
            #print("cannot move:", m)
            #print_input(new_maze)
    #print_input(new_maze)
    get_sum_v2(new_maze)

with open("./input.txt", "r") as file:
    maze = []
    move = []
    map_mode = True
    for line in file:
        line = line.strip()
        if line == "": 
            map_mode = False
        if map_mode == True:
            row = list(line)
            maze.append(row)
        else:
            row = list(line)
            move.extend(row)
    q2(maze, move)
    #build_new_maze(maze)