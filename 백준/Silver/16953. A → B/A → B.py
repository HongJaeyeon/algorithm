import sys
from collections import deque

def bfs():
    dq = deque()
    dq.append([a, 0])
    while dq:
        num, cnt = dq.popleft()
        
        if num > b:
            # print(-1)
            # return
            continue
            
        if num == b:
            print(cnt+1)
            return
        
        dq.append([num * 2, cnt+1])
        dq.append([int(str(num)+"1"), cnt+1])
    # num이 b보다 크다고 바로 -1 리턴하면 안됨 다른 bfs에서 답을 찾을 수 있어서
    # dq가 빌 때까지도 못 찾았다면 정말 못 찾은 것이므로 여기에서 -1 출력
    else:
        print(-1)
        return

a, b = map(int, sys.stdin.readline().rstrip().split())
bfs()