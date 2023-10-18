import sys
input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
selected = [0 for _ in range(M)]

def recur(depth, start):
    if depth == M:
        print(*selected)
        return

    for i in range(start, N):
        selected[depth] = ls[i]
        recur(depth+1, i)

recur(0, 0)
