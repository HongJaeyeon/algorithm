import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()
ls = list(input())
selected = [-1 for _ in range(n+1)]
visited = [False for _ in range(10)]
maxValue = str(-float('inf'))
minValue = str(float('inf'))
def recur(depth, selected, visited):
    global maxValue, minValue
    if depth >= 2:
        if ls[depth-2] == "<" and selected[depth-2] >= selected[depth-1]:
            return

        if ls[depth-2] == ">" and selected[depth-2] <= selected[depth-1]:
            return

    if depth == n+1:
        maxValue = max(maxValue, ''.join(map(str, selected)))
        minValue = min(minValue, ''.join(map(str, selected)))
        return

    # for i in range(10):
    #     selected[depth] = i
    #     recur(depth+1, selected)

    #선택된 숫자는 모두 달라야하므로
    # for i in range(start, 10):
    #     selected[depth] = i
    #     recur(depth+1, selected, i+1)

    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        selected[depth] = i
        recur(depth+1, selected, visited)
        visited[i] = False
recur(0, selected, visited)
print(maxValue)
print(minValue)