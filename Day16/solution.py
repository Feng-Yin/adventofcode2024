import re
import copy

def print_input(input_data):
    for row in input_data:
        print("".join(row))

def print_trace(maze, trace):
    maze_copy = copy.deepcopy(maze)
    for y, x in trace:
        maze_copy[y][x] = 'X'
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

def get_next_stops(maze, pos):
    s1 = (pos[0] + 1, pos[1])
    s2 = (pos[0] - 1, pos[1])
    s3 = (pos[0], pos[1] + 1)
    s4 = (pos[0], pos[1] - 1)
    ret = []
    for p in [s1, s2, s3, s4]:
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
    direction = '>'
    cost = 0
    for i in range(1, len(path)):
        cost += 1
        d = get_direction(path[i-1], path[i])
        if d != direction:
            cost += 1000
            direction = d
    return cost

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
    print(costes[pos_to_str(start, end)])
    #print_trace(maze, last_pathes[pos_to_str(start, end)])
    
def q2(maze, start, end):
    pathes = {}
    costes = {}
    next_stops = get_next_stops(maze, start)
    for next_stop in next_stops:
        key = pos_to_str(start, next_stop)
        pathes[key] = [[start, next_stop]]
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
        for k, vs in last_pathes.items():
            for v in vs:
                if v[-1] == end:
                    continue
                next_stops = get_next_stops(maze, v[-1])
                #if v[-1] == (7, 4):
                #    print(v, next_stops)
                for next_stop in next_stops:
                    if next_stop in v:
                        continue
                    key = pos_to_str(start, next_stop)
                    new_path = v.copy()
                    #new_path = v
                    new_path.append(next_stop)
                    cost = get_cost(new_path)
                    #if next_stop == (7, 5):
                    #    print(new_path, cost)
                    if key in pathes and new_path not in pathes[key] and (cost == costes[key] or abs(cost - costes[key] == 1000)):
                        pathes[key].append(new_path)
                        #if next_stop == (7, 5):
                        #    print("same cost", pathes[key])
                        #    print_trace_v2(maze, pathes[key])
                        continue
                    if key in pathes and cost > costes[key]:
                        #if next_stop == (7, 5):
                        #    print(new_path, "high cost", cost, costes[key], pathes[key])
                        continue
                    if key in pathes and cost < costes[key]:
                        #if next_stop == (7, 5):
                        #    print(new_path, "low cost", cost, costes[key])
                        pathes[key] = [new_path]
                        costes[key] = cost
                        continue
                    if key not in pathes:
                        #if next_stop == (7, 5):
                        #    print(new_path, "new path", cost)
                        pathes[key] = [new_path]
                        costes[key] = cost
    #print(pathes[pos_to_str(start, end)])
    #print(pathes[pos_to_str(start, (7, 4))])
    print(costes[pos_to_str(start, end)])
    fkey = pos_to_str(start, end)
    lcost = costes[fkey]
    fpathes = []
    for path in pathes[fkey]:
        if get_cost(path) <= lcost:
            fpathes.append(path)
    print_trace_v2(maze, fpathes)

with open("./input.txt", "r") as file:
    maze = []
    y = 0
    start = (0, 0)
    end = (0, 0)
    for line in file:
        line = line.strip()
        row = list(line)
        maze.append(row)
        if 'S' in row:
            start = (y, row.index('S'))
        if 'E' in row:
            end = (y, row.index('E'))
        y += 1
    #print_input(maze)
    #print("S:", start)
    #print("E:", end)
    q2(maze, start, end)
