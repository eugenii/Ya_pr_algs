#  Сравнить 2 строки.
import sys

input_data = sys.stdin.read().splitlines()
line_1 = input_data[0]
line_2 = input_data[1]

word_1 = ''
word_2 = ''

for w in line_1:
    if ord(w) % 2 == 0:
        word_1 += w
for w in line_2:
    if ord(w) % 2 == 0:
        word_2 += w
if word_1 < word_2:
    print(-1)
elif word_1 == word_2:
    print(0)
else:
    print(1)