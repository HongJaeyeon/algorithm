import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())

parents = [i for i in range(n+1)]

def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parents[rootA] = rootB

for _ in range(m):
    a, b, c = map(int, input())
    if a == 1:
        print("YES" if find(b) == find(c) else "NO")
    else:
        union(b, c)

