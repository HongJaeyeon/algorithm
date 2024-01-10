import sys
input = lambda: sys.stdin.readline().strip().split()

N, K = map(int, input())
ls = [list(map(int, input())) for _ in range(N)]

if N == K:
    print(0)
    sys.exit()
    

minValue = float('inf')
selected = [False for _ in range(N)]

# 모든 조합 문제는 뽑고 안 뽑고로 바꿀 수 있다.
def recur(idx, cnt):
    global ls, minValue

    # 가지치기 - 이미 K개를 다 뽑았을 때
    if cnt == K:
        notSelectedList = []
        selectedList = []
        for i in range(N):
            if not selected[i]:
                notSelectedList.append(ls[i])
            else:
                selectedList.append(ls[i])

        # 가장 가까운 대피소(min)의 거리가 가장 큰 것(max)
        maxDist = -float('inf')
        for cr, cc in notSelectedList:
            minDist = float('inf')
            for dr, dc in selectedList:
                minDist = min(minDist, abs(dr - cr) + abs(dc - cc))
            maxDist = max(maxDist, minDist)

        minValue = min(minValue, maxDist)
        return

    # 종료 조건 - 모든 인덱스를 다 봤을 때
    if idx == N:
        return

    # 해당 인덱스의 좌표를 뽑는 경우
    selected[idx] = True
    recur(idx+1, cnt+1)

    # 해당 인덱스의 좌표를 안 뽑는 경우
    selected[idx] = False
    recur(idx+1, cnt)

recur(0, 0)
print(minValue)