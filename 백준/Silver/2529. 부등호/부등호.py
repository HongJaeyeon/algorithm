import sys
lambda input: sys.stdin.readline().strip()

N = int(input())
ls = list(input().split())
selected = [0 for _ in range(N+1)]
visited = [0 for _ in range(10)]

maxValue = str(-float('inf'))
minValue = str(float('inf'))

def recur(depth):
    global maxValue, minValue
    if depth >= 2:
        if ls[depth-2] == "<":
            if selected[depth-2] > selected[depth-1]:
                return
        else:
            if selected[depth - 2] < selected[depth - 1]:
                return

    if depth == N+1: #뽑는 개수
        tmp = ''.join(map(str, selected))
        maxValue = max(maxValue, tmp)
        minValue = min(minValue, tmp)
        return

    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        selected[depth] = i
        recur(depth+1)
        visited[i] = False
recur(0)

print(maxValue)
print(minValue)

