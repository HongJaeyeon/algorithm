import sys
input = lambda: sys.stdin.readline().strip().split()

n, c = map(int, input())
ls = list(map(int, input()))
selected = []
ls.sort()

def recur(depth, cnt):
    if depth == n:
        if cnt == c:
            print(*selected)
        return

    selected.append(ls[depth])
    recur(depth+1, cnt+1)
    selected.pop()
    recur(depth+1, cnt)

recur(0, 0)