import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

dp = [[-1] * 3 for _ in range(n)]


# 지금 depth에서, 해당 집을 뽑고 안 뽑고
def recur(depth, beforColor):
    minValue = float('inf')

    if depth == n:
        return 0

    if dp[depth][beforColor] != -1:
        return dp[depth][beforColor]

    #해당 depth에서 모든 색깔을 뽑아보는데, 앞에서 뽑은 색깔이면 뽑지 않게
    for i in range(3):
        if i == beforColor:
            continue
        minValue = min(minValue, recur(depth+1, i) + ls[depth][i])
    dp[depth][beforColor] = minValue
    # return minValue
    return dp[depth][beforColor]

print(recur(0,-1))