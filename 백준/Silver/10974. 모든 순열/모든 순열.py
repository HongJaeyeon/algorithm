def recur(depth):
    if depth == n:
        print(" ".join(map(str, selected)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        selected[depth] = i
        visited[i] = True
        recur(depth+1)
        visited[i] = False

n = int(input())
selected = [-1 for _ in range(n)]
visited = [False for _ in range(n+1)]
recur(0)
