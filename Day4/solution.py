import re

def get_str(matrix, points):
    str = ""
    for i,j in points:
        str += matrix[i][j]
    return str

def is_valid_coord(matrix, points):
    width = len(matrix[0])
    height = len(matrix)
    for i,j in points:
        if i < 0 or i >= height or j < 0 or j >= width:
            return False
    return True

def checkxmasq1(matrix, points_list):
    count = 0
    for points in points_list:
        if is_valid_coord(matrix, points):
            str = get_str(matrix, points)
            if str == "XMAS":
                count += 1
    return count

def checkxmasq2(matrix, points_list):
    count = 0
    if is_valid_coord(matrix, points_list[0]) and is_valid_coord(matrix, points_list[1]):
        str1 = get_str(matrix, points_list[0])
        str2 = get_str(matrix, points_list[1])  
        if (str1 == "MAS" or str1 == "SAM") and ( str2 == "MAS" or str2 == "SAM"):
            count += 1
    return count


def q1(matrix):
    width = len(matrix[0])
    height = len(matrix)
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            p1 = [(i, j), (i-1, j), (i-2, j), (i-3, j)]
            p2 = [(i, j), (i-1, j+1), (i-2, j+2), (i-3, j+3)]
            p3 = [(i, j), (i, j+1), (i, j+2), (i, j+3)]
            p4 = [(i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3)]
            p5 = [(i, j), (i+1, j), (i+2, j), (i+3, j)]
            p6 = [(i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3)]
            p7 = [(i, j), (i, j-1), (i, j-2), (i, j-3)]
            p8 = [(i, j), (i-1, j-1), (i-2, j-2), (i-3, j-3)]
            count += checkxmasq1(matrix, [p1, p2, p3, p4, p5, p6, p7, p8])
    print(count)
            

def q2(list1):
    width = len(matrix[0])
    height = len(matrix)
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            p1 = [(i-1, j+1), (i, j), (i+1, j-1)]
            p2 = [(i-1, j-1), (i, j), (i+1, j+1)]
            count += checkxmasq2(matrix, [p1, p2])
    print(count)

with open("./input.txt", "r") as file:
    matrix = []
    for line in file:
        line = line.strip()
        matrix.append(list(line))
    q1(matrix)
    q2(matrix)
