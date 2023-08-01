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
    if i == 1:
        if len(adj[j]) == 1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
