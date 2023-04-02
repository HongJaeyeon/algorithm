import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.comb(b, a))