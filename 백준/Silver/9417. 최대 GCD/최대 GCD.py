import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()

selected = [0, 0]

def getGCD(a, b):
    if a % b == 0:
        return b
    return getGCD(b, a%b)


def combi(ls, depth, start):
    global maxValue

    if depth == 2:
        # selected.sort()
        maxValue = max(maxValue, getGCD(selected[0], selected[1]))
        return

    for i in range(start, len(ls)):
        selected[depth] = ls[i]
        combi(ls, depth+1, i+1)

for _ in range(n):
    ls = list(map(int, input()))
    maxValue = -float('inf')
    combi(ls, 0, 0)
    print(maxValue)

