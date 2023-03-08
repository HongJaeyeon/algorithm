import sys
input = sys.stdin.readline
V, E = map(int, input().strip().split())
parents = [0 for _ in range(V+1)]

def makeSet():
    for i in range(1, V):
        parents[i] = i

def findParent(i):
    if parents[i] == i:
        return i
    parents[i] = findParent(parents[i])
    return parents[i]

def union(i, j):
    i = findParent(i)
    j = findParent(j)
    if i == j: return False
    parents[j] = i
    return True

edges = []
for _ in range(E):
   edges.append(list(map(int, input().strip().split())))
edges.sort(key=lambda x: x[2])

ans = 0
cnt = 0
makeSet()
for edge in edges:
    s, t, w = edge
    if union(s, t):
        ans += w
        cnt += 1
    if cnt == V - 2:
        break
print(ans)