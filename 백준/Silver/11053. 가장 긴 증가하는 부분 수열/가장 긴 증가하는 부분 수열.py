import sys

n = int(input())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1 for _ in range(n)]
#dp[i] = i이전까지의 가장긴증가하는부분수열의 길이를 담는다.
#ls[0~i-1]중 ls[i]보다 작은 값을 찾고 해당 인덱스의 dp값들 중 가장 긴 것에다가 +1 한 것이 dp[i]가 된다

dp[0] = 1 #idx 0이 가지는 가장긴증가하는부분수열의 길이는 자기 자신만 포함한 1이다.

# for i in range(1, n):
#     maxVal = -float('inf')
#     for j in range(i):
#         # print(i, j)
#         if ls[j] < ls[i] : #현재 타겟 인덱스 i보다 작은 값을 가지고 있다면
#             maxVal = max(maxVal, dp[j]) #더 긴길이를 가지고 있는 dp를 찾는다
#     dp[i] = maxVal + 1

for i in range(1, n):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j]+1,)

# print(dp[-1])
#모든 배열의 요소를 다 보았을 때 저장된 값이 최종 답
#이 아니다.. 끝까지 보는 게 더 작은 값을 가질 수도 있다

print(max(dp))