# B Расписание.
import sys

count = int(input())
data = sys.stdin.read().split()

lessons = [(i, j) for i, j in zip(data[::2], data[1::2])]
lessons.sort(key=lambda x: (float(x[1]), float(x[0])))

result_lessons = []

last_end = -1.0

for lesson in lessons:
    if float(lesson[0]) >= float(last_end):
        result_lessons.append(lesson)
        last_end = float(lesson[1])

print(len(result_lessons))
for lesson in result_lessons:
    print(*lesson)