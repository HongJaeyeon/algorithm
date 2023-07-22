import sys
import math
input = sys.stdin.readline

selected = [-1 for i in range(6)]
def recur(depth, start):
    global ls
    if depth == 6:
        print(" ".join(map(str, selected)))
        return

    for i in range(start, len(ls)):
        selected[depth] = ls[i]
        recur(depth+1, i+1)

while True:
    ls = list(map(int, input().strip().split()))
    if len(ls) == 1 and ls[0] == 0:
        break
    recur(0, 1)
    print()