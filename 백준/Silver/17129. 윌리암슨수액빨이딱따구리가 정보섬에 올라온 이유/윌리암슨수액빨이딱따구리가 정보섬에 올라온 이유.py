import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().strip().split())

ls = [list(map(int, input().strip())) for _ in range(r)]
loc = [[i,j] for i in range(r) for j in range(c) if ls[i][j] == 2]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dq = deque([loc[0] + [0]])
visited = [[False for _ in range(c)] for _ in range(r)]
visited[loc[0][0]][loc[0][1]] = True

while dq:
    cr, cc, step = dq.popleft()
    if ls[cr][cc] == 3 or ls[cr][cc] == 4 or ls[cr][cc] == 5:
        print("TAK")
        print(step)
        break
    for d in dir:
        nr = cr + d[0]
        nc = cc + d[1]
        if nr < 0 or nc < 0 or nr >= r or nc >= c:
            continue
        if ls[nr][nc] == 1 or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        dq.append([nr, nc, step+1])
else:
    print("NIE")