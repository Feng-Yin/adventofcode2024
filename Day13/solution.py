import re
import copy

def print_input(input_data):
    pass

def q1(data):
    cost = 0
    for ax, ay, bx, by, x, y in data:
        an = x*by - y*bx
        ad = ax*by - ay*bx
        
        bn = x*ay - y*ax
        bd = bx*ay - by*ax
        
        if an%ad == 0 and bn%bd == 0:
            a = int(an/ad)
            b = int(bn/bd)
            cost += (a*3 + b)
    print(cost)
    

def q2(data):
    cost = 0
    for ax, ay, bx, by, x, y in data:
        x += 10000000000000
        y += 10000000000000
        an = x*by - y*bx
        ad = ax*by - ay*bx
        
        bn = x*ay - y*ax
        bd = bx*ay - by*ax
        
        if an%ad == 0 and bn%bd == 0:
            a = int(an/ad)
            b = int(bn/bd)
            cost += (a*3 + b)
    print(cost)

with open("./input.txt", "r") as file:
    data = []
    ##int ax, ay, bx, by, x, y
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("Button A: "):
            line.replace("Button A: ", "")
            l = line.split(',')
            ax = int(l[0].split('+')[1])
            ay = int(l[1].split('+')[1])
            continue
        if line.startswith("Button B: "):
            line.replace("Button B: ", "")
            l = line.split(',')
            bx = int(l[0].split('+')[1])
            by = int(l[1].split('+')[1])
            continue
        if line.startswith("Prize: "):
            line.replace("Prize: ", "")
            l = line.split(',')
            x = int(l[0].split('=')[1])
            y = int(l[1].split('=')[1])
            data.append((ax, ay, bx, by, x, y))
    q2(data)