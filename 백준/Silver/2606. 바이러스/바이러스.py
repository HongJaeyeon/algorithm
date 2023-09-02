n = int(input())
m = int(input())

visited = [False for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(cur):
    visited[cur] = True
    for ele in adj[cur]:
        if visited[ele]:
            continue

        # 모든 길을 다 가봐야하는 것이 아니라, 연결 요소만 보려는 것이기 때문에 visited 안 풀어도 된다.
        visited[ele] = True
        dfs(ele)

dfs(1)

cnt = -1
for ele in visited:
    if ele:
        cnt += 1

print(cnt)
