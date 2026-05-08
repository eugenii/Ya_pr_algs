# H field with flowers.
import sys


def collect(n, m, field, dp):
    
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i == n - 1 and j == 0:
                continue
            if i == n - 1:
                dp[i][j] = dp[i][j - 1] + field[i][j]
                continue
            elif j == 0:
                dp[i][j] = dp[i + 1][j] + field[i][j]
                continue
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + field[i][j]

def find_path(n: int, m: int, field: list, dp) -> str:
    res = ''
    row = 0
    col = m - 1
    while ( row, col) != (n - 1, 0):
        if col == 0:
            res += 'U'
            row += 1
            continue
        if row == n - 1:
            res += 'R'
            col -= 1
            continue
        if dp[row][col - 1] >= dp[row + 1][col]:
            res += 'R'
            col -= 1
        else:
            res += 'U'
            row += 1
    return res[::-1]



def main():

    data = sys.stdin.read().split()

    n, m = int(data[0]), int(data[1])

    field = []
    for line in data[2:]:
        field.append([int(j) for j in list(line)])

    dp = [[0 for _ in range(m)] for _ in range(n)]  
    dp[n - 1][0] = field[n - 1][0]

    collect(n, m, field, dp)

    print(dp[0][m - 1])
    print(find_path(n, m, field, dp))


if __name__ == '__main__':
    main()