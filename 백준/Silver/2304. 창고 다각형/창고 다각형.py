import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()

ls = [0] * 1111
for _ in range(n):
    a, b = map(int, input())
    ls[a] = b

max_prefix = [0] * 1111 # max_prefix[i] == i까지 봤을 때의 최고 왼쪽의 높이
max_suffix = [0] * 1111 # max_suffix[i] == i까지 봤을 때의 최고 오른쪽 높이
ans = 0

for i in range(1, 1001):
    max_prefix[i] = max(max_prefix[i-1], ls[i])

for i in range(1, 1001)[::-1]:
    max_suffix[i] = max(max_suffix[i+1], ls[i])

for i in range(1, 1001):
    ans += min(max_prefix[i], max_suffix[i])

print(ans)