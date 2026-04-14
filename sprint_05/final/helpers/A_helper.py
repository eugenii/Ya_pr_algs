# Вспомогательные подзадачи к финальным задачам.
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