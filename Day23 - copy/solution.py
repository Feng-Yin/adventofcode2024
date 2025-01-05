import re
import copy

def q1(data, key_set):
    ret = set()
    for d in data:
        tmp = d.split('-')
        d1 = tmp[0]
        d2 = tmp[1]
        need_t = (not str.startswith(d1, 't')) and (not str.startswith(d2, 't'))
        for k in key_set:
            if need_t and (not str.startswith(k, 't')):
                continue
            if ('-'.join([k, d1]) in data or '-'.join([d1, k]) in data) and ('-'.join([k, d2]) in data or '-'.join([d2, k]) in data):
                r = [d1, d2, k]
                r.sort()
                ret.add(','.join(r))
    #print(ret)
    print(len(ret))
    return ret
    
def want_t(ar):
    for p in ar:
        if str.startswith(p, 't'):
            return False
    return True
def is_connected(k, ar, data):
    for f in ar:
        if ('-'.join([f, k]) not in data) and ('-'.join([k, f]) not in data):
            return False
    return True

def three_group(data, key_set):
    ret = set()
    for d in data:
        tmp = d.split('-')
        d1 = tmp[0]
        d2 = tmp[1]
        for k in key_set:
            if ('-'.join([k, d1]) in data or '-'.join([d1, k]) in data) and ('-'.join([k, d2]) in data or '-'.join([d2, k]) in data):
                r = [d1, d2, k]
                r.sort()
                ret.add(','.join(r))
    #print(ret)
    print(len(ret))
    return ret

def q2(data, key_set):
    current_set = set()
    next_set = three_group(data, key_set)
    key_set_copy = set()
    tmp_key_set = key_set.copy()
    while len(next_set) > 0:
        for i in next_set:
            print("current party size:", i.count(',') + 1, "total:", len(next_set), "e.g:", i)
            break
        key_set_copy = tmp_key_set
        tmp_key_set = set()
        current_set = next_set
        next_set = set()
        for s in current_set:
            ar = s.split(',')
            #needs_t = want_t(ar)
            for k in key_set_copy:
                if k in ar:
                    continue
                #if needs_t and (not str.startswith(k, 't')):
                #    continue
                if not is_connected(k, ar, data):
                    continue
                arc = ar.copy()
                arc.append(k)
                arc.sort()
                next_set.add(','.join(arc))
                tmp_key_set.add(k)
    print(current_set)

with open("./input1.txt", "r") as file:
    data = []
    key_set = set()
    for line in file:
        line = line.strip()
        data.append(line)
        keys = line.split('-')
        key_set.add(keys[0])
        key_set.add(keys[1])
    q2(data, key_set)

