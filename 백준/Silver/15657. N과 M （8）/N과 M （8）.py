import sys
input = lambda: sys.stdin.readline().strip().split()

n, c = map(int, input())
ls = list(map(int, input()))
selected = [0 for _ in range(c)]
ls.sort()

# 중복 조합
def recur(depth, start):
    if depth == c:
        print(*selected)
        return

    for i in range(start, n):
        selected[depth] = ls[i]
        recur(depth+1, i)

recur(0, 0)
