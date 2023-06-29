import sys
# sys.stdin = open("res/tc.txt")

input = sys.stdin.readline
n = int(input())
ls = list(input().rstrip())

s = 0
e = 0
dic = {}
dic[ls[0]] = 1
kind = 1
maxLength = -float('inf')
# print(n, s)

while e < len(ls):
    # print("dic", dic, maxLength)
    if kind > n:
        dic[ls[s]] -= 1
        if dic[ls[s]] == 0:
            kind -= 1
        s += 1

    #가득 차거나, 아직 안 찼을 때
    else:
        maxLength = max(maxLength, e-s+1)
        e += 1
        if e < len(ls):
            dic[ls[e]] = dic.get(ls[e], 0) + 1
            if dic[ls[e]] == 1:
                kind += 1

print(maxLength)


