import sys

#조합은 visited 체크 안해도 되어서 바로 숫자를 nums(뽑은 배열)에 넣었지만 순열은 방문 체크 해야하기 때문에 idx로 넣음
# ls = [9,7,9,1] 인 경우 [9,9] [9,9] 두 번 나오지 않게 -> 인덱스 방문 체크 외에도 다른 중복 체크 해야함
def perm(depth):
    if depth == r:
        tmp = []
        for idx in nums:
            tmp.append(ls[idx])
        tmp = tuple(tmp) # list to tuple
        dic[tmp] = dic.get(tmp, 0) + 1
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        nums[depth] = i
        perm(depth+1)
        visited[i] = False

n, r = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
ls.sort()
dic = {}
visited = [False for _ in range(n)]
nums = [-1 for _ in range(r)]
perm(0)

for k in dic.keys():
    print(" ".join(map(str, k)))