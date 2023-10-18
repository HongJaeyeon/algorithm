import sys
input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
selected = []

def recur(idx, cnt):
    if idx == N: #모든 들어 올 수 있는 수를 다보고
        if cnt == M: #뽑은 자리수가 M과 같다면
            print(*selected)
        return
    selected.append(ls[idx])
    recur(idx+1, cnt+1)
    selected.pop()
    recur(idx+1, cnt)

recur(0, 0)
