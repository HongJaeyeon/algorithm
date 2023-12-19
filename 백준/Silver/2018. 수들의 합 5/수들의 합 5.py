tg = int(input())
s = 1
e = 1
sumValue = 1
cnt = 0

while s <= e:
    # print("sumValue", sumValue, "s", s, "e", e)
    if tg > sumValue:
        e += 1
        sumValue += e
    elif tg < sumValue:
        sumValue -= s
        s += 1
    else:
        cnt += 1
        sumValue -= s
        s += 1
print(cnt)