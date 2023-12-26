n = int(input())
ls = [int(input()) for _ in range(n)]
# ls.sort()
# print(n, ls)
ans = 0
for ele in ls:
    # print("ele", ele)
    cnt = 0
    for i in range(5):
        if ele + i in ls:
            cnt += 1
        # print("A", ele + i)
    # print("cnt", cnt)
    ans = max(cnt, ans)

print(5-ans)