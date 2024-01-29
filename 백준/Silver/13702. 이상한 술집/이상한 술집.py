import sys

N, K = map(int, sys.stdin.readline().strip().split())
ans = 0
drinks = list(int(input()) for _ in range(N))
start = 1
end = pow(2, 31) - 1

while start <= end:
    mid = (start + end) // 2
    person = 0

    for d in drinks:
        person += d // mid

    if person >= K:
        start = mid + 1
        ans = mid
        
    else:
        end = mid - 1

print(ans)