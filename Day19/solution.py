import re
import copy

def get_next_steps(path, puzzle, patterns):
    steps = []
    full_path = "".join(path)
    if len(full_path) < len(puzzle):
        for i in range(len(full_path), len(puzzle)+1):
            #print("Check if", puzzle[len(full_path):i], len(full_path), i, "in", puzzle)
            if puzzle[len(full_path):i] in patterns:
                steps.append(puzzle[len(full_path):i])
    else:
        print("Path", path, "is long enough")
    return steps

def pathes_has_puzzle(pathes, puzzle):
    for path in pathes:
        if "".join(path) == puzzle:
            return True
    return False

def print_progress(pathes):
    for path in pathes:
        print("".join(path))

def print_progress_v2(pathes1, pathes2):
    pass

def is_new_path(path, step, tmp_pathes):
    full_path = "".join(path) + step
    for tmp_path in tmp_pathes:
        if "".join(tmp_path) == full_path:
            return False
    return True

def is_new_path_v2(path, step, tmp_pathes):
    full_path = path.copy()
    full_path.append(step)
    for tmp_path in tmp_pathes:
        if full_path in tmp_path and tmp_path.index(full_path) == 0:
            return False
    return True

def is_possible(puzzle, patterns):
    pathes = []
    steps = get_next_steps([], puzzle, patterns)
    for step in steps:
        pathes.append([step])
    #print("Initial pathes:", pathes)
    while not pathes_has_puzzle(pathes, puzzle):
        #input("Print progress:")
        #print_progress(pathes)
        has_new_path = False
        tmp_pathes = []
        for path in pathes:
            steps = get_next_steps(path, puzzle, patterns)
            #print("Next steps:", steps, "for path: ", path)
            if len(steps) == 0:
                continue
            has_new_path = True
            for step in steps:
                if is_new_path(path, step, tmp_pathes):
                    path_copy = path.copy()
                    path_copy.append(step)
                    if pathes_has_puzzle([path_copy], puzzle):
                        return True 
                    tmp_pathes.append(path_copy)            
        if has_new_path == False:
            return False
        pathes = tmp_pathes
    return True

def has_new_path(old_pathes, new_pathes):
    #print("old_pathes:", old_pathes)
    #print("new_pathes:", new_pathes)
    if len(old_pathes) != len(new_pathes):
        return True
    for path in old_pathes:
        if path not in new_pathes:
            return True
    return False
 
def get_possible_ways(puzzle, patterns):
    pathes = []
    tmp_pathes = []
    steps = get_next_steps([], puzzle, patterns)
    for step in steps:
        tmp_pathes.append([step])
    #print("Initial pathes:", tmp_pathes)
    while has_new_path(pathes, tmp_pathes):
        #input("Print progress:")
        #print_progress_v2(tmp_pathes, pathes)
        pathes = tmp_pathes
        tmp_pathes = []
        for path in pathes:
            if pathes_has_puzzle([path], puzzle):
                tmp_pathes.append(path)
                continue
            steps = get_next_steps(path, puzzle, patterns)
            #print("Next steps:", steps, "for path: ", path)
            #input("Next:")
            if len(steps) == 0:
                continue
            for step in steps:
                if is_new_path_v2(path, step, tmp_pathes):
                    path_copy = path.copy()
                    path_copy.append(step)
                    tmp_pathes.append(path_copy)
    count = 0
    for path in tmp_pathes:
        if "".join(path) == puzzle:
            count += 1
    return count

def get_next_steps_v2(puzzle, patterns):
    final_steps = []
    non_final_steps = []
    for i in range(0, len(puzzle)+1):
        #print("Check if", puzzle[len(full_path):i], len(full_path), i, "in", puzzle)
        if puzzle[:i] in patterns:
            if i == len(puzzle):
                final_steps.append(puzzle[:i])
            else:
                non_final_steps.append(puzzle[:i])
    return final_steps, non_final_steps


def get_possible_ways_v2(puzzle, patterns):
    final_steps, non_final_steps = get_next_steps_v2(puzzle, patterns)
    #print("final steps:", final_steps)
    #print("non-final steps:", non_final_steps)
    #input("Next:")
    if len(non_final_steps) == 0:
        return len(final_steps)
    else:
        tmp = 0
        for nf in non_final_steps:
            tmp += get_possible_ways_v2(puzzle[len(nf):], patterns)
        return len(final_steps) + tmp

def q1(patterns, puzzles):
    count = 0
    for i in range(len(puzzles)):
        #print("Checking: ", puzzles[i], "(", i+1, "/", len(puzzles), ")")
        if is_possible(puzzles[i], patterns):
            count += 1
            #print(puzzle, "is possible")
        else:
            print(puzzles[i], "is impossible")
    print(count)

def q2(patterns, puzzles):
    count = 0
    new_puzzles = []
    for i in range(len(puzzles)):
        #print("Checking: ", puzzles[i], "(", i+1, "/", len(puzzles), ")")
        if is_possible(puzzles[i], patterns):
            new_puzzles.append(puzzles[i])
    for i in range(len(new_puzzles)):
        print("Checking: ", new_puzzles[i], "(", i+1, "/", len(new_puzzles), ")")
        count += get_possible_ways(new_puzzles[i], patterns)
    print(count)
    
with open("./input.txt", "r") as file:
    patterns = []
    puzzles = []
    pattern_mode = True
    for line in file:
        line = line.strip()
        if line == "":
            pattern_mode = False
            continue
        if pattern_mode == True:
            patterns = line.split(", ")
        else:
            puzzles.append(line)
    q2(patterns, puzzles)