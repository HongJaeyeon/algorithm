n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()
print(*ls, sep="\n")