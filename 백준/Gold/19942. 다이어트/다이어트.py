import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n+1)]
minValue = float('inf')
ans = []

def recur(idx, dan, je, tan, vi, cost, selected):
    global minValue, ans

    # 최소 조건을 만족하는 경우 - 이후의 값은 체크해도 사전 순으로 뒤에 속함
    if not (ls[0][0] > dan or ls[0][1] > je or ls[0][2] > tan or ls[0][3] > vi):
        # 같은 비용의 집합이 하나 이상이면 사전 순으로 가장 빠른 것을 출력
        # selected가 [1]인 것과 [1,2]인 것이 나오고, 둘이 비용이 같다면 [1]이 정답
        #  -> 그냥,,, 이퀄(=)안 넣으면 됨
        if minValue > cost:
            minValue = cost
            ans = selected
        return

    if idx == n+1: # n개에 대해서 다 뽑을지 말지 고려해보았을 때, idx=0은 limit정보라 n+1까지
        return

    # 몇 개를 뽑아야할지 모름, 뽑고 안 뽑고 -> 부분집합
    #뽑은 경우
    recur(idx+1, dan+ls[idx][0], je+ls[idx][1], tan+ls[idx][2], vi+ls[idx][3], cost+ls[idx][4], selected+[idx])

    #안 뽑은 경우
    recur(idx+1, dan, je, tan, vi, cost, selected)

recur(1, 0, 0, 0, 0, 0, [])

if ans:
    print(minValue)
    print(' '.join(map(str, ans)))
else:
    print(-1)
