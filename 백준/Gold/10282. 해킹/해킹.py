import heapq

tc = int(input())
for _ in range(tc):
    n, d, c = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    dist = [float('inf') for _ in range(n+1)]
    pq = []

    for _ in range(d):
        x, y, z = map(int, input().split())
        adj[y].append([x, z])

    pq.append([0, c])
    dist[c] = 0

    while pq:
        cw, cn = heapq.heappop(pq)
        if dist[cn] < cw:
            continue

        for nxtn, nxtw in adj[cn]:
            if dist[nxtn] > dist[cn] + nxtw:
                dist[nxtn] = dist[cn] + nxtw
                heapq.heappush(pq, [dist[nxtn], nxtn])

    # 안 이어진 것은 갱신 될 수가 없다 -> inf로 남아있음
    # 이어진 것들 중에서 dist[i]는 i까지의 최단 거리를 저장하고 있다
    # => inf가 아닌 최대값 출력
    maxValue = -float('inf')
    cnt = 0
    for ele in dist:
        if ele == float('inf'):
            continue
        maxValue = max(maxValue, ele)
        cnt += 1
        
    print(cnt, maxValue)