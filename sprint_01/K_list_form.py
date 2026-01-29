# K Списочная форма.

x = int(input())
form = input()
k = int(input())

res = ''
end = -len(form) - 1
up = 0
for i in range(-1, end, -2):
    temp = int(form[i]) + k % 10 + up
    if temp > 9:
        res = " " + str(temp % 10) + res
        up = 1
    else:
        res = " " + str(temp) + res
        up = 0
    k //= 10

while k > 0:
    temp = k % 10 + up
    if temp > 9:
        res = " " + str(temp % 10) + res
        up = 1
    else:
        res = " " + str(temp) + res
        up = 0
    k //= 10
if up == 1:
    res = "1" + res
print(res.strip())