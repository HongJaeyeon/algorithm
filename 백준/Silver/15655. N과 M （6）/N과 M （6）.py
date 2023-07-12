import sys

input = lambda: sys.stdin.readline().strip()

n, r = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()

# visited = [0 for _ in range(n)] #index를 다룬다
selected = [0 for _ in range(r)]

def comb(depth, start):
    if depth == r:
        for i in selected:
            print(ls[i], end=" ")
        print()
        return

    for i in range(start, n):
        selected[depth] = i
        comb(depth+1, i+1)

comb(0, 0)