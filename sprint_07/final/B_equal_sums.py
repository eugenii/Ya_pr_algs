# B - Equal Sums
import sys


def solve(scores):
    total_sum = sum(scores)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2

    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for p in scores:
        for j in range(target, p - 1, -1):
            if dp[j - p] == 1:
                dp[j] = 1

    if dp[target] == 1:
        return True
    else:
        return False


def main():

    data = sys.stdin.read().split()
    # n = int(data[0])
    scores = list(map(int, data[1:]))
    print(solve(scores))


if __name__ == '__main__':
    main()