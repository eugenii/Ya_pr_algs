# L_excess_letter.py

s, t = list(input()), list(input())
s.sort()
t.sort()

for i in range(len(s)):
    if s[i] != t[i]:
        print(t[i])
        break
else:
    print(t[-1])
