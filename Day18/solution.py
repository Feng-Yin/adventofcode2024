import re
import copy

def print_input(input_data):
    for row in input_data:
        print("".join(row))

def print_trace(maze, trace):
    maze_copy = copy.deepcopy(maze)
    for y, x in trace:
        maze_copy[y][x] = 'O'
    print_input(maze_copy)

def print_trace_v2(maze, traces):
    maze_copy = copy.deepcopy(maze)
    count = 0
    for trace in traces:
        for y, x in trace:
            if maze_copy[y][x] != 'O':
                count += 1
            maze_copy[y][x] = 'O'
    #print_input(maze_copy)
    print(count)

def pos_to_str(start, next_stop):
    return str(start[0])+":"+str(start[1])+":"+str(next_stop[0])+":"+str(next_stop[1])

def str_to_pos(pos_str):
    l = pos_str.split(":")
    return (int(l[0]), int(l[1])), (int(l[2]), int(l[3]))

def is_inside(maze, p):
    if p[0] < 0 or p[0] >= len(maze):
        return False
    if p[1] < 0 or p[1] >= len(maze[0]):
        return False
    return True

def get_next_stops(maze, pos):
    s1 = (pos[0] + 1, pos[1])
    s2 = (pos[0] - 1, pos[1])
    s3 = (pos[0], pos[1] + 1)
    s4 = (pos[0], pos[1] - 1)
    ret = []
    for p in [s1, s2, s3, s4]:
        if not is_inside(maze, p):
            continue
        if maze[p[0]][p[1]] == '.' or maze[p[0]][p[1]] == 'E': 
            ret.append(p)
    return ret

def get_direction(start, end):
    if start[0] == end[0]:
        if start[1] > end[1]:
            return '<'
        else:
            return '>'
    if start[1] == end[1]:
        if start[0] > end[0]:
            return '^'
        else:
            return 'v'

def get_cost(path):
    return len(path)

def is_path_different(pathes1, pathes2):
    if len(pathes1) != len(pathes2):
        return True
    for k, v in pathes1.items():
        if k not in pathes2:
            return True
        if pathes2[k] != v:
            return True
    return False

def q1(maze, start, end):
    pathes = {}
    costes = {}
    next_stops = get_next_stops(maze, start)
    for next_stop in next_stops:
        key = pos_to_str(start, next_stop)
        pathes[key] = [start, next_stop]
        costes[key] = get_cost(pathes[key])
    last_pathes = {}
    while is_path_different(pathes, last_pathes):
        #print("pathes:", pathes)
        #print("last pathes:", last_pathes)
        #last_pathes = copy.deepcopy(pathes)
        last_pathes = pathes.copy()
        #tmp_pathes = {}
        #tmp_costes = {}
        ##keys_to_remove = []
        for k, v in last_pathes.items():
            if v[-1] == end:
                continue
            next_stops = get_next_stops(maze, v[-1])
            for next_stop in next_stops:
                if next_stop in v:
                    continue
                key = pos_to_str(start, next_stop)
                new_path = v.copy()
                new_path.append(next_stop)
                cost = get_cost(new_path)
                if key in pathes and cost > costes[key]:
                    continue
                pathes[key] = new_path
                costes[key] = cost
    #print(pathes)
    print(costes[pos_to_str(start, end)] - 1)
    #print_trace(maze, pathes[pos_to_str(start, end)])
    
def has_path(maze, start, end, input, i):
    maze_copy = copy.deepcopy(maze)
    for wi in range(i+1):
        maze_copy[input[wi][0]][input[wi][1]] = '#'
    pathes = {}
    costes = {}
    next_stops = get_next_stops(maze_copy, start)
    for next_stop in next_stops:
        key = pos_to_str(start, next_stop)
        pathes[key] = [start, next_stop]
        costes[key] = get_cost(pathes[key])
    last_pathes = {}
    while is_path_different(pathes, last_pathes):
        #print("pathes:", pathes)
        #print("last pathes:", last_pathes)
        #last_pathes = copy.deepcopy(pathes)
        last_pathes = pathes.copy()
        #tmp_pathes = {}
        #tmp_costes = {}
        ##keys_to_remove = []
        for k, v in last_pathes.items():
            if v[-1] == end:
                continue
            next_stops = get_next_stops(maze_copy, v[-1])
            for next_stop in next_stops:
                if next_stop in v:
                    continue
                key = pos_to_str(start, next_stop)
                new_path = v.copy()
                new_path.append(next_stop)
                cost = get_cost(new_path)
                if key in pathes and cost > costes[key]:
                    continue
                pathes[key] = new_path
                costes[key] = cost
    #print(pathes)
    #print(costes[pos_to_str(start, end)] - 1)
    #print_trace(maze, pathes[pos_to_str(start, end)])
    if pos_to_str(start, end) not in pathes:
        return False
    return True
        
def q2(maze, start, end, wall_input):
    done = False
    s = int(len(wall_input) / 2)
    step = s
    while not done:
        step = int(step/2)
        print("Check:", s, wall_input[s])
        #a = input("")
        if not has_path(maze, start, end, wall_input, s):
            if has_path(maze, start, end, wall_input, s - 1):
                print("DONE")
                break
            else:
                s -= step
        else:
            s += step
    print(wall_input[s][1], ',', wall_input[s][0], sep='')

def build_maze(maze_height, maze_width, input, count):
    maze = []
    for j in range(maze_height + 1):
        row = []
        for i in range(maze_width + 1):
            row.append('.')
        maze.append(row)
    for i in range(count):
        maze[input[i][0]][input[i][1]] = '#'
    return maze

with open("./input.txt", "r") as file:
    maze = []
    maze_height = 70
    maze_width = 70
    start = (0, 0)
    end = (maze_height, maze_width)
    wall_input = []
    count = 1024
    for line in file:
        line = line.strip()
        pos = line.split(',')
        wall_input.append((int(pos[1]), int(pos[0])))
    maze = build_maze(maze_height, maze_width, wall_input, count)
    #print_input(maze)
    #q1(maze, start, end)
    q2(maze, start, end, wall_input[count:])
