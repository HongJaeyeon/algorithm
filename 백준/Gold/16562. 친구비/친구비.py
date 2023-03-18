import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().strip().split())
weights = list(map(int, input().strip().split()))
weights.insert(0, 0)
adj = [[] for _ in range(N+1)]
visited = [ False for _ in range(N+1)]
answer = 0

for _ in range(M):
    start, end = map(int, input().strip().split())
    adj[start].append(end)
    adj[end].append(start)

q = deque()

# 첫 노드부터 가보기, 사실 상관 없음 -> 친구가 있다면 어차피 다른 노드와 이어지게 됨
for start in range(1, N+1):
    if visited[start]: continue
    q.append(start)
    visited[start] = True
    w = weights[start]
    while q:
        curr = q.popleft()
        for ele in adj[curr]:
            if visited[ele]: continue
            q.append(ele)
            visited[ele] = True
            w = min(weights[ele], w)
    answer += w

print("Oh no" if answer > K else answer)

'''
5 3 20
10 10 20 20 30
1 3
2 4
5 4
'''