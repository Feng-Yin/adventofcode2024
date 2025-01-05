import re
import copy

def print_input(input_data):
    for row in input_data:
        print(row)

def find_all_starts(maze):
    ret = []
    for ri in range(len(maze)):
        ret.extend([(ri, index) for index, value in enumerate(maze[ri]) if value == 0])
    return ret

def is_in_maze(maze, point):
    if point[0] < 0 or point[0] >= len(maze):
        return False
    if point[1] < 0 or point[1] >= len(maze[0]):
        return False
    return True

def matches_value(maze, point, value):
    return maze[point[0]][point[1]] == value

def find_all_pathes(maze, start):
    pathes = [[start]]
    next_step = 1
    pathes_temp = []
    while next_step <= 9:
        pathes_temp = []
        cont = False
        for path in pathes:
            last_stop = path[-1]
            next_stop1 = (last_stop[0] - 1, last_stop[1])
            next_stop2 = (last_stop[0] + 1, last_stop[1])
            next_stop3 = (last_stop[0], last_stop[1] - 1)
            next_stop4 = (last_stop[0], last_stop[1] + 1)
            for next_stop in [next_stop1, next_stop2, next_stop3, next_stop4]:
                if is_in_maze(maze, next_stop) and matches_value(maze, next_stop, next_step):
                    path_copy = copy.deepcopy(path)
                    path_copy.append(next_stop)
                    pathes_temp.append(path_copy)
                    cont = True
        pathes = pathes_temp
        pathes_temp = []
        if cont == True:
            next_step += 1
        else:
            return []
    return pathes

def q1(maze):
    start_points = find_all_starts(maze)
    sum = 0
    for start in start_points:
        pathes = find_all_pathes(maze, start)
        l = [path[-1] for path in pathes]
        #print(len(set(l)))
        sum += len(set(l))
    print(sum)
    
def get_path_key(path):
    return str(path[0]) + str(path[-1])
    
def q2(maze):
    start_points = find_all_starts(maze)
    sum = 0
    path_rating = {}
    for start in start_points:
        pathes = find_all_pathes(maze, start)
        for path in pathes:
            key = get_path_key(path)
            if key in path_rating:
                path_rating[key] += 1
            else:
                path_rating[key] = 1
                
    print(path_rating)
    for k, v in path_rating.items():
        sum += v
    print(sum)

with open("./input.txt", "r") as file:
    maze = []
    for line in file:
        line = line.strip()
        row = list(line)
        maze.append([int(ch) for ch in row])
    #print_input(maze)
    q2(maze)