import sys
input = lambda: sys.stdin.readline().strip()


ls = list(input())
n = len(ls)
visited = [False for _ in range(n)]
selected = ['' for _ in range(n)]
ans = set()

def recur(depth):
    if depth == n:
        # print(selected)
        ans.add(''.join(selected))
        return

    for i in range(n):
        if visited[i]:
            continue
        if ls[i] == selected[depth-1]:
            # print("ls[i] == selected[depth-1]:", ls[i], selected[depth-1])
            continue

        visited[i] = True
        selected[depth] = ls[i]
        recur(depth+1)
        visited[i] = False
        selected[depth] = ''

recur(0)
print(len(ans))
