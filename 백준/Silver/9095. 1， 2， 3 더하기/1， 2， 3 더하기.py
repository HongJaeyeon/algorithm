import sys

def recur(sumValue):
    if sumValue > n:
        return 0
    if sumValue == n:
        return 1

    #들린 것
    if dp[n-sumValue] != -1:
        return dp[n-sumValue]

    cnt = 0
    for i in range(1, 4):
        cnt += recur(sumValue+i)

    dp[n-sumValue] = cnt
    return cnt

t = int(input())
input = lambda: sys.stdin.readline().strip()

dp = [-1] * 11

for _ in range(t):
    n = int(input())
    print(recur(0))
