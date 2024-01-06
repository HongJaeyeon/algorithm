import sys

input = lambda : sys.stdin.readline().strip().split()
v, e = map(int, input())
ls = [list(map(int, input())) for _ in range(e)]
# par = [i for i in range(1, v+1)]

par = [i for i in range(v+1)]

def findp(a):
    if par[a] == a:
        return a
    par[a] = findp(par[a])
    return par[a]

def union(a, b):
    a = findp(a)
    b = findp(b)
    if a == b:
        return False
    par[a] = b
    return True

def kruskal():
    weight = 0
    ls.sort(key=lambda x: x[2])
    for a, b, w in ls:
        if union(a, b):
            weight += w

    print(weight)

kruskal()