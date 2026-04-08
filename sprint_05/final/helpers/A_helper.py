# Вспомогательные подзадачи к финальным задачам.
from dataclasses import dataclass
import sys


@dataclass(order=True)
class Participant:
    tasks: int
    penalty: int
    login: str


count = int(input())
participants = []
for _ in range(count):
    login, tasks, penalty = sys.stdin.readline().split()
    participants.append(Participant(int(tasks), -int(penalty), login))

# Проверю рабоатет ли?
for i in range(4):
    print(participants[i] > participants[i + 1])

'''
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80
'''