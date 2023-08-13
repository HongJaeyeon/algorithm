import sys

def recur(cur):
    global visited
    visited[cur] = True
    for ele in adj[cur]:
        if visited[ele]:
            continue
        recur(ele)

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())
visited = [False for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input())
    adj[a].append(b)
    adj[b].append(a)

cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    recur(i)
    cnt += 1

print(cnt)