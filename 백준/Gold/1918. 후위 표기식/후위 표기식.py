import sys
from collections import deque
s = list(sys.stdin.readline().rstrip())
# ")"는 어차피 들어오지를 않음
degree = {"*":3, "/":3, "+":2, "-":2, "(":1}
stack = deque()
ans = ""
for ele in s:
    # "("나타날 때까지 선입후출
    if ele == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    # 문자인 경우
    elif ele not in degree:
        ans += ele
    elif ele == "(":
        stack.append(ele)
    # 연산자인 경우
    else:
        while True:
            if stack and degree[stack[-1]] >= degree[ele]:
                ans += stack.pop()
            else:
                stack.append(ele)
                break
while stack:
    ans += stack.pop()

print(ans)