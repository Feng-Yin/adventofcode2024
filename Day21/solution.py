import re
import copy

def reverse(ar):
    ret = []
    for i in range(len(ar)):
        if ar[len(ar) - i - 1] == '^':
            ret.append('v')
        if ar[len(ar) - i - 1] == 'v':
            ret.append('^')
        if ar[len(ar) - i - 1] == '<':
            ret.append('>')
        if ar[len(ar) - i - 1] == '>':
            ret.append('<')
    return ret

def build_input_map(keys, keys_pos):
    input_map = {}
    for fi in range(len(keys)):
        for ti in range(fi + 1, len(keys)):
            if fi == ti:
                continue
            tmp = []
            #print("From", keys[fi], "to", keys[ti])
            ych = '^'
            if keys_pos[keys[ti]][0] > keys_pos[keys[fi]][0]:
                ych = 'v'
            for i in range(abs(keys_pos[keys[ti]][0] - keys_pos[keys[fi]][0])):
                tmp.append(ych)
            #print(tmp)

            xch = '<'
            if keys_pos[keys[ti]][1] > keys_pos[keys[fi]][1]:
                xch = '>'
            for i in range(abs(keys_pos[keys[ti]][1] - keys_pos[keys[fi]][1])):
                tmp.append(xch)
            #print(tmp)
            input_map[keys[fi]+':'+keys[ti]] = [tmp]
            input_map[keys[ti]+':'+keys[fi]] = [reverse(tmp)]

            if keys[fi] in ['3', '4', '5', '6', '7', '8', '9'] and keys[ti] in ['3', '4', '5', '6', '7', '8', '9']:
                tmp = []
                xch = '<'
                if keys_pos[keys[ti]][1] > keys_pos[keys[fi]][1]:
                    xch = '>'
                for i in range(abs(keys_pos[keys[ti]][1] - keys_pos[keys[fi]][1])):
                    tmp.append(xch)
                ych = '^'
                if keys_pos[keys[ti]][0] > keys_pos[keys[fi]][0]:
                    ych = 'v'
                for i in range(abs(keys_pos[keys[ti]][0] - keys_pos[keys[fi]][0])):
                    tmp.append(ych)
                if tmp not in input_map[keys[fi]+':'+keys[ti]]:
                    input_map[keys[fi]+':'+keys[ti]].append(tmp)
                    input_map[keys[ti]+':'+keys[fi]].append(reverse(tmp))
    return input_map

def get_kb_input(dig_input_map, ar):
    ret = []
    f = 'A'
    for t in ar:
        if f != t:
            if len(ret) == 0:
                for p in dig_input_map[f+':'+t]:
                    path = p.copy()
                    path.append('A')
                    ret.append(path)
            else:
                tp = []
                for ep in ret:
                    for p in dig_input_map[f+':'+t]:
                        path = ep.copy()
                        path.extend(p)
                        path.append('A')
                        tp.append(path)
                ret = copy.deepcopy(tp)
        f = t
    return ret

def q1(data):
    dig_keys = ['A', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    dig_keys_pos = {
        '7':(0,0), '8':(0,1), '9':(0,2),
        '4':(1,0), '5':(1,1), '6':(1,2),
        '1':(2,0), '2':(2,1), '3':(2,2),
        'X':(3,0), '0':(3,1), 'A':(3,2), 
    }
    dig_input_map = build_input_map(dig_keys, dig_keys_pos)
    #print(dig_input_map)
    dir_keys = ['A', '^', '<', 'v', '>']
    dir_keys_pos = {
        'X':(0,0), '^':(0,1), 'A':(0,2),
        '<':(1,0), 'v':(1,1), '>':(1,2), 
    }
    dir_input_map = build_input_map(dir_keys, dir_keys_pos)
    print(dir_input_map)
    r_sum = 0
    for i in data:
        ar = list(i)
        r_inputs = get_kb_input(dig_input_map, ar)
        r = 999999999999
        #print(r_inputs)
        for r_input in r_inputs:
            print(r_input)
            dr_inputs = [r_input]
            for l in range(2):
                dr_inputs = get_kb_input(dir_input_map, dr_inputs[0])
                #print(l+1, "".join(r_input))
            r = min(r, (len(dr_inputs[0]) * int(i[:-1])))
            print(dr_inputs, len(dr_inputs[0]), int(i[:-1]))
        r_sum += r
    print(r_sum)
    
def q2(maze, start, end):
    pass

with open("./input.txt", "r") as file:
    data = []
    for line in file:
        line = line.strip()
        data.append(line)
    q1(data)
