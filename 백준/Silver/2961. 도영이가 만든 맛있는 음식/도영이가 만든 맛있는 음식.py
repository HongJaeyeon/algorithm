import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()

ls = [list(map(int, input())) for _ in range(n)]
minValue = float('inf')
# 부분 집합은 실시간으로 결과값을 만들어낼 수 있으면, 그걸 가지고 다니면 된다.
def recur(depth, ssin, ssen):
    global minValue
    if depth == n:
        if ssen == 0:
            return
        minValue = min(minValue, abs(ssin - ssen))
        return

    #안 뽑은 경우
    recur(depth+1, ssin, ssen)
    #뽑은 경우
    recur(depth+1, ssin*ls[depth][0], ssen+ls[depth][1])

recur(0,1,0)
print(minValue)