import sys

input = lambda: sys.stdin.readline().strip()
# sys.stdin = open("res/tc.txt")
n, m = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(n)]
chicken = [[r,c] for r in range(n) for c in range(n) if ls[r][c] == 2]
home = [[r, c] for r in range(n) for c in range(n) if ls[r][c] == 1]

minValue = float('inf')

def calMinDist(selected):
    minList = [float('inf') for _ in range(len(home))]
    for idx, h in enumerate(home):
        hr, hc = h[0], h[1]
        for sr, sc in selected:
            minList[idx] = min(minList[idx], abs(hr-sr) + abs(hc-sc))
    return sum(minList)

def recur(idx, selected, selectCnt):
    global minValue
    if selectCnt == m or idx == len(chicken):
        minValue = min(minValue, calMinDist(selected))
        return

    # 해당 치킨 집을 선택 안하기
    recur(idx+1, selected, selectCnt)

    # 해당 치킨 집을 선택
    recur(idx+1, selected + [chicken[idx]], selectCnt+1)

recur(0, [], 0)
print(minValue)