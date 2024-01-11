N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
dist = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    dist[a][b] = 1
    dist[b][a] = 1

# dist 갱신
# 자기에서 자기는 0
# 연결 정보가 있는 것은 모두 가중치가 1, 없으면 inf
for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

minValue = float('inf')
ans = -1
for idx, l in enumerate(dist):
    tmp = l[1:]
    if minValue > sum(tmp):
        minValue = sum(tmp)
        ans = idx
        
print(ans)