import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    sr, sc = map(int, input().rstrip().split())
    er, ec = map(int, input().rstrip().split())

    visited = [[False for _ in range(n)]for _ in range(n)]
    dq = deque()
    dq.append([sr, sc, 0])
    dir = [[-2,-1], [-2, 1], [2,-1], [2,1], [-1,-2], [1,-2], [-1,2], [1,2]]

    while dq:
        cr, cc, step = dq.popleft()
        if cr == er and cc == ec:
            print(step)
            break

        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]

            if nr < 0 or nr >= n or nc <0 or nc >= n:
                continue
            if visited[nr][nc]:
                continue

            dq.append([nr,nc,step+1])
            visited[nr][nc] = True
