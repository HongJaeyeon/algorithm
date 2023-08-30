import sys
n = int(input())
ls = list(map(int, sys.stdin.readline().strip().split()))

# 해당 수가 소수인지 아닌지 판별 -> 해당 수의 루트까지만 보며, 나누어지는지 안 나누어지는지로 판별
# O(sqrt(1000) * 100) => 100개 밖에 보지 않음, 1억 넘지 않음

# +)
# 그러나 엄청 많은 수를 소수인지 아닌지 판별하려면, 그리고 그 수가 크다면 O(sqrt(N) * N)
# 이걸 줄이는 게 에라토스테네스의 체 nlogn으로 바꾼다

ans = 0
for ele in ls:
    cnt = 0
    if ele == 1:
        continue
    for num in range(2, int(ele ** 0.5)+1):
        if ele % num == 0:
            break
    else:
        ans += 1

print(ans)