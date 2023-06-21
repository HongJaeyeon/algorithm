import sys

input = sys.stdin.readline
n, target = map(int, input().rstrip().split())
ls = list(map(int, input().rstrip().split()))

s = 0
e = 0
sumValue = ls[0]
minValue = float('inf')
while True:
    if target > sumValue:
        e += 1
        if e == n:
            break
        sumValue += ls[e]

    else: #target <= sumValue
        sumValue -= ls[s]
        minValue = min(minValue, e-s+1)
        s += 1

print(0 if minValue == float('inf') else minValue)