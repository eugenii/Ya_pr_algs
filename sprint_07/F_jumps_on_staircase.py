# F Jumps on Staircaseю

MOD = 10 ** 9 + 7


def staircase(n, k):

    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = sum(dp[:i]) % MOD
            continue
        dp[i] = (2 * dp[i - 1] - (dp[i - k - 1])) % MOD
    return dp[n - 1]


def main():
    n, k = map(int, input().split())
    print(staircase(n, k))


if __name__ == '__main__':
    main()


    assert staircase(532, 66) == 979579740