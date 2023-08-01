import sys

input = sys.stdin.readline
n = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print("no" if i == 1 and len(adj[j]) == 1 else "yes")

