n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print("NO BRAINS" if a < b else "MMM BRAINS")