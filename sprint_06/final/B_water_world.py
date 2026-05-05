# Успешная посылка: https://contest.yandex.ru/contest/25070/run-report/160919516/
# Алгоритм:
# Использован итеративный обход в глубину (DFS) на базе стека (Stack). 
# Вместо создания явного графа обход выполняется прямо по матрице смежности (сетке), что экономит память.

# Временная сложность: O(N * M).
# Мы посещаем каждую клетку поля ровно один раз.
# Внешние циклы проходят по всем клеткам, а внутренний DFS «поглощает» каждую клетку суши только единожды, 
# помечая её водой (flood fill).

# Пространственная сложность: O(N * M).
# Хранение самой карты требует O(N * M)памяти.
# В худшем случае (если всё поле — один извилистый остров) стек может разрастись до O(N * M).
# Примечание: Мы сэкономили  O(N * M) памяти, отказавшись от отдельного массива visited, изменяя данные прямо во входной матрице.
# В решении использован итеративный подход (stack) чтобы избежать RecursionError на больших тестах (до 1000x1000).

import sys

def solve():
    # Читаем все данные сразу
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    # Превращаем строки в списки символов, чтобы можно было их менять
    world = [list(row) for row in input_data[2:]]
    
    islands_count = 0
    max_island_size = 0
    
    for r in range(n):
        for c in range(m):
            # Если нашли необработанную землю
            if world[r][c] == '#':
                islands_count += 1
                current_size = 0
                # Итеративный DFS (стек)
                stack = [(r, c)]
                world[r][c] = '.'  # Помечаем как посещенную (топим)
                
                while stack:
                    curr_r, curr_c = stack.pop()
                    current_size += 1
                    
                    # Проверяем 4 направления
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        if 0 <= nr < n and 0 <= nc < m and world[nr][nc] == '#':
                            world[nr][nc] = '.'  # Помечаем сразу при добавлении в стек
                            stack.append((nr, nc))
                
                # Обновляем рекорд размера
                if current_size > max_island_size:
                    max_island_size = current_size
                    
    print(islands_count, max_island_size)

if __name__ == '__main__':
    solve()
