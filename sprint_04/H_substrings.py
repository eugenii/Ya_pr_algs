# H подстроки.

line = input()
left = 0
right = 0
substrings = {}
end = len(line)
len_max = 0

while right < end:
    if not substrings.get(line[right]):
        substrings[line[right]] = 1
        right += 1
        if
