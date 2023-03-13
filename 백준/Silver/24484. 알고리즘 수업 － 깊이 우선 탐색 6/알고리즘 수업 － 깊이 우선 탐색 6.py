import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, depth):
    global cnt
    global answer
    visited[node] = True
    cnt += 1
    answer += (cnt * depth)
    for ele in adj[node]:
        if not visited[ele]:
            dfs(ele, depth+1)

v, e, s = map(int, sys.stdin.readline().strip().split())

adj = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
cnt = 0
answer = 0
for _ in range(e):
    n, m = map(int, sys.stdin.readline().strip().split())
    adj[n].append(m)
    adj[m].append(n)

for arr in adj:
    arr.sort(reverse=True)

dfs(s, depth=0)

print(answer)




'''

5 5 1
1 4
1 2
2 3
2 4
3 4

'''