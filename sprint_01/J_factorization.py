# J Факторизация

def factorize(n):
    factors = []
    end = int(n ** 0.5) + 1
    for i in range(2, end):
        if n % i == 0:
            while n % i == 0:
                factors.append(i)
                n //= i
    if n > 1:
        factors.append(n)
    return factors


print(*factorize(int(input())))