import sys
import heapq

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input())
    adj[a].append([c, b])
    adj[b].append([c, a])

start, end = map(int, input())
visited = [False for _ in range(n+1)]
dist = [-float('inf') for _ in range(n+1)]

pq = []

visited[start] = True
for weight, ele in adj[start]:
    heapq.heappush(pq, [-weight, ele])

while pq:
    cur_weight, cur_node = heapq.heappop(pq)
    cur_weight = -cur_weight

    if visited[cur_node]:
        continue

    if cur_node == end:
        print(cur_weight)
        break

    visited[cur_node] = True
    dist[cur_node] = cur_weight
    for next_weight, next_node in adj[cur_node]:
        heapq.heappush(pq, [-min(next_weight, cur_weight), next_node])

