import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
c, r = map(int, input().split())
ls = [list(map(int, input())) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dq = deque()
dq.append([0, 0, 0])
visited[0][0] = True

def bfs():
    while dq:
        break_wall_cnt, cr, cc = dq.popleft()

        if cr == r-1 and cc == c-1:
            print(break_wall_cnt)
            break

        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]

            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if visited[nr][nc]: # 들어갈 때 visited 체크해줘도 된다.
                continue

            if ls[nr][nc] == 0:
                dq.appendleft([break_wall_cnt, nr, nc])
                visited[nr][nc] = True

            else: #1인경우 뒤에
                dq.append([break_wall_cnt+1, nr, nc])
                visited[nr][nc] = True
bfs()

# bfs - 1이하 0, 1 -> bfs 조건문으로 0일댄 앞에, 1일땐 뒤에 -> heapq 쓰는 거랑 같은 원리 -> 정렬을 안해서 훨씬 빠르다.
# 다익스트라