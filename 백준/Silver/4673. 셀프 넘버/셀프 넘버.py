cur = 2
visited = [False for _ in range(10_000+1)]
visited[2] = True
while True:
    # print("cur:", cur)
    sumValue = cur
    copy_cur = cur
    while True:
        # print("copy_cur", copy_cur)
        if copy_cur == 0:
            break
        sumValue += (copy_cur % 10)
        copy_cur //= 10
        # print("sumValue", sumValue)
    if sumValue > 10_000:
        break
    # print("sumValue", sumValue)
    visited[sumValue] = True
    cur += 1

for i in range(1, len(visited)):
    if not visited[i] and i <= 9993:
        print(i)