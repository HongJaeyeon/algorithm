import sys
from collections import deque

R, C = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
dir = [[-1,0], [1,0], [0,-1], [0,1]]
max_dist = 0 #모든 좌표를 시작점으로 하여 최단거리로 돌면서 그 중 가장 멀은 곳을 저장

def bfs(i, j):
    global max_dist
    q = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    q.append([i, j, 0])
    visited[i][j] = True

    while q:
        r, c, dist = q.popleft()
        for d in dir:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue
            if visited[nr][nc] or arr[nr][nc] == "W":
                continue
            q.append([nr, nc, dist+1])
            visited[nr][nc] = True
        max_dist = max(max_dist, dist)

#bfs에서 맨 마지막으로 나오는 원소는 맨 마지막 너비 == 가장 멀리 있는 좌표가 나오는 것 이용
#각 bfs가 visited를 공유하면 안됨

for i in range(R):
    for j in range(C):
        if arr[i][j] == "L":
            bfs(i, j)
print(max_dist)