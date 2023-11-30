import sys
input = lambda: sys.stdin.readline().split()

while True:
    a, b = map(int, input())
    if a == 0 and b == 0:
        break
    print(a + b)