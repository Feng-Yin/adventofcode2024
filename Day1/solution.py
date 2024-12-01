import re

list1 = []
list2 = []


def q1(list1, list2):
    dist = 0
    for v1, v2 in zip(list1, list2):
        dist += abs(v1 - v2)
    print(dist)


def q2(list1, list2):
    rep_map = {}
    for v in list2:
        if v in rep_map:
            rep_map[v] = rep_map[v] + 1
        else:
            rep_map[v] = 1
    sim = 0
    for v in list1:
        if v in rep_map:
            sim += v * rep_map[v]
    print(sim)


with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        pair = line.split()
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
    list1.sort()
    list2.sort()

    q2(list1, list2)
