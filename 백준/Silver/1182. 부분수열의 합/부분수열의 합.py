import sys

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())
ls = list(map(int, input()))
ans = 0

def subset(idx, sumValue):
    global ans
    #음수와 양수가 둘다 나올 수 있기에 다음에 값이 m보다 더 작아질지, 커질지 예측하지 못해서, 가지치기는 못함

    if idx == n:
        if sumValue == m:
            ans += 1
        return

    subset(idx+1, sumValue + ls[idx])
    subset(idx+1, sumValue)

subset(0,0)

if m == 0:
    ans -= 1
print(ans)