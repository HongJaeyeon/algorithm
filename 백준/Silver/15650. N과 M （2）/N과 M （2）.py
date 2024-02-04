N, M = map(int, input().split())

selected = []
visited = [0] * (N+1)
nums = [i for i in range(1, N+1)]

# 모든 조합은 뽑고 안 뽑고로 바꿀 수 있다. 한 자리당 모든 수 보기 vs 모든 수당 뽑고 안 뽑기 => 시간 복잡도도 뒤에가 유리
# 탁쌤은 뽑고 안 뽑고를 좋아하신다.
# 주의 ! 뽑고 안 뽑고는 depth 자체를 인덱스로 쓰기 때문에 for문을 돌지 않는다.

def recur(idx, cnt):
	if idx == N:
		if cnt == M:
			print(*selected)
		return
	selected.append(nums[idx])
	recur(idx+1, cnt+1)
	selected.pop()
	recur(idx+1, cnt)
recur(0, 0)