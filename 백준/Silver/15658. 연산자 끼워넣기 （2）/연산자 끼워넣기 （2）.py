import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()
ls = list(map(int, input()))
opers = list(map(int, input()))

minValue = float('inf')
maxValue = -float('inf')

def recur(depth, a, b, c, d, result):
    global minValue, maxValue
    #지금 depth에 무조건 뭘 넣긴 하는데 뭘 넣을까 문제
    if depth == n-1:
        minValue = min(minValue, result)
        maxValue = max(maxValue, result)
        return

    #해당 depth에서 여러 oper로 다 가봐야하니까 else 아닌 if
    if a:
        recur(depth + 1, a-1, b, c, d, result + ls[depth + 1])
    if b:
        recur(depth + 1, a, b-1, c, d, result - ls[depth + 1])
    if c:
        recur(depth + 1, a, b, c-1, d,  result * ls[depth + 1])
    if d:
        recur(depth + 1, a, b, c, d-1, result // ls[depth + 1]) if result >= 0 else recur(depth + 1, a, b, c, d - 1, -((-result) // ls[depth + 1]))


recur(0, opers[0], opers[1], opers[2], opers[3], ls[0])

print(maxValue)
print(minValue)