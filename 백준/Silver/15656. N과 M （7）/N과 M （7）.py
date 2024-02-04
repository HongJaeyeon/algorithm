import sys
input = lambda: sys.stdin.readline().strip().split()

n, c = map(int, input())
ls = list(map(int, input()))
selected = [0 for _ in range(c)]
ls.sort()

# 중복 순열
def recur(depth):
    if depth == c:
        print(*selected)
        return

    for i in range(n):
        selected[depth] = ls[i]
        recur(depth+1)

recur(0)
