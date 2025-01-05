import re
import copy
import sys
import time

def print_input(input_data):
    pass

def q1(robots, time, width, height):
    final_robots = []
    for rx, ry, vx, vy in robots:
        fx = (rx + time * vx) % width
        fy = (ry + time * vy) % height
        final_robots.append((fx, fy))
    #print(final_robots)
    width -= 1
    height -= 1
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    for x, y in final_robots:
        if x < width/2 and y < height/2:
            #print("f1:", x, y)
            f1 += 1
        if x > width/2 and y < height/2:
            #print("f2:", x, y)
            f2 += 1
        if x < width/2 and y > height/2:
            #print("f3:", x, y)
            f3 += 1
        if x > width/2 and y > height/2:
            #print("f4:", x, y)
            f4 += 1
    #print(f1, f2, f3, f4)
    print(f1*f2*f3*f4)
            
def is_a_tree(final_robots):
    min_y = 999
    for x, y in final_robots:
        if y < min_y:
            min_y = y
    tops = []
    for x, y in final_robots:
        if y == min_y:
            tops.append((x, y))
    check_levels = 2
    for tx, ty in tops:
        ret = True
        for i in range(1, check_levels + 1):
            tl = (tx - i, ty + i)
            tr = (tx + i, ty + i)
            if tl not in final_robots or tr not in final_robots:
                ret = False
                break
    return ret

def is_a_tree_v2(final_robots, width, height):
    for j in range(height):
        row = []
        for i in range(width):
            if (i, j) in final_robots:
                row.append('*')
            else:
                row.append('.')
        rs = ''.join(row)
        if "*********" in rs:
            return True
    return False

def print_robot(final_robots, width, height):
    width -= 10
    for j in range(height):
        for i in range(width):
            if (i, j) in final_robots:
                #print('*', end='')
                sys.stdout.write('*')
            else:
                #print('.', end='')
                sys.stdout.write('.')
        #print("")
        sys.stdout.write("\r")
        #sys.stdout.flush()
        #return
    sys.stdout.flush()
            

def q2(robots, time, width, height):
    for i in range(time):
        final_robots = []
        print_robots = []
        if i > 0 and (i*100) % time == 0:
            print("Progress:", i/time*100, "%")
        for rx, ry, vx, vy in robots:
            fx = (rx + vx) % width
            fy = (ry + vy) % height
            final_robots.append((fx, fy, vx, vy))
            print_robots.append((fx, fy))
        #print(width, height)
        #print_robot(print_robots, width, height)
        #print("#" * (width - 10))
        if is_a_tree_v2(print_robots, width, height):
            print(i)
            print_robot(print_robots, width, height)
            return
        robots = final_robots


with open("./input.txt", "r") as file:
    width = 0
    height = 0
    robots = []
    for line in file:
        line = line.strip()
        data = line.split(" v=")
        pos = data[0].replace("p=", "")
        pos = pos.split(',')
        rx = int(pos[0])
        ry = int(pos[1])
        v = data[1].split(',')
        vx = int(v[0])
        vy = int(v[1])
        width = max(width, rx + 1)
        height = max(height, ry + 1)
        robots.append((rx, ry, vx, vy))
    #print(robots, width, height)
    q2(robots, 10000, width, height)