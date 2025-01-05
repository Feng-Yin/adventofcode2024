import re
import copy

maze_map = []
guard_pos = (-1, -1)
guard_dir = 0 # from 0: up, right, down and left

def get_next_pos():
    if guard_dir == 0:
        return (guard_pos[0] - 1, guard_pos[1])
    if guard_dir == 1:
        return (guard_pos[0], guard_pos[1] + 1)
    if guard_dir == 2:
        return (guard_pos[0] + 1, guard_pos[1])
    if guard_dir == 3:
        return (guard_pos[0], guard_pos[1] - 1)

def is_in_map(new_pos):
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(maze_map) or new_pos[1] >= len(maze_map[0]):
        return False
    return True

def is_allowed(new_pos):
    if maze_map[new_pos[0]][new_pos[1]] == '#':
        return False
    return True

def count_x_place():
    count = 0
    for row in maze_map:
        count += row.count('X')
    return count

def q1():
    global guard_pos
    global guard_dir
    new_pos = get_next_pos()
    while is_in_map(new_pos):
        if is_allowed(new_pos):
            maze_map[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = new_pos
            maze_map[guard_pos[0]][guard_pos[1]] = 'X'
        else:
            guard_dir = (guard_dir + 1) % 4
        new_pos = get_next_pos()
    print(count_x_place())

def get_all_obs_candidate():
    candidates = []
    global guard_pos
    global guard_dir
    new_pos = get_next_pos()
    while is_in_map(new_pos):
        if is_allowed(new_pos):
            maze_map[guard_pos[0]][guard_pos[1]] = 'X'
            #candidates.append((guard_pos[0], guard_pos[1]))
            guard_pos = new_pos
            maze_map[guard_pos[0]][guard_pos[1]] = 'X'
            #candidates.append((guard_pos[0], guard_pos[1]))
        else:
            guard_dir = (guard_dir + 1) % 4
        new_pos = get_next_pos()
    for i in range(0, len(maze_map)):
        for j in range(0, len(maze_map[0])):
            if maze_map[i][j] == 'X':
                candidates.append((i, j))
    return candidates

def is_valid_obs(pair):
    global maze_map
    maze_map[pair[0]][pair[1]] = '#'
    global guard_pos
    global guard_dir
    travel_path = []
    travel_path.append((guard_pos[0], guard_pos[1], guard_dir))
    new_pos = get_next_pos()
    while is_in_map(new_pos):
        if is_allowed(new_pos):
            guard_pos = new_pos
        else:
            guard_dir = (guard_dir + 1) % 4
        if (guard_pos[0], guard_pos[1], guard_dir) in travel_path:
            #print(travel_path)
            #print(guard_pos[0], guard_pos[1], guard_dir)
            return True
        else:
            travel_path.append((guard_pos[0], guard_pos[1], guard_dir))
        new_pos = get_next_pos()
    return False
    
    

def q2():
    global guard_pos
    global guard_dir
    global maze_map
    saved_pos = guard_pos
    saved_dir = guard_dir
    #saved_map = maze_map.copy()
    saved_map = copy.deepcopy(maze_map)
    cans = get_all_obs_candidate()
    print(len(cans))

    count = 0
    progress = 0
    for pair in cans:
        progress += 1
        print("progress: ", progress/len(cans)*100, "%")
        guard_pos = saved_pos
        guard_dir = saved_dir
        maze_map = copy.deepcopy(saved_map)
        if pair == saved_pos:
            continue 
        if is_valid_obs(pair):
            count += 1
            #print(pair)
    print(count)

with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        row = list(line)
        maze_map.append(row)
        if '^' in row:
            guard_pos = (len(maze_map) - 1, row.index('^'))
    #print(maze_map)
    ##print(guard_pos[0], guard_pos[1])
    q2()
    #for row in maze_map:
    #    print(row)
