import sys
tc = int(input())

for i in range(tc):
    k, n = map(int, input().split())
    ls = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(4)]
    minGap = float('inf')
    ans = 0
    ls1 = []
    for i in range(n):
        for j in range(n):
            ls1.append(ls[0][i] + ls[1][j])


    ls2 = []
    for i in range(n):
        for j in range(n):
            ls2.append(ls[2][i] + ls[3][j])

    ls1.sort()
    ls2.sort()

    s = 0
    e = len(ls1) - 1
    # print("----", tc, "-----")
    while s <= len(ls1)-1 and 0 <= e:
        # print(s, ls1[s], e, ls2[e])
        sumValue = ls1[s] + ls2[e]

        if minGap > abs(k - sumValue):
            minGap = abs(k - sumValue)
            ans = sumValue

        elif minGap == abs(k - sumValue):
            if ans > sumValue:
                ans = sumValue
        # print("abs(k - sumValue)", abs(k - sumValue))
        # print("sumValue", sumValue)
        # print("minGap", minGap)
        # print("ans", ans)

        # 그냥 완전 똑같은 수가 되었다면 더 볼 필요 없음
        if minGap == 0:
            break

        # 그게 아니라면, 더 근접한 수가 나올 수 있으니 더 해봐야함
        if k > sumValue: #값을 늘려봐야함
            s += 1

        elif k < sumValue: # 값을 줄여봐야함
            e -= 1

    print(ans)