# def rec(k): # 길이가 k인 그거를 채우는 경우의수
#     global ans
#     if k < 0: #
#         return
#     if k == 0:
#         ans += 1
#         return
#     rec(k - 1)
#     rec(k - 2)

# def rec(k): # 길이가 k인 그거를 채우는 경우의수
#     if k < 0:
#         return 0
#     if k == 0:
#         return 1
#     return rec(k - 1) + rec(k - 2)

def rec(k): # 길이가 k인 그거를 채우는 경우의수
    if k < 0:
        return 0
    if k == 0:
        return 1
    if dp[k] != -1: # 메모이제이션
        return dp[k]
    dp[k] = (rec(k - 1) + rec(k - 2)) % 10007
    return dp[k]



n = int(input())
# ans = 0
# rec(n)
# print(ans)

# print(rec(n))

dp = [-1] * (n + 1)
print(rec(n))