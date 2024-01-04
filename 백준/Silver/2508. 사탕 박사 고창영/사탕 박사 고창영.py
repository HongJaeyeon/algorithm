def checkCandy(i, j):
    # 가로로 체크
    if i - 1 >= 0 and i + 1 < R:
        if ls[i-1][j] == 'v' and ls[i+1][j] == '^':
            return True

    # 세로로 체크
    if j - 1 >= 0 and j + 1 < C:
        if ls[i][j-1] == '>' and ls[i][j+1] == '<':
            return True

    return False

tc = int(input())

for _ in range(tc):
    _ = input()
    R, C = map(int, input().split())
    ls = [list(input()) for _ in range(R)]
    cnt = 0
    for i in range(R):
        for j in range(C):
            if ls[i][j] == 'o':
                if checkCandy(i, j):
                    cnt += 1
    print(cnt)