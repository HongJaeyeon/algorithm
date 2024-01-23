import sys
input = lambda : sys.stdin.readline().strip()
tc = int(input())
for _ in range(tc):
    N = int(input())
    
    ls = list(map(int, input().split()))
    ls.sort()
    ans = 0
    st = set(ls)

    for s in range(N):
        for e in range(N):
            if s == e:
                continue
            if (ls[s] + ls[e]) / 2 in st:
                ans += 1
                
    print(ans//2)