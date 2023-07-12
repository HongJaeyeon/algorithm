import sys

input = lambda: sys.stdin.readline().strip()

n, r = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

visited = [0 for _ in range(n)] #index를 다룬다
selected = [0 for _ in range(r)]

def perm(depth):
    if depth == r:
        for i in selected:
            print(ls[i], end=" ")
        print()
        return

    for i in range(n):
        selected[depth] = i
        perm(depth+1)
perm(0)