tc = int(input())
for _ in range(tc):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = 0
    maxValue = -float('inf')

    for i in reversed(range(len(ls))):
        if maxValue == ls[i]:
            continue

        if maxValue > ls[i]:
            ans += (maxValue - ls[i])

        if maxValue < ls[i]:
            maxValue = ls[i]

    print(ans)