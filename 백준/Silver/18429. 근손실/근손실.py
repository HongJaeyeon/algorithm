import sys
input = lambda: sys.stdin.readline().strip()
n, k = map(int, input().split())
ls = list(map(int, input().split()))
visited = [False for _ in range(n)]
# selected = [0 for _ in range(n)] 안 쓰고 바로 weight에 반영
cnt = 0

def recur(day, weight):
    global cnt
    if weight < 500:
        return

    if day == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        recur(day+1, weight-k+ls[i])
        visited[i] = False

recur(0, 500)
print(cnt)
