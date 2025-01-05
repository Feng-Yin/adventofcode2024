import re

list1 = []

def q1(list1):
    sum = 0
    for line in list1:
        exps = re.findall(r'mul\(\d+\,\d+\)', line)
        for exp in exps:
            nums = re.findall(r'\d+', exp)
            sum += int(nums[0]) * int(nums[1]) 
    print(sum)

def q2(list1):
    sum = 0
    new_list = []
    new_str = ""
    for line in list1:
        new_str += line
    new_line = ""
    while new_line != new_str:
        if new_line == "":
            new_line = new_str
        else:
            new_str = new_line
        new_line = re.sub(r'don\'t\(\).*?do\(\)', "", new_str) 
    new_line = re.split(r'don\'t\(\)', new_line)
    new_list.append(new_line[0])
    q1(new_list)
    


with open("./input.txt", "r") as file:
    for line in file:
        line = line.strip()
        list1.append(line)
    q2(list1)
