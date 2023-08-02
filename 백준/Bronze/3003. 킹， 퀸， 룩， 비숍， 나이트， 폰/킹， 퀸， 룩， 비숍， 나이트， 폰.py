import sys
ls = list(map(int, sys.stdin.readline().strip().split()))
tmp = [1,1,2,2,2,8]
for j in range(len(tmp)):
    print(tmp[j] - ls[j], end=" ")

