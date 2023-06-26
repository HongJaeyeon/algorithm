import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().rstrip().split()))
x = int(input())

# 정렬 100000log(100000) = 5 * 100000

ls.sort()
s = 0
e = n-1
cnt = 0
sumValue = ls[s] + ls[e]
while s<e:
    if sumValue < x:
        sumValue -= ls[s]
        s += 1
        sumValue += ls[s]

    elif sumValue > x:
        sumValue -= ls[e]
        e -= 1
        sumValue += ls[e]

    else:
        cnt += 1
        # e를 더 줄여봤자 해당 s에서 나올 수 있는 다른 경우는 없다 -> s를 늘린다
        sumValue -= ls[s]
        s += 1
        sumValue += ls[s]
print(cnt)