import math
import sys

input = lambda: sys.stdin.readline().strip().split()
n, m = map(int, input())
ls = [list(map(int, input())) for _ in range(3)]
visited = [False for _ in range(3)]
minValue = float('inf')

def recur(depth, pre_x, pre_y, dist):
    global minValue
    if depth == len(ls):
        minValue = min(minValue, dist)
        return

    for i in range(len(ls)):
        if visited[i]:
            continue

        visited[i] = True
        recur(depth+1, ls[i][0], ls[i][1], dist+math.sqrt((ls[i][0]-pre_x) ** 2 + (ls[i][1] - pre_y) ** 2))
        visited[i] = False

recur(0,n,m,0)
print(math.floor(minValue))