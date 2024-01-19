import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())

cnt = N
cnt += (N-2)

if N == 1:
    cnt = 1
    
print(cnt)