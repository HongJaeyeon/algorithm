import sys
input = lambda: sys.stdin.readline().strip()
tc = int(input())

for i in range(tc):
    a, b = map(int, input().split())
    print("Case #%d: %d" % (i + 1, a + b))