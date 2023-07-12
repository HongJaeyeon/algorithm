import sys

input = lambda: sys.stdin.readline().strip().split()
answer = list(map(int, input()))
ans = 0
def recur(depth, selected):
    global ans
    cnt = 0
    if depth == 10:
        for i, j in zip(selected, answer):
            if i == j:
                cnt += 1
        if cnt >= 5:
            ans += 1
        return

    for i in range(1, 6):
        if depth > 1 and (selected[depth-2] == selected[depth-1] and selected[depth-1] == i):
            continue
        recur(depth+1, selected+[i])

recur(0,[])
print(ans)