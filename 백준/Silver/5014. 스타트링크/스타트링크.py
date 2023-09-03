import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

dq = deque()
visited = [False for _ in range(f+1)]
dq.append([0, s])
visited[s] = True

def bfs():
    while dq:
        step, cur = dq.popleft()

        if cur == g:
            print(step)
            break

        for dir in [u, -d]:
            ncur = cur + dir

            if ncur < 1 or f+1 <= ncur:
                continue

            if visited[ncur]: #해당 위치라면 다음에 갈 수 있는 길이 모두 u or -d로 같기 때문에, 먼저 ncur에 도달하는게 visited 체크해도 됨 -> 그 뒤에 오는 것들도 모두 같은 길을 걷게 되기에
                continue

            dq.append([step+1, ncur])
            visited[ncur] = True

    else:
        print("use the stairs")

bfs()