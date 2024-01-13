R, C = map(int, input().split())
ls = [list(input()) for _ in range(R)]
cnt = 1
ans = [-1 for _ in range(10)]

for c in reversed(range(1, C-1)):
    flag = False
    for r in range(R):
        if ls[r][c] != '.':
            if ans[int(ls[r][c])] != -1:
                continue
            ans[int(ls[r][c])] = cnt
            flag = True

    if flag:
        cnt += 1

print(*ans[1:], sep="\n")