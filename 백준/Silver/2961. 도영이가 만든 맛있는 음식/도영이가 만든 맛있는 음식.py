import sys
lambda input: sys.stdin.readline().strip()

N = int(input())
ls = [list(map(int, input().split())) for _ in range(N)]
minValue = float('inf')

def recur(idx, cnt, sin, sson):
    global minValue
    if idx == N:
        if cnt >= 1:
            minValue = min(minValue, abs(sin-sson))
        return
    recur(idx + 1, cnt+1, sin*ls[idx][0], sson+ls[idx][1])
    recur(idx + 1, cnt, sin, sson)

recur(0,0,1,0)
print(minValue)