n = int(input())
newNum = n
cnt = 1

while True:
    left = newNum // 10
    right = newNum % 10
    # print("left", left, "right", right)
    tmp = left + right
    newNum = int(str(right) + str(tmp % 10))
    # print("tmp", tmp)
    # print("newNum", newNum)
    if newNum == n:
        break
    cnt += 1

print(cnt)

