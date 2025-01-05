import re

list1 = [[]]

def is_safe(vs):
    if len(vs) < 2:
        return False
    is_inc = True if vs[0] < vs[1] else False
    for i in range(len(vs) - 1):
        if vs[i] == vs[i + 1]:
            return False
        is_inc_tmp = True if vs[i] < vs[i + 1] else False
        if is_inc != is_inc_tmp:
            return False
        if abs(vs[i+1] - vs[i]) > 3:
            return False
    return True

def is_safe2(vs):
    if is_safe(vs):
        return True
    for i in range(len(vs) - 1):
        if is_safe(vs[:i] + vs[i+1:]):
            return True
    if is_safe(vs[:len(vs) - 1]):
        return True
    return False    

def q1(list1):
    count = 0
    for vs in list1:
        if is_safe(vs):
            count += 1
    print(count)

def q2(list1):
    count = 0
    for vs in list1:
        if is_safe2(vs):
            count += 1
    print(count)

with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        steps = line.split()
        l = []
        for v in steps:
            l.append(int(v))
        #print(l)
        list1.append(l)
    q2(list1)
