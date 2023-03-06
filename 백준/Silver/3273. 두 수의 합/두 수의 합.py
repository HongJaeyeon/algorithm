import itertools
import sys

def main():
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    X = int(input())

    # for문  - 시간 초과

    # combi - 메모리 초과
    # cnt = 0
    # for a, b in list(itertools.combinations(arr, 2)):
    #     if a + b == X : cnt += 1

    #투포인터 O(n) start와 end가 서로 끝으로 가는 상황이 최악
    #정렬 후, 하나는 0 하나는 0orN-1 가르키는 포인터 선언
    #해당 인덱스에 해당하는 값들의 합보다 작다면 / 크다면 / 같다면 조건 나누기

    arr.sort()
    start = 0
    end = N-1
    cnt = 0
    while (start < end):
        if arr[start] + arr[end] < X : start += 1
        elif arr[start] + arr[end] == X :
          cnt +=1
          start += 1
          end -= 1
        else : end -= 1
    print(cnt)


if __name__ == '__main__':
    main()