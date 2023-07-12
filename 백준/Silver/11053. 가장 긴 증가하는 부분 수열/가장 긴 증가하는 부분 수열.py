import sys

n = int(input())
input = lambda: sys.stdin.readline().strip().split()

ls = list(map(int, input()))

#memo[i][0] = 인덱스 i까지 봤을 때 가능한 cnt, memo[i][1] = 인덱스 i까지 봤을 때 제일 큰 수
memo = [1 for _ in range(n)]
memo[0] = 1

for i in range(1, n):
    for j in range(i):
        # i보다 앞에 더 작은 값이 있을 때
        # maxValue = -float('inf')
        if ls[i] > ls[j]:
            memo[i] = max(memo[i], memo[j] + 1)
        #아무 뒤에도 못 붙으면 (내 앞에 나보다 작은게 없으면) 나부터 시작

print(max(memo))
