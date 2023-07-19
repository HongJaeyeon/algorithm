# import sys
# sys.stdin = open("res/tc.txt")
#
# n = int(input())
# cnt = 0
# def recur(leftLength):
#     global cnt
#     if leftLength == 0:
#         return
#     if leftLength == 2:
#         cnt += 2
#         return
#     if leftLength == 1:
#         cnt += 1
#         return
#
#     recur(leftLength-1)
#     recur(leftLength-2)
#
# recur(n)
# print(cnt)
import sys
n = int(input())

# 남은 길이가 i일 때를 다시 계산하지 않게. dp[i]에 저장해둔다.
lhs = [-1 for _ in range(n+1)]


def recur(leftLength):
    if leftLength == 0:
        return 0
    if leftLength == 2:
        return 2
    if leftLength == 1:
        return 1
    if lhs[leftLength] != -1:
        return lhs[leftLength]

    #내가 선택했을 때 남은 녀석들의 가지수
    lhs[leftLength] = (recur(leftLength-1) + recur(leftLength-2)) % 10007
    return lhs[leftLength]

print(recur(n))