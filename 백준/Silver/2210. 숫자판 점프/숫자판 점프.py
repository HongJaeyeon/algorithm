import sys
input = lambda: sys.stdin.readline().strip().split()

ls = [list(map(int, input())) for _ in range(5)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = set()

def recur(r, c, arr, cnt):
    if cnt == 5:
        ans.add(''.join(map(str, arr)))
        return

    for d in dir:
        nr = r + d[0]
        nc = c + d[1]
        if nr < 0 or nc < 0 or nr >= 5 or nc >= 5:
            continue
        arr.append(ls[nr][nc])
        recur(nr, nc, arr, cnt+1)
        arr.pop()
    return

for r in range(5):
    for c in range(5):
        recur(r, c, [ls[r][c]], 0)

print(len(ans))