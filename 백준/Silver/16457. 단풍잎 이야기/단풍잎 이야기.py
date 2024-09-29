import sys
sys.setrecursionlimit(10000)

input = lambda: sys.stdin.readline().strip().split()
n, m, k = map(int, input())
ls = [[False]*(2*n+1) for _ in range(m)]

maxCnt = 0

for i in range(m):
    for j in map(int, input()):
        ls[i][j] = True

visited = [False]*m
def recur(num, depth):
    global maxCnt

    if depth >= m:
        tmp = [False]*(2*n+1)

        cnt = 0
        for i in range(m):
            if visited[i]:
                cnt += 1
                for j in range(2*n+1):
                    tmp[j] |= ls[i][j]

        keyCnt = 0
        for i in range(2*n+1):
            if tmp[i]:
                keyCnt += 1

        if keyCnt <= n:
            maxCnt = max(maxCnt, cnt)
        return

    visited[num] = True
    recur(num+1, depth+1)

    visited[num] = False
    recur(num+1, depth+1)

recur(0, 0)
print(maxCnt)