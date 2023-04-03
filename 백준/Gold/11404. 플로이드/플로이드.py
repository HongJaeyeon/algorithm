import sys
n = int(input())
m = int(input())

#1. dist 세팅
dist = [[float('inf') for _ in range(n)] for _ in range(n)]

#2. 인접된 값 세팅
for _ in range(m):
    a, b, c = map(int, list(sys.stdin.readline().split()))
    if dist[a-1][b-1] > c:
        dist[a-1][b-1] = c

#3. 자기 자신까지의 거리 값 세팅
for i in range(n):
    dist[i-1][i-1] = 0

#4. 플로이드
for path in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][path] + dist[path][j]:
                dist[i][j] = dist[i][path] + dist[path][j]

for r in dist:
    for c in r:
        if c == float('inf'):
            print(0, "", end="")
        else:
            print(c, "", end="")
    print()