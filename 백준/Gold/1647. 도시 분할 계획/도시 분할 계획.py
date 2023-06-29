import sys

def makeSet(): #자기가 대표인 집합 만들기
    for i in range(1, V+1):
        parents[i] = i

def findParent(a):
    if parents[a] == a:
        return a
    parents[a] = findParent(parents[a])
    return parents[a]

def union(a, b):
    pa = findParent(a)
    pb = findParent(b)
    # 부모가 같다면 합칠 수 없음 (사이클 존재)
    if pa == pb:
        return False
    parents[pb] = pa
    return True

V, E = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(E)]
parents = [0 for _ in range(V+1)]

edge_cnt = 0
edges.sort(key=lambda x: x[2])
ans = 0

makeSet()
for s, t, w in edges:
    if not union(s, t):
        continue
    if edge_cnt == V-2:
        break
    ans += w
    edge_cnt += 1

print(ans)