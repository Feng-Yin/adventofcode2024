#​
import re
import copy

def is_inside(maze, node):
    r_max = len(maze) - 1
    c_max = len(maze[0]) - 1
    if node[0] < 0 or node[0] > r_max:
        return False
    if node[1] < 0 or node[1] > c_max:
        return False
    return True

def get_antinodes_v2(maze, antenna_list):
    antinodes = []
    for i in range(len(antenna_list) - 1):
        for j in range(i+1, len(antenna_list)):
            cont = True
            count = 1
            while cont:
                node1 = (antenna_list[j][0] + (antenna_list[j][0] - antenna_list[i][0]) * count, antenna_list[j][1] + (antenna_list[j][1] - antenna_list[i][1]) * count)
                if is_inside(maze, node1):
                    antinodes.append(node1)
                    count += 1
                else:
                    cont = False
            cont = True
            count = 1
            while cont:
                node2 = (antenna_list[i][0] + (antenna_list[i][0] - antenna_list[j][0]) * count, antenna_list[i][1] + (antenna_list[i][1] - antenna_list[j][1]) * count)
                if is_inside(maze, node2):
                    antinodes.append(node2)
                    count += 1
                else:
                    cont = False
    return antinodes

def get_antinodes(maze, antenna_list):
    antinodes = []
    for i in range(len(antenna_list) - 1):
        for j in range(i+1, len(antenna_list)):
            node1 = (antenna_list[j][0] + (antenna_list[j][0] - antenna_list[i][0]), antenna_list[j][1] + (antenna_list[j][1] - antenna_list[i][1]))
            node2 = (antenna_list[i][0] + (antenna_list[i][0] - antenna_list[j][0]), antenna_list[i][1] + (antenna_list[i][1] - antenna_list[j][1]))
            if is_inside(maze, node1):
                antinodes.append(node1)
            if is_inside(maze, node2):
                antinodes.append(node2)
    #print(antinodes)
    return antinodes
            

def q1(maze, antenna_map):
    count = 0
    result = []
    for k, v in antenna_map.items():
        result.extend(get_antinodes(maze, v))
    print(len(set(result)))
    
def q2(maze, antenna_map):
    count = 0
    anteena_count = 0
    result = []
    for k, v in antenna_map.items():
        result.extend(get_antinodes_v2(maze, v))
        anteena_count += len(v)
        result.extend(v)
    print(len(set(result)))

with open("./input.txt", "r") as file:
    antenna_map = {}
    maze = []
    ri = 0
    for line in file:
        line = line.strip()
        row = list(line)
        maze.append(row)
        for i in range(len(row)):
            if row[i] != '.': 
                if row[i] in antenna_map:
                    antenna_map[row[i]].append((ri, i))
                else:
                    antenna_map[row[i]] = [(ri, i)]
        ri += 1
    #print(maze)
    #print(antenna_map)
    q2(maze, antenna_map)