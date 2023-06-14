import sys

def findscore(a,b):
    sumA = 0
    for i in a:
        for j in a:
            sumA += maps[i][j]

    sumB = 0
    for i in b:
        for j in b:
            sumB += maps[i][j]

    global minValue
    minValue = min(minValue, abs(sumA-sumB))

# 부분 집합 2^n 시간 복잡도, n==30까지 가능
def subset(idx):
    a = []
    b = []
    if idx == N:
        for i in range(len(isSelected)):
            if isSelected[i]:
                a.append(i)
            else:
                b.append(i)

        # 팀에 무조건 한 명은 있도록
        if len(a) == N or len(b) == N:
            return

        findscore(a, b)
        return

    # 구성에 포함시키고 재귀 보내기
    isSelected[idx] = True
    subset(idx+1)

    # 구성에 포함시키지 않고 재귀 보내기
    isSelected[idx] = False
    subset(idx+1)


# sys.stdin = open("res/15661.txt")

N = int(input())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
isSelected = [False for _ in range(N)]
minValue = float('inf')

subset(0)

print(minValue)