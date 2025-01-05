import re
import copy

def calculate(input_map, ic):
    if ic[1] == "OR":
        if input_map[ic[0]] == 1 or input_map[ic[2]] == 1:
            return 1
        else:
            return 0
    if ic[1] == "AND":
        if input_map[ic[0]] == 0 or input_map[ic[2]] == 0:
            return 0
        else:
            return 1
    if ic[1] == "XOR":
        if input_map[ic[0]] == input_map[ic[2]]:
            return 0
        else:
            return 1

def q1(input_map, ics):
    next_ics = ics
    while len(next_ics) > 0:
        ics = next_ics
        next_ics = []
        for i in range(len(ics)):
            if ics[i][0] in input_map and ics[i][2] in input_map:
                input_map[ics[i][3]] = calculate(input_map, ics[i])
            else:
                next_ics.append(ics[i].copy())
    zk = []
    for k in input_map.keys():
        if 'z' in k:
            zk.append(k)
    zk.sort(reverse=True)
    r = 0
    for k in zk:
        r = r * 2 + input_map[k]
    print(r) 

def q2(input_map, ics):
    for i in ics:
        if "AND" == i[1]:
            print(" ".join(i))

with open("./input1.txt", "r") as file:
    input_map = {}
    ic = []
    part1 = True
    for line in file:
        line = line.strip()
        if len(line) == 0:
            part1 = False
            continue
        if part1:
            ar = line.split(':')
            input_map[ar[0]] = int(ar[1])
        else:
            line = line.replace(" -> ", " ")
            ar = line.split()
            ic.append(ar)
    #print(input_map)
    #print(ic)
    q1(input_map, ic)
