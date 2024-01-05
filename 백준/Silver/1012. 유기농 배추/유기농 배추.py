from collections import deque

tc = int(input())
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def check(R, C):
    dq = deque()
    dq.append([R, C])

    while dq:
        cr, cc = dq.popleft()
        
        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]

            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue

            if visited[nr][nc]:
                continue

            if ls[nr][nc] == 1:
                visited[nr][nc] = True
                dq.append([nr, nc])

for _ in range(tc):
    ans = 0
    
    c, r, n = map(int, input().split())
    ls = [[0 for _ in range(c)] for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    for _ in range(n):
        a, b = map(int, input().split())
        ls[b][a] = 1

    for i in range(r):
        for j in range(c):
            if ls[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                check(i, j)
                ans += 1
                
    print(ans)