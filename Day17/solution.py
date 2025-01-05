import re
import copy
import numpy as np

def get_combo_operand(operand, registers):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']

def adv(operand, registers):
    operand = get_combo_operand(operand, registers)
    registers['A'] = int(registers['A']/pow(2, operand))
    return registers

def bdv(operand, registers):
    operand = get_combo_operand(operand, registers)
    registers['B'] = int(registers['A']/pow(2, operand))
    return registers

def cdv(operand, registers):
    operand = get_combo_operand(operand, registers)
    registers['C'] = int(registers['A']/pow(2, operand))
    return registers

def bxl(operand, registers):
    a1 = np.array([operand], dtype=np.int64)
    a2 = np.array([registers['B']], dtype=np.int64)
    result = np.bitwise_xor(a1, a2)
    registers['B'] = int(result[0])
    return registers

def bst(operand, registers):
    operand = get_combo_operand(operand, registers)
    registers['B'] = operand % 8
    return registers

def jnz(operand, registers):
    if registers['A'] == 0:
        return -1
    return operand

def bxc(registers):
    a1 = np.array([registers['B']], dtype=np.int64)
    a2 = np.array([registers['C']], dtype=np.int64)
    result = np.bitwise_xor(a1, a2)
    registers['B'] = int(result[0])
    return registers

def out(operand, registers):
    operand = get_combo_operand(operand, registers)
    return str(operand % 8)

def run_cmd(opcode, operand, registers):
    #print("Run1:", opcode, operand, registers)
    new_pi = -1
    output = ""
    if opcode == 0:
        registers = adv(operand, registers)
    if opcode == 1:
        registers = bxl(operand, registers)
    if opcode == 2:
        registers = bst(operand, registers)
    if opcode == 3:
        new_pi = jnz(operand, registers)
    if opcode == 4:
        registers = bxc(registers)
    if opcode == 5:
        output = out(operand, registers)
    if opcode == 6:
        registers = bdv(operand, registers)
    if opcode == 7:
        registers = cdv(operand, registers)
    
    return new_pi, registers, output

def run_program(prog, registers):
    pi = 0
    outputs = []
    while pi < len(prog):
        opcode = prog[pi]
        pi += 1
        operand = prog[pi]
        pi += 1
        new_pi, registers, output = run_cmd(opcode, operand, registers)
        if new_pi >= 0:
            pi = new_pi
        if output != "":
            outputs.append(output)
    return [int(ch) for ch in outputs]

def q1(prog, registers):
    outputs = run_program(prog, registers)
    print(",".join([str(i) for i in outputs]))
    
def q2(prog, registers):
    outputs = []
    #registers['A'] = 35747063728283
    registers['A'] = 105690648086683
    #inc = [2097152]#,68717379584,2097152,1030790053888]
    inc = [255,1383,8,23185]#,2072321]
    counter = 0
    while outputs != prog:
        r_copy = registers.copy()
        outputs = run_program(prog, r_copy)
        #print("A:", registers['A'], "Output:", outputs, len(outputs), "want:", prog, len(prog))
        #break
        registers['A'] -= inc[counter%len(inc)]
        #registers['A'] += sum(inc)
        #registers['A'] += 1
        counter += 1
    print(registers)


with open("./input.txt", "r") as file:
    prog = []
    registers = {}
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if "Register A: " in line:
            registers['A'] = int(line.replace("Register A: ", ""))
        if "Register B: " in line:
            registers['B'] = int(line.replace("Register B: ", ""))
        if "Register C: " in line:
            registers['C'] = int(line.replace("Register C: ", ""))
        if "Program: " in line:
            line = line.replace("Program: ", "")
            l = line.split(',')
            prog = [int(ch) for ch in l]
    q2(prog, registers)