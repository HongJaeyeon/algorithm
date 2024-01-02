r, c = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(r)]
# 첫 행, 첫 열을 위한 패딩 작업
prefix_sum = [[0 for _ in range(c+1)] for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        # 사각형 형태로 누적합 저장
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + ls[i-1][j-1]

n = int(input())
for i in range(n):
    i, j, x, y = map(int, input().split())
    print(prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1])