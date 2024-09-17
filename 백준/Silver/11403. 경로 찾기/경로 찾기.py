import sys
n = int(input())
ls = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dist = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if ls[i][j] == 1:
            dist[i][j] = 1

for path in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][path] + dist[path][j]:
                dist[i][j] = dist[i][path] + dist[path][j]

for r in dist:
    for ele in r:
        if ele != float('inf'):
            print(1, "", end="")
        else:
            print(0, "", end="")
    print()