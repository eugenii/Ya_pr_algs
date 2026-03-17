# F Префиксные хеши.
import sys

# Используем sys.stdin.read().split(), чтобы чтение 10^5 строк было мгновенным
input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = int(input_data[0])
m = int(input_data[1])
s = input_data[2]
t = int(input_data[3])

n = len(s)
# 1. Массив префиксных хешей
# h[i] будет хранить хеш префикса длины i
h = [0] * (n + 1)
# 2. Массив степеней основания a^k % m
p = [1] * (n + 1)

for i in range(n):
    # Считаем хеш: предыдущий * a + текущий символ
    h[i+1] = (h[i] * a + ord(s[i])) % m
    # Считаем степень: предыдущая * a
    p[i+1] = (p[i] * a) % m

# Обработка запросов
results = []
idx = 4
for _ in range(t):
    l = int(input_data[idx])
    r = int(input_data[idx+1])
    idx += 2
    
    # Формула: Hash(l, r) = (h[r] - h[l-1] * a^(r-l+1)) % m
    # В задаче индексация с 1, поэтому используем l-1 и r
    res = (h[r] - h[l-1] * p[r - l + 1]) % m
    results.append(str(res))

# Выводим всё одним махом
sys.stdout.write("\n".join(results) + "\n")
