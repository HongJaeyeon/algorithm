from collections import deque
from itertools import combinations
import sys

ls = [list(sys.stdin.readline().strip()) for _ in range(5)]
lsIdx = [[i, j] for i in range(5) for j in range(5)]
dir = [[-1,0],[1,0],[0,-1],[0,1]]
cnt = 0

def checkSom(comb):
    cnt = 0
    for ele in comb:
        if ls[ele[0]][ele[1]] == "S":
           cnt += 1
    return True if cnt >= 4 else False

def checkadj(comb):
    dq = deque()
    dq.append(comb[0])
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[comb[0][0]][comb[0][1]] = True
    
    while dq:
        cr, cc = dq.popleft()
        for d in dir:
            nr = cr + d[0]
            nc = cc + d[1]

            if nr < 0 or nc <0 or nr >=5 or nc >= 5:
                continue

            if visited[nr][nc]:
                continue

            if [nr, nc] in comb:
                dq.append([nr, nc])
                visited[nr][nc] = True

    for ele in comb:
        if not visited[ele[0]][ele[1]]:
            return False
    return True

for comb in combinations(lsIdx, 7):
    if checkadj(comb) and checkSom(comb):
        cnt += 1
print(cnt)

