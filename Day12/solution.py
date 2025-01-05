import re
import copy

def print_input(maze, region_map):
    for row in maze:
        print(row)
    for k, v in region_map.items():
        print(k, v)

def is_connected(zone, pos):
    for p in zone:
        if abs(p[0] - pos[0]) + abs(p[1] - pos[1]) == 1:
            return True
    return False

def processed(zoned_regions, pos):
    for zone in zoned_regions:
        for p in zone:
            if p == pos:
                return True
    return False

def has_connected(l, new_zone):
    has_new = False
    for p in l:
        if p not in new_zone and is_connected(new_zone, p):
            new_zone.append(p)
            has_new = True
    return has_new, new_zone

def get_zoned_regions(l):
    zoned_regions = []
    for pos in l:
        if processed(zoned_regions, pos):
            continue
        new_zone = [pos]
        has_new, new_zone = has_connected(l, new_zone)
        while has_new:
            has_new, new_zone = has_connected(l, new_zone)
        zoned_regions.append(new_zone)
    return zoned_regions

def is_inside(maze, p):
    if p[0] < 0 or p[0] >= len(maze):
        return False
    if p[1] < 0 or p[1] >= len(maze[0]):
        return False
    return True
    
def get_primier(maze, zone):
    zone_ch = maze[zone[0][0]][zone[0][1]]
    primier = 0
    for p in zone:
        p1 = (p[0]-1, p[1])
        p2 = (p[0]+1, p[1])
        p3 = (p[0], p[1]-1)
        p4 = (p[0], p[1]+1)
        for np in [p1, p2, p3, p4]:
            #print(zone_ch, np, is_inside(maze, np), maze[np[0]][np[1]])
            if (not is_inside(maze, np)) or (maze[np[0]][np[1]] != zone_ch):
                primier += 1
    return primier

def get_sides(maze, zone):
    zone_ch = maze[zone[0][0]][zone[0][1]]
    
    # up primier
    up_primier = []
    for p in zone:
        p1 = (p[0]-1, p[1])
        if (not is_inside(maze, p1)) or (maze[p1[0]][p1[1]] != zone_ch):
            up_primier.append(p1)
    # down primier
    down_primier = []
    for p in zone:
        p1 = (p[0]+1, p[1])
        if (not is_inside(maze, p1)) or (maze[p1[0]][p1[1]] != zone_ch):
            down_primier.append(p1)
    # left primier
    left_primier = []
    for p in zone:
        p1 = (p[0], p[1]-1)
        if (not is_inside(maze, p1)) or (maze[p1[0]][p1[1]] != zone_ch):
            left_primier.append(p1)
    # right primier
    right_primier = []
    for p in zone:
        p1 = (p[0], p[1]+1)
        if (not is_inside(maze, p1)) or (maze[p1[0]][p1[1]] != zone_ch):
            right_primier.append(p1)
    
    zoned_up_primier = get_zoned_regions(up_primier)
    zoned_down_primier = get_zoned_regions(down_primier)
    zoned_left_primier = get_zoned_regions(left_primier)
    zoned_right_primier = get_zoned_regions(right_primier)
    
    return len(zoned_up_primier) + len(zoned_down_primier) + len(zoned_left_primier) + len(zoned_right_primier)


def q1(maze, region_map):
    zoned_region_map = {}
    for k, v in region_map.items():
        zoned = get_zoned_regions(v)
        zoned_region_map[k] = zoned
    #print(zoned_region_map['C'])
    total_price = 0
    for k, v in zoned_region_map.items():
        for zone in v:
            area = len(zone)
            primier = get_primier(maze, zone)
            #print(k, area, primier)
            total_price += (area * primier)
    print(total_price)
    #print(zoned_region_map)
    

def q2(page_map, page_list):
    zoned_region_map = {}
    for k, v in region_map.items():
        zoned = get_zoned_regions(v)
        zoned_region_map[k] = zoned
    #print(zoned_region_map['C'])
    total_price = 0
    for k, v in zoned_region_map.items():
        for zone in v:
            area = len(zone)
            primier = get_sides(maze, zone)
            #print(k, area, primier)
            total_price += (area * primier)
    print(total_price)


with open("./input.txt", "r") as file:
    maze = []
    region_map = {}
    rc = 0
    for line in file:
        line = line.strip()
        row = list(line)
        maze.append(row)
        for ri in range(len(row)):
            if row[ri] in region_map:
                region_map[row[ri]].append((rc, ri))
            else:
                region_map[row[ri]] = [(rc, ri)]
        rc += 1
    q2(maze, region_map)