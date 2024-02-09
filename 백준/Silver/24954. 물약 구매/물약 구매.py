import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
ls = list(map(int, input().split()))
adj = [[] for _ in range(n)]

for i in range(n):
    m = int(input())
    for j in range(m):
        a, b = map(int, input().split())
        adj[i].append([a-1, b])

selected = [0 for _ in range(n)]
visited = [False for _ in range(n)]
minValue = float('inf')

def cal(arr):
    global minValue
    ori = [0 for _ in range(n)]
    for i in range(n):
        ori[i] = ls[i]

    sumValue = 0
    for idx in arr: #이번 순열의 구매 순서

        sumValue += ori[idx] #현재 구매하는 아이템 가격 더하기

        for ele, money in adj[idx]: #현재 구매하는 아이템과 관련된 애들 할인 시키기
            ori[ele] -= money
            if ori[ele] <= 0: # 아무리 할인을 해도 가격이 최소 동전 1개는 되어야함
                ori[ele] = 1

    minValue = min(minValue, sumValue)

# 순열
def recur(depth):
    if depth == n:
        cal(selected)
        return

    for i in range(n):
        if visited[i]:
            continue
        selected[depth] = i
        visited[i] = True
        recur(depth+1)
        visited[i] = False

recur(0)
print(minValue)