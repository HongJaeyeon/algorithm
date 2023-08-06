import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
adj = [[] for _ in range(n+1)]
input = lambda: sys.stdin.readline().strip().split()
visited = [False for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

def dfs(cur, pre):
    visited[cur] = True
    # print("cur", cur, "pre", pre)
    parents[cur] = pre
    for ele in adj[cur]:
        if visited[ele]:
            continue
        dfs(ele, cur)

for _ in range(n-1):
    a, b = map(int, input())
    adj[a].append(b)
    adj[b].append(a)


dfs(1, 0)
print("\n".join(map(str, parents[2:])))

