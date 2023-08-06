import sys
sys.setrecursionlimit(10 ** 6)

def dfs(cur):
    for ele in adj[cur]:
        sumList[ele] += sumList[cur]
        dfs(ele)

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())
adj = [[]for _ in range(n+1)]
ls = list(map(int, input()))
for i in range(n):
    if ls[i] == -1:
        continue
    adj[ls[i]].append(i+1)

sumList = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input())
    sumList[a] += b

dfs(1)

print(" ".join(map(str, sumList[1:])))