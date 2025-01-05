import re
import copy
import multiprocessing

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

def get_next_stops(maze, pos, prev=None):
    s1 = (pos[0] + 1, pos[1])
    s2 = (pos[0] - 1, pos[1])
    s3 = (pos[0], pos[1] + 1)
    s4 = (pos[0], pos[1] - 1)
    ret = []
    for p in [s1, s2, s3, s4]:
        if not is_inside(maze, p):
            continue
        if maze[p[0]][p[1]] == '.' and p != prev: 
            ret.append(p)
    return ret

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
def is_sub_list(v1, v2):
    if len(v1) >= len(v2):
        return False
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True

def dedup(pathes, costes):
    #print("dedup input:", pathes, costes)
    items = pathes.copy().items()
    for k1, v1 in items:
        for k2, v2 in items:
            if k1 != k2 and is_sub_list(v1, v2) and k1 in pathes:
                #print("del", k1)
                del pathes[k1]
                del costes[k1]
            if k1 != k2 and is_sub_list(v2, v1) and k2 in pathes:
                #print("del", k2)
                del pathes[k2]
                del costes[k2]
    #print("dedup return:", pathes, costes)
    return pathes, costes

def get_shortest_path(maze, start, end):
    pathes = {}
    costes = {}
    next_stops = get_next_stops(maze, start, prev=None)
    for next_stop in next_stops:
        key = pos_to_str(start, next_stop)
        pathes[key] = [start, next_stop]
        costes[key] = get_cost(pathes[key])
    last_pathes = {}
    while is_path_different(pathes, last_pathes):
        #print("pathes:", pathes)
        #print("last pathes:", last_pathes)
        #input("Next")
        #last_pathes = copy.deepcopy(pathes)
        last_pathes = pathes.copy()
        #tmp_pathes = {}
        #tmp_costes = {}
        ##keys_to_remove = []
        for k, v in last_pathes.items():
            if v[-1] == end:
                continue
            next_stops = get_next_stops(maze, v[-1], v[-2])
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
                pathes, costes = dedup(pathes, costes)

    #print(pathes)
    #print(costes[pos_to_str(start, end)] - 1)
    return costes[pos_to_str(start, end)] - 1
    #print_trace(maze, pathes[pos_to_str(start, end)])

def run_parallel(maze, start, end, walls):
    pool = multiprocessing.Pool()
    results = []
    for i in range(len(walls)):
        print("fork ", i+1, "/", len(walls), sep='')
        maze_copy = copy.deepcopy(maze)
        maze_copy[walls[i][0]][walls[i][1]] = '.'
        result = pool.apply_async(get_shortest_path, (maze_copy, start, end,))
        results.append(result)

    pool.close()
    pool.join()

    return [result.get() for result in results]

def q1(maze, start, end, walls):
    base = get_shortest_path(maze, start, end)
    print("base:", base)
    #new_pathes = run_parallel(maze, start, end, walls)
    new_pathes = []
    for i in range(len(walls)):
        print("Progress: ", i+1, "/", len(walls), sep='')
        maze_copy = copy.deepcopy(maze)
        #maze_copy = maze.copy()
        maze_copy[walls[i][0]][walls[i][1]] = '.'
        #print("Removed ", wall)
        new_path = get_shortest_path(maze_copy, start, end)
        print("Progress: ", i+1, "/", len(walls), "(", new_path, ")", sep='')
    #    if base - new_path >= 0:
    #        new_pathes.append(new_path)
    #new_pathes.sort()
    #print(new_pathes)
    x = []
    for new_path in new_pathes:
        if base - new_pathes >= 100:
            x.append(new_path)
    print(len(x))
    
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

def get_start_end(maze):
    start = (0, 0)
    end = (0, 0)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'E':
                end = (i, j)
    return start, end

def is_removable_wall(maze, pos):
    p1 = (pos[0], pos[1]+1)
    p2 = (pos[0], pos[1]-1)
    p3 = (pos[0]+1, pos[1])
    p4 = (pos[0]-1, pos[1])
    if is_inside(maze, p1) and is_inside(maze, p2) and maze[p1[0]][p1[1]] == '.' and maze[p2[0]][p2[1]] == '.':
        return True
    if is_inside(maze, p3) and is_inside(maze, p4) and maze[p3[0]][p3[1]] == '.' and maze[p4[0]][p4[1]] == '.':
        return True
    return False

def get_removable_walls(maze):
    walls = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '#' and is_removable_wall(maze, (i, j)):
                walls.append((i, j))
    return walls

if __name__ == '__main__':
    with open("./input.txt", "r") as file:
        maze = []
        start = (0, 0)
        end = (0, 0)
        walls = []
        for line in file:
            line = line.strip()
            w = list(line)
            maze.append(w)
        start, end = get_start_end(maze)
        maze[start[0]][start[1]] = '.'
        maze[end[0]][end[1]] = '.'
        walls = get_removable_walls(maze)
        q1(maze, start, end, walls)
