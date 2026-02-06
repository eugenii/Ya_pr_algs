# Задача А. Мониторинг (напечатать транспонированную матрицу)
# rows - строки, cols - столбцы

rows, cols = int(input()), int(input())
matrix = [input().split() for _ in range(rows)]
t_matrix = []
for col in range(cols):
    t_matrix.append([])
    for row in range(rows):
        t_matrix[col].append(matrix[row][col])

for row in range((len(t_matrix))):
    print(*t_matrix[row])

