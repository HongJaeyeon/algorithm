import sys
input = lambda : sys.stdin.readline().strip()
N = int(input())
ls = [int(input()) for _ in range(N)]
ls.sort(key=lambda x: -x)

maxValue = ls[0]

for i in range(N):
    if i == 0:
        continue
    maxValue = max(maxValue, ls[i]*(i+1))
print(maxValue)


# 30 15 10
# 30 최대 들 수 있는 무게: 30
# 30 15 최대 들 수 있는 무게: 30
# 30 15 10 최대 들 수 있는 무게: 30

# 20 15 10
# 20 최대 들 수 있는 무게: 20
# 20 15 최대 들 수 있는 무게: 30

# 5 4 2 2 2
# 5 4 2 2 2 최대 들 수 있는 무게 : 10

# 1 2 3 4 5
# 5 4 3 2 1
# 5 / 5 / ls[i]
# 5 4 / 8 / max(max, ls[i] * 2)
# 5 4 2 / max(max, ls[i] * i)
