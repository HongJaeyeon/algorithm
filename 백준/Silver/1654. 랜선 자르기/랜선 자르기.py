import sys
N, K = map(int, sys.stdin.readline().strip().split())
lensuns = [int(input()) for _ in range(N)]

start = 0
end = pow(2, 31) - 1
ans = 0


# 추측값 == 랜선의 길이
# 조건 == 해당 랜선의 길이일 때 k개의 랜선은 나와야 한다.

while start <= end:
    mid = (start + end) // 2
    num_lensun = sum ( [lensun // mid for lensun in lensuns])
    
    if num_lensun >= K:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
print(ans)

'''
4 11
802
743
457
539
'''