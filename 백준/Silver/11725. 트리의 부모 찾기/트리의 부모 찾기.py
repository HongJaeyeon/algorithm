import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().strip()

n = int(input())
tree = [[] for _ in range(n+1)]
preNodeInfo = [0 for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(preNode, curNode):
    preNodeInfo[curNode] = preNode
    for node in tree[curNode]:
        if preNode != node:
            dfs(curNode, node)

dfs(-1, 1)

for ele in preNodeInfo:
    if ele == -1 or ele == 0:
        continue
    print(ele)