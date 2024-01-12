n = int(input())
ls = list(map(int, input().split()))

ls.sort()

ans = 0
sumValue = 0
for ele in ls:
    sumValue += ele
    ans += sumValue

print(ans)