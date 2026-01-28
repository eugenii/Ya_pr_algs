# задача C Соседи


def neighbours(matrix, y, x):
    result = []
    if rows == 1 and cols == 1:
        return result
    if rows == 1:
        if x == 0:
            return [matrix[y][x + 1]]
        elif x == cols - 1:
            return sorted([matrix[y][x - 1]])
        else:
            return sorted([matrix[y][x - 1], matrix[y][x + 1]])
        
    if cols == 1:
        if y == 0:
            return [matrix[y + 1][x]]
        elif y == rows - 1:
            return [matrix[y - 1][x]]
        return sorted([matrix[y - 1][x], matrix[y + 1][x]])
    if y == 0:
        if x == 0:
            return sorted([matrix[y][x + 1], matrix[y + 1][x]])
        elif x == cols - 1:
            return sorted([matrix[y][x - 1], matrix[y + 1][x]])
        else:
            return sorted([matrix[y][x - 1], matrix[y][x + 1], matrix[y - 1][x]])
    if y == rows - 1:
        if x == 0:
            return sorted([matrix[y][x + 1], matrix[y - 1][x]])
        elif x == cols - 1:
            return sorted([matrix[y][x - 1], matrix[y + 1][x]])
        else:
            return sorted([matrix[y][x - 1], matrix[y][x + 1], matrix[y - 1][x]])
    if x == 0:
        return sorted([matrix[y][x + 1], matrix[y - 1][x], matrix[y + 1][x]])
    if x == cols - 1:
        return sorted([matrix[y][x - 1], matrix[y - 1][x], matrix[y + 1][x]])
    
    return sorted([matrix[y][x - 1], matrix[y][x + 1], matrix[y - 1][x], matrix[y + 1][x]])

rows, cols = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for _ in range(rows)]
y, x = int(input()), int(input())


for i in neighbours(matrix, y, x):
    print(i, end=' ')
