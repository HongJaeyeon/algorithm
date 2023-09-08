import sys
input = lambda: sys.stdin.readline().strip()
ls = list(input())
ls2 = list(input())

memo = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, len(ls)+1):
    for j in range(1, len(ls2)+1):
        if ls[i-1] == ls2[j-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[len(ls)][len(ls2)])