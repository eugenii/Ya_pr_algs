# C Последовательность

s = input()  # Искомая подпоследоватьность
t = input()  # Последовательность

result = []
for letter in s:
    if letter in t:
        result.append((1, t.index(letter), s.count(letter), t.count(letter)))
    else:
        result.append(0)

print(all(result))
print(result)
print(len(result) == len(s))