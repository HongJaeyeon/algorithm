import sys
from itertools import permutations

#완탐 (순열) O(8!)
# n == 최대 8이므로 모든 자리수를 바꿔보며 식의 최대값을 구해본다
ans = 0
n = int(input())
ls = list(sys.stdin.readline().split())
for li in list(permutations(ls, n)):
    s = 0
    for i in range(1, n):
        s += abs(int(li[i-1]) - int(li[i]))
    ans = max(ans, s)

print(ans)