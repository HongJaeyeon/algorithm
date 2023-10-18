import sys
import itertools

n, m = map(int, sys.stdin.readline().strip().split())

comb = itertools.combinations_with_replacement([i for i in range(1, n+1)], m)

for i in comb:
    print(' '.join(map(str, i)))
