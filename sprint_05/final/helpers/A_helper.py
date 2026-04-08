# Вспомогательные подзадачи к финальным задачам.
from dataclasses import dataclass
import sys


@dataclass(order=True)
class Participant:
    tasks: int
    penalty: int
    login: str

    def __lt__(self, other):
        # 1. Сначала сравниваем задачи (чем меньше задач, тем "меньше" участник)
        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        # 2. Если задачи равны, сравниваем штраф (чем БОЛЬШЕ штраф, тем "меньше" участник)
        if self.penalty != other.penalty:
            return self.penalty > other.penalty
        # 3. Если и это равно, сравниваем логин (чем ПОЗЖЕ логин, тем "меньше" участник)
        # В алфавитном порядке 'b' > 'a', значит 'b' - "меньше" в турнирной таблице
        return self.login > other.login


def sift_down(heap, idx) -> int:
    heap_max_index = len(heap)-1
    left = idx * 2 + 1
    right = idx * 2 + 2

    # нет дочерних узлов
    if left > heap_max_index:
        return idx
    
    # проверяем, что есть оба дочерних узла
    if right <= heap_max_index and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left
    # отправляем максимум на вершину кучи и рекурсивно завпускаем просеивание в ребенке
    if heap[index_largest] > heap[idx]:
        heap[index_largest], heap[idx] = heap[idx], heap[index_largest]
        return sift_down(heap, index_largest)
    return idx


def heapify(participants):
    n = len(participants)
    # Начинаем с последнего родителя и идем к корню
    for i in range(n // 2 - 1, -1, -1):
        sift_down(participants, i, n) # n здесь — размер кучи


count = int(input())
participants = []
for _ in range(count):
    login, tasks, penalty = sys.stdin.readline().split()
    participants.append(Participant(int(tasks), -int(penalty), login))



'''
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
'''