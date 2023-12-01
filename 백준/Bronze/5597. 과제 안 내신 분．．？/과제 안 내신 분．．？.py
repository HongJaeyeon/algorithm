visited = [False for _ in range(30)]
for i in range(28):
    n = int(input())
    visited[n-1] = True

for i in range(30):
    if not visited[i]:
        print(i+1)