import sys
from collections import deque

def main():
    N = int(input())
    for _ in range(N):
        dq = deque()
        right = True;
        l = list(sys.stdin.readline())[:-1]
        #스택 : 후입 선출
        for ele in l:
            # print(ele)
            if ele == '(':
                dq.append('(')
            else:
                if not dq:
                    right = False
                    break
                else:
                    dq.pop()

            # print(dq)

        # 위에 과정을 지나왔는데 아직도 dq에 값이 남아있다 -> 짝이 맞지 않는다
        if dq:
            right = False

        print("YES" if right else "NO")

if __name__ == '__main__':
    main()