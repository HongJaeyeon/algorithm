import sys

input = lambda: sys.stdin.readline().strip().split()
m, n = map(int, input())
ls = list(input())
ls.sort()

def recur(depth, result):
    if depth == n:
        cnt = 0
        for ele in result:
            if ele not in ["a", "e", "i", "o", "u"]:
                cnt += 1
        if len(result) == m and cnt !=m and cnt >= 2:
            print(result)
        return

    recur(depth+1, result + ls[depth])
    recur(depth+1, result)

recur(0, "")