import re
import copy

def expand(input_list):
    mode = 0
    ret = ""
    id = 0
    id_map = {}
    space_map = {}
    for char in input_list:
        if mode == 0:
            id_map[id] = int(char)
        else:
            space_map[id] = int(char)
            id += 1
        mode += 1
        mode %= 2
    #print(id_map)
    #print(space_map)
    return id_map, space_map

def fill_space(expanded):
    pass

def get_check_sum(id_map, space_map):
    max_id = max(id_map.keys())
    tail_id = max_id
    #print(max_id)
    sum = 0
    file_id = 0
    for block_id in range(max_id + 1):
        for diff in range(id_map[block_id]):
           sum += (block_id * (file_id + diff))
        if block_id == tail_id:
            return sum
        file_id += id_map[block_id]
        if block_id in space_map:
            while space_map[block_id] > 0:
                sum += tail_id * file_id
                file_id += 1
                id_map[tail_id] -= 1
                if id_map[tail_id] == 0:
                    tail_id -= 1
                space_map[block_id] -= 1
    return sum

def get_check_sum_q2(id_map, space_map):
    space_map_copy = copy.deepcopy(space_map)
    fill_map = {}
    max_id = max(id_map.keys())
    search_id = max_id
    space_id = 0
    while search_id > 0:
        #print("search", search_id)
        space_id = 0
        while search_id > space_id:
            if space_id in space_map_copy:
                #print(id_map[search_id], space_map_copy[space_id])
                if id_map[search_id] <= space_map_copy[space_id]:
                    for i in range(id_map[search_id]):
                        if space_id in fill_map:
                            fill_map[space_id].append(search_id)
                        else:
                            fill_map[space_id] = [search_id]
                        if search_id - 1 in space_map:
                            space_map_copy[search_id - 1] += 1
                        else:
                            space_map_copy[search_id - 1] = 1
                    space_map_copy[space_id] -= id_map[search_id]
                    id_map[search_id] = 0
                    #del(id_map[search_id])
                    #print("found", search_id + 1)
                    break
                else:
                    space_id += 1
            else:
                space_id += 1
        search_id -= 1
    #print("id_map:", id_map)
    #print("space_map_copy:", space_map_copy)
    #print("fill_map:", fill_map)
    
    max_id = max(id_map.keys())
    file_id = 0
    sum = 0
    for i in range(max_id + 1):
        if i in id_map:
            for diff in range(id_map[i]):
                #print("file_id:", file_id+diff, "value:", i)
                sum += ((file_id + diff) * i)
            file_id += id_map[i]
        if i in fill_map:
            for mf in fill_map[i]:
                #print("file_id:", file_id, "value:", mf)
                sum += (file_id * mf)
                file_id += 1
            #file_id += space_map_copy[i]
        if i in space_map_copy:
            file_id += space_map_copy[i]
    return sum
                
        
    

def q1(input_list):
    id_map, space_map = expand(input_list)
    sum = get_check_sum(id_map, space_map)
    print(sum)
    
def q2(input_list):
    id_map, space_map = expand(input_list)
    sum = get_check_sum_q2(id_map, space_map)
    print(sum)

with open("./input.txt", "r") as file:
    input_list = []
    for line in file:
        line = line.strip()
        input_list = list(line)
    q2(input_list)