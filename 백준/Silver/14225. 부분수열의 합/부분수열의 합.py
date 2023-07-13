import sys

input = lambda: sys.stdin.readline().strip()
n = int(input())
ls = list(map(int, input().split()))
tmp = []
# 부분집합, 해당 원소를 뽑고 안 뽑고, 몇개를 뽑을 지 알 수 없어서 selected 배열을 만들기 보다는
# 원하는 값을 실시간으로 계산

# 20개의 합으로 나올 수 있는 최대 수 = 2,000,000 < 100,000,000

def recur(idx, sumValue):
    global tmp
    if idx == n:
        tmp.append(sumValue)
        return

    #뽑았을 때
    recur(idx+1, sumValue + ls[idx])

    #안 뽑았을 때
    recur(idx+1, sumValue)

recur(0, 0)
tmp = set(tmp)

for i in range(2_000_000):
    if i in tmp:
        continue
    else:
        print(i)
        break
