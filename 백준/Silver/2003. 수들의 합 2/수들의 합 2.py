import sys

# 연속된 수의 합 구하기
# N의 크기 10,000 / 시간 제한 0.5초 -> O(N)의 시간복잡도만 통과
# 한 배열에 투 포인터 O(N)
n, m = map(int, sys.stdin.readline().rstrip().split())
ls = list(map(int, sys.stdin.readline().rstrip().split()))

# N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
s = 0
e = 1
sumValue = ls[0]
cnt = 0

while True:
    # 1. ls[left]를 빼고 2. left를 1 증가 시킨다.
    if sumValue > m:
        sumValue -= ls[s]
        s += 1

    # 1. right 1 증가 시키고 2. ls[right]를 더해준다.
    # 이때 right가 n과 같아진다면 (ls의 길이) 반복문 탈출
    elif sumValue < m:
        if e == n:
            break
        sumValue += ls[e]
        e += 1

    # sumValue == m
    # 1. cnt를 증가 시키고 2. ls[left]를 빼고 3. left를 1 증가 시킨다.
    # 다음으로 sumValue < m 인 곳으로 감
    else:
        cnt += 1
        sumValue -= ls[s]
        s += 1

print(cnt)