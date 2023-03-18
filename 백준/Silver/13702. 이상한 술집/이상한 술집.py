import sys

N, K = map(int, sys.stdin.readline().strip().split())
ans = 0
drinks = list(int(input()) for _ in range(N))
start = 1
end = pow(2, 31) - 1
# mid = 막걸리의 양
while start <= end:
    mid = (start + end) // 2
    person = 0
    #나머지는 버려야하니까 합계로 구하지 않고 각 값을 따로 돌림
    for d in drinks:
        person += d // mid

    # 인원이 같다해도 막걸리 양을 더 늘릴 수 있어서 break 걸면 안됨 -> mid를 더 커지게 하는 조건에 같이 넣어야함
    # if K == person:

    # 해당 양 (mid)로 나누면 더 많은 사람이 나눠먹는다 -> mid가 더 커져야함
    if person >= K:
        start = mid + 1
        ans = mid
    # elif person < K:
    else:
        end = mid - 1

print(ans)