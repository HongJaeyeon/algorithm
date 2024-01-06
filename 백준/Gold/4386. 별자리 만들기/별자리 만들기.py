import math

def makeSet():
    global parent
    parent = [i for i in range(n)]

def findParents(a):
    global parent
    if parent[a] == a:
        return a
    parent[a] = findParents(parent[a])
    return parent[a]

def union(a, b):
    global parent
    aRoot = findParents(a)
    bRoot = findParents(b)

    if aRoot == bRoot:
        return False

    parent[bRoot] = aRoot
    return True

n = int(input())
ls = [list(map(float, input().split())) for _ in range(n)]
adj = []
parent = []
totalWeight = 0
totalCnt = 0
for i in range(n):
    for j in range(i+1, n):
        adj.append([math.sqrt((ls[j][0] - ls[i][0]) ** 2 + (ls[j][1] - ls[i][1]) ** 2), i, j])

adj.sort()
makeSet()
for w, s, e in adj:
    if totalCnt == n-1:
        break
    if union(s, e):
        totalWeight += w
        totalCnt += 1

print(totalWeight)

