import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    cnt = 1
    maxValue = -float('inf')
    numbers = deque([i for i in range(n)])
    orders = deque(ls)
    flag = False

    while numbers:
        maxValue = -float('inf')

        for i in range(len(orders)):
            maxValue = max(maxValue, orders[i])

        for _ in range(n):
            curNum = numbers.popleft()
            curOrd = orders.popleft()

            if maxValue == curOrd:
                if curNum == m:
                    flag = True
                    print(cnt)

                else:
                    cnt += 1

                break

            else:
                numbers.append(curNum)
                orders.append(curOrd)

        if flag:
            break