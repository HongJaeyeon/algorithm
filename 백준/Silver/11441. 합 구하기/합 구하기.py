n = int(input())
ls = list(map(int, input().split()))
tc = int(input())
ls = [0] + ls

# 그냥 돌면 O(100,000 * 100,000) -> 1초 이상
# for _ in range(tc):
#     n, m = map(int, input().split())
#     sumValue = 0
#     for i in range(n-1, m):
#         sumValue += ls[i]
#
#     print(sumValue)


# 누적합 쓰면 한 번만 구하고 상수 시간으로 접근하므로 O(100,000)
for i in range(1, n+1):
    ls[i] = ls[i-1] + ls[i]

for _ in range(tc):
    n, m = map(int, input().split())
    print(ls[m]-ls[n-1])
