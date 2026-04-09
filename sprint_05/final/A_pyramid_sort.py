# Успешная сдача задачи: https://contest.yandex.ru/contest/24810/run-report/160060102/
#  Обоснование решения по шагам, памяти и времени:
# Для сравнения элементов используем переопределенный метод __lt__, для инициализации элемента класса
# используется декоратор @dataclass. (текущая тема в Яндекс.Лицее, просто попробовал применить на практике)

# Временная сложность:
# Построение кучи (Heapify): Занимает O(n). Хотя на первый взгляд кажется, что O(n * log n), 
# метод Флойда (просеивание вниз от середины) работает быстрее, так как большинство узлов находятся внизу и просеиваются на небольшую глубину.
# Сортировка: Мы n раз извлекаем корень и делаем sift_down, что занимает O(n*log n).Итого: O(n*log n). 
# Это оптимальное время для сортировок на основе сравнений.
# Сложность по памяти:
# In-place: Мы перестраиваем исходный массив «на месте», не создавая вспомогательных структур данных.
# Итого: O(1) (если не считать рекурсию в sift_down, которую при желании можно заменить на цикл, чтобы было честное O(1)).
from dataclasses import dataclass
import sys


@dataclass
class Participant:
    tasks: int
    penalty: int
    login: str

    def __lt__(self, other):
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        if self.penalty != other.penalty:
            return self.penalty < other.penalty
        return self.login > other.login



def sift_down(array, idx, n): # Добавляем n - текущий размер кучи
    left = 2 * idx + 1
    right = 2 * idx + 2
    largest = idx

    # Ищем самого "сильного" среди родителя и детей
    if left < n and array[largest] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right

    # Если самый сильный не родитель - меняем
    if largest != idx:
        array[idx], array[largest] = array[largest], array[idx]
        sift_down(array, largest, n)


def heap_sort(array):
    n = len(array)
    # 1. Строим кучу (Heapify)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n)

    # 2. Вынимаем элементы по одному
    for i in range(n - 1, 0, -1):
        # Самый лучший (на индексе 0) едет в конец массива
        array[0], array[i] = array[i], array[0]
        # Теперь куча стала меньше на один элемент
        sift_down(array, 0, i) 


count = int(input())
participants = []
for _ in range(count):
    login, tasks, penalty = sys.stdin.readline().split()
    participants.append(Participant(int(tasks), -int(penalty), login))

heap_sort(participants)

for participant in participants[::-1]:
    print(participant.login)


'''
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
'''