import sys

n, m = map(int, sys.stdin.readline().strip().split())
selected = [0 for _ in range(m)]

def perm(cnt):
    if cnt == m:
        print(' '.join(map(str, selected)))
        return

    for i in range(1,n+1):
        selected[cnt] = i
        perm(cnt+1)
perm(0)