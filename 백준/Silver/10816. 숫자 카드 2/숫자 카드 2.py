import sys
# sys.stdin = open("res/tc.txt")

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().rstrip().split()))
m = int(input())
ls2 = list(map(int, input().rstrip().split()))


ls.sort()
for target in ls2:
    # print("Target", target)

    s = 0
    e = n - 1
    right = -1
    # target과 같은 수중 가장 오른쪽 인덱스인 것 찾기
    while s <= e:
        mid = (s + e) // 2
        if target > ls[mid]:
            s = mid+1
        elif target < ls[mid]:
            e = mid-1
        else:
            right = mid
            # 저장해놓고 같은 수 중에 더 오른쪽인 것이 있나 찾으러 가기
            s = mid+1

    s = 0
    e = n - 1
    left = 0
    while s <= e:
        mid = (s + e) // 2
        if target > ls[mid]:
            s = mid+1
        elif target < ls[mid]:
            e = mid-1
        else:
            left = mid
            # 저장해놓고 같은 수 중에 더 왼쪽인 것이 있나 찾으러 가기
            e = mid-1
    # print("ls", ls)
    # print("right", right)
    # print("left", left)

    print(right - left + 1, end=" ")
    # print()