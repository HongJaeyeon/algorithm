import sys
sys.setrecursionlimit(10**5)

tree = []
par = []
N = 0

def dfs(cur, pre):
    for nxt in tree[cur]:
        if nxt == pre:
            continue
        par[nxt] = cur
        dfs(nxt, cur)

def makeCommonParList(a):
    ls = []
    while a != -1:
        ls.append(a)
        a = par[a]
    return ls

def findRoot(visited):
    for i in range(len(visited)):
        if i == 0:
            continue
        if not visited[i]:
            return i

tc = int(input())
for _ in range(tc):
    N = int(input())
    visited = [False for _ in range(N+1)]
    tree = [[]for _ in range(N+1)]
    par = [-1 for _ in range(N+1)]
    for _ in range(N-1):
        p, c = map(int, input().split())
        tree[p].append(c)
        visited[c] = True
    a, b = map(int, input().split())

    dfs(findRoot(visited), 0)

    aList = makeCommonParList(a)
    bList = makeCommonParList(b)

    flag = False
    for i in range(len(aList)):
        for j in range(len(bList)):
            if aList[i] == bList[j]:
                print(aList[i])
                flag = True
                break

        if flag:
            break