import sys

def comb(depth, start):
    if depth == r:
        print(" ".join(map(str,nums))) # 2. 조인으로 합침
        return

    for i in range(start, n):
        nums[depth] = ls[i] # 1. 인덱스가 아니라 바로 수로 넣고
        #if depth >= 1 and nums[depth-1] > nums[depth]:
            #continue
        comb(depth+1, i)

n, r = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))
ls.sort()
nums = [-1 for _ in range(r)]
comb(0, 0)