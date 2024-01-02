r, c = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(r)]

n = int(input())

for i in range(n):
    i, j, x, y = map(int, input().split())

    sumValue = 0
    for l in range(i, x+1):
        for m in range(j, y+1):
            sumValue += ls[l-1][m-1]
    print(sumValue)