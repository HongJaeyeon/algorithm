import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
shops = list(map(int, input().split()))
eat = 0
shopIdx = 0
cnt = 0
while True:
    if shopIdx >= n:
        break

    if eat == shops[shopIdx]:
        eat = (eat + 1) % 3
        shopIdx += 1
        cnt += 1

    else:
        shopIdx += 1

print(cnt)