import sys

input = lambda: sys.stdin.readline().strip()
r, c, k = map(int, input().split())
ls = [list(input()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
dir = [[-1,0], [1,0], [0,-1], [0,1]]
ans = 0
def recur(depth, cr, cc):
    global r, c, ans
    if depth >= k:
        return
    if cr == 0 and cc == c-1 and depth == k-1:
        ans += 1
        return

    for d in dir:
        nr = cr + d[0]
        nc = cc + d[1]

        if nr < 0 or nc < 0 or nr >= r or nc >= c:
            continue
        if visited[nr][nc] or ls[nr][nc] == "T":
            continue
        visited[nr][nc] = True
        recur(depth+1, nr, nc)
        visited[nr][nc] = False

visited[r-1][0] = True
recur(0, r-1, 0)
print(ans)