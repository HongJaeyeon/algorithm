# def solution(n, m, section):
#     visited = [True] * (n+1)
#     for i in section:
#         visited[i] = False
#     start = 0
#     start 
#     cnt = 0
#     for i in section:
#         flag = False
#         for j in range(i, i+m):
#             if j <= n and not visited[j]:
#                 visited[j] = True
#                 flag = True
#         if flag:
#             cnt += 1
        
#     return cnt
from collections import deque 
def solution(n, m, section):
    cnt = 0
    dq = deque()
    visited = [True] * (n)
    for i in section:
        visited[i-1] = False
        
    # 맨 앞이 False이고 롤러의 길이(M)개가 채워져있는 경우 cnt ++
    for i in range(n):
        dq.append(visited[i])
        # 롤러의 길이가 M개가 채워짐
        if len(dq) == m:
            # 맨 앞이 False
            if not dq.popleft():
                dq = deque()
                cnt += 1

    # 남은 것 체크, 하나라도 False가 있다면 cnt ++
    while dq:
        if not dq.popleft():
            cnt += 1
            break
            
    return cnt
            
    

    