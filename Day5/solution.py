import re

def is_correct_list(page_map, l):
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if j < i:
                if l[i] in page_map and l[j] in page_map[l[i]]:
                    return False
            if i < j:
                if l[j] in page_map and l[i] in page_map[l[j]]:
                    return False
    return True

def q1(page_map, page_list):
    sum = 0
    for l in page_list:
        if is_correct_list(page_map, l):
            sum += int(l[int(len(l)/2)])
    print(sum)

def fix_wrong_list(page_map, l):
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if j < i:
                if l[i] in page_map and l[j] in page_map[l[i]]:
                    lcopy = l.copy()
                    del lcopy[i]
                    lcopy.insert(j, l[i])
                    return lcopy
            if i < j:
                if l[j] in page_map and l[i] in page_map[l[j]]:
                    lcopy = l.copy()
#                    print(lcopy, i, j)
                    del lcopy[j]
                    lcopy.insert(i, l[j])
                    return lcopy
    print("ERROR")
    

def q2(page_map, page_list):
    sum = 0
    for l in page_list:
        if is_correct_list(page_map, l):
            continue
        while not is_correct_list(page_map, l):
            l = fix_wrong_list(page_map, l)
        sum += int(l[int(len(l)/2)])
    print(sum)

with open("./input.txt", "r") as file:
    page_map = {}
    page_list = []
    rule_mode = True
    for line in file:
        line = line.strip()
        if rule_mode == True:
            if line != "": 
                pages = line.split("|")
                if pages[0] not in page_map:
                    page_map[pages[0]] = [pages[1]]
                else:
                    page_map[pages[0]].append(pages[1])
            else:
                rule_mode = False
        else:
            page_list.append(line.split(","))
    #print(page_map)
    #print("="*100)
    #print(page_list)
    q2(page_map, page_list)