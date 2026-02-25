# C Последовательность

s = input()  # Искомая подпоследовательность
t = input()  # Последовательность

pos_s = 0

for i in range(len(t)):
    if t[i] == s[pos_s]:
        pos_s += 1
        if pos_s == len(s):
            break

print(pos_s == len(s))