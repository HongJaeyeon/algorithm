n = int(input())
tg = int(input())
ls = list(map(int, input().split()))

s = 0
e = len(ls)-1
ls.sort()
sumValue = ls[0] + ls[e]
ans = 0

while s < e:
    # print("sumValue", sumValue)
    # print(ls[s], ls[e])
    if sumValue > tg:
        sumValue -= ls[e]
        e -= 1
        sumValue += ls[e]

    elif sumValue < tg:
        sumValue -= ls[s]
        s += 1
        sumValue += ls[s]

    else:
        ans += 1
        sumValue -= ls[s]
        s += 1
        sumValue += ls[s]

print(ans)