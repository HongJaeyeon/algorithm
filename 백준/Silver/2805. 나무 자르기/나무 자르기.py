import sys
input = sys.stdin.readline
#특정 구간의 최대 or 최소값을 구하는 문제이며 수가 정렬되어았을 때-> 이진탐색 접근

n, m = map(int, input().strip().split())
trees = list(map(int, input().strip().split()))
trees.sort()
#계속 추측해봐야하는 값: 절단기 높이
# left = trees[0] 자르는 높이는 최소 높이의 나무보다 더 작을 수 있음
left = 0
# 추측해야하는 값 (높이)는 trees의 배열 범위 내에서 움직이지 않음  -> 그냥 상수를 넣어야함
# right = trees[-1]
# 나무의 높이는 1,000,000,000보다 작거나 같다
right = int(1e9)
ans = 0
while left <= right:
    #h == mid
    h = (left + right) // 2
    sumValue = 0
    for tree in trees:
        if tree > h:
            sumValue += (tree - h)

    if sumValue > m:
        # sum을 m이상, m과 최대한 가깝게 만드는 h의 최대값을 구하는 것이 목표, 다음이 어떻게 될지 모르니까 일단 저장해둔다
        ans = h
        left = h + 1

    # 절단기의 크기 (h)를 높일수록 sum은 더 작아지므로 sumValue가 m보다 작다면 (기준 미달) 예측 h를 높여야한다
    elif sumValue < m:
        right = h - 1

    else:
        print(h)
        break
else:
	print(ans)