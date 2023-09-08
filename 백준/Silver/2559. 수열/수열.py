import sys

input = lambda: sys.stdin.readline().strip().split()
n, k = map(int, input())
ls = list(map(int, input()))

prefix_sum = [0] * (n+1)

for idx, ele in enumerate(ls):
    prefix_sum[idx+1] = prefix_sum[idx] + ele

maxValue = -float('inf')
for i in range(k, len(ls)+1): #day: 연속된 날짜수 1~n
    maxValue = max(maxValue, prefix_sum[i]-prefix_sum[i-k])

print(maxValue)