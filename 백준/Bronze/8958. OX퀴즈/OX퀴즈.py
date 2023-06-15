import sys

n = int(input())

for _ in range(n):
    s = list(sys.stdin.readline())
    cnt = 0
    sumValue = 0
    for ele in s:
        sumValue += cnt
        if ele == "O":
            cnt += 1
        else:
            cnt = 0
    print(sumValue)