import sys
lambda input : sys.stdin.readline().strip()

n = int(input())
ls = list(map(int, input().split()))
ans = 0
sumValue = sum(ls)

for ele in ls:
    sumValue -= ele
    ans += ele * sumValue

print(ans % 1000000007)