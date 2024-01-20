import sys
import heapq
input = lambda : sys.stdin.readline().strip()
V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]
in_degree = [0 for _ in range(V+1)]
pq = []
ans = []

for _ in range(E):
    first, second = map(int, input().split())
    adj[first].append(second)
    in_degree[second] += 1

for i in range(1, V+1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)


while pq:
    cur = heapq.heappop(pq)
    ans.append(cur)

    for nxt in adj[cur]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(pq, nxt)

print(*ans)

'''
4 2
1 4
3 2

1 3 2 4 입니다.

처음에 풀 수 있는 문제는 1, 3번 문제입니다. 따라서 그중 가장 쉬운 1번 문제를 먼저 풀게 됩니다.
그러고 나면 4번 문제를 풀 수 있게 됩니다. 따라서 남은 문제 중 풀 수 있는 문제는 3, 4번 문제이며, 이중 가장 쉬운 문제인 3번을 풀게 됩니다.
그러고 나면 2번 문제를 풀 수 있게 됩니다. 따라서 남은 문제 중 풀 수 있는 문제는 2, 4번 문제이며, 이중 가장 쉬운 문제인 2번을 풀게 됩니다.
마지막으로는 남은 4번 문제를 풀게 되므로, 답은 1 3 2 4 입니다.
'''