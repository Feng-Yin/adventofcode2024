import re
import copy

def get_ops(row):
    formular = row[1:]
    num_opers = len(formular) - 1
    ops = []
    for v in range(pow(2, num_opers)):
        op = []
        for i in range(num_opers):
            if v % 2 == 0:
                op.append('+')
            else:
                op.append('*')
            v = int(v / 2)
        ops.append(op)
    return ops

def is_doable(row, ops):
    result = row[0]
    formular = row[1:]
    for op in ops:
        v = formular[0]
        for i in range(len(op)):
            if op[i] == '+':
                v += formular[i+1]
            if op[i] == '*':
                v *= formular[i+1]
            if op[i] == "||":
                v = int(str(v) + str(formular[i+1]))
            if v > result:
                break
        if v == result:
            return True
    return False

def is_doable_v2(row, ops):
    result = row[0]
    formular = row[1:]
    lcount = 0
    for op in ops:
        v = formular[0]
        for i in range(len(op)):
            if op[i] == '+':
                v += formular[i+1]
            if op[i] == '*':
                v *= formular[i+1]
            if op[i] == "||":
                v = int(str(v) + str(formular[i+1]))
            if v > result:
                lcount += 1
                break
        if v == result:
            return True, False
    if lcount >= len(ops):
        return False, True
    return False, False
    
    
def get_q2_ops(q1_ops):
    result = []
    for i in range(len(q1_ops)):
        for v in range(pow(2, len(q1_ops[i]))):
            new_op = q1_ops[i].copy()
            for id in range(len(new_op)):
                if v % 2 == 1:
                    new_op[id] = "||"
                v = int(v / 2)
            if new_op.count("||") > 0 and new_op not in result:
                print(new_op)
                result.append(new_op)
    return result

def get_new_ops(op, num_or):
    ops = []
    for i in range(len(op)):
        if op[i] != "||":
            opcopy = op.copy()
            opcopy[i] = "||"
            ops.append(opcopy)
    num_or -= 1
    if num_or == 0:
        return ops
    else:
        re = []
        for v in ops:
            re.extend(get_new_ops(v, num_or))
        return re

def q1(quze):
    sum = 0
    count = 0
    for row in quze:
        result = row[0]
        count += 1
        print("progress:", count, "/", len(quze))
        if is_doable(row, get_ops(row)):
            sum += result
    print(sum)

def q2(quze):
    sum = 0
    count = 0
    for row in quze:
        result = row[0]
        count += 1
        print("progress:", count, "/", len(quze))
        org_ops = get_ops(row)
        if is_doable(row, org_ops):
            sum += result
        else:
            done = False
            for op in org_ops:
                for num_or in range(1, len(op)+1):
                    new_ops = get_new_ops(op, num_or)
                    #print(row)
                    #print(new_ops)
                    #if num_or > 2:
                    #    exit(0)
                    res, skip = is_doable_v2(row, new_ops)
                    if res == True:
                        sum += result
                        done = True
                        break
                    if skip == True:
                        print("hit skip")
                        break
                if done == True:
                    break
    print(sum)

with open("./input.txt", "r") as file:
    quze = []
    for line in file:
        line = line.strip()
        inputs = line.split(':')
        result = int(inputs[0])
        factors = inputs[1].strip().split()
        tmp = [result]
        for v in factors:
            tmp.append(int(v))
        quze.append(tmp)
    q2(quze)