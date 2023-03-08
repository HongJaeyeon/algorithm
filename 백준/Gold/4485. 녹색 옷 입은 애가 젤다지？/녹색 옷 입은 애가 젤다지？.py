import sys
import heapq
N = int(input())
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 0
#한 좌표에서의 상하좌우를 인접한 노드로 보고 다익스트라를 푼다


while N != 0:
    cnt += 1
    maps = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0] = maps[0][0] #자기에서 자기로 가는 것은 0이 아니라 자기 좌표의 값
    pq = [[maps[0][0], 0, 0]] #w, r, c

    while pq:
        w, r, c = heapq.heappop(pq) #현재 노드

        if r == N-1 and c == N-1:
            print(f'Problem {cnt}: {dist[r][c]}')
            break

        if dist[r][c] < w : continue #옛정보

        for d in dir: #nr, nc 인접 노드
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            # #이것도 방문 체크 해야하나?
            # if visited[nr][nc] :
            #     continue

            if dist[nr][nc] > maps[nr][nc] + w:
                dist[nr][nc] = maps[nr][nc] + w  #newCost
                heapq.heappush(pq, [dist[nr][nc], nr, nc])

    N = int(input())
















# while pq:
#     w, r, c = heapq.heappop(pq)
#     sum += w
#     print(w)
#     #pq는 레벨마다 초기화
#     pq = []
#     for d in dir:
#         nr = r + d[0]
#         nc = c + d[1]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         if visited[nr][nc]:
#             continue
#         #맨 마지막 좌표는 제일 우선 순위가 크다
#         if nr == N-1 and nc == N-1:
#             sum += maps[nr][nc]
#             break
#         heapq.heappush(pq, [maps[nr][nc], nr, nc])
#         visited[nr][nc] = True
#
# print(sum)


# 같은 레벨에서 같은 수가 나왔을 때는 어느 것을 가야할지 모른다. -> 갈래가 갈라져야한다
# while pq:
#     w, r, c = heapq.heappop(pq)
#     sum += w
#     print(w)
#     #pq는 레벨마다 초기화
#     pq = []
#     for d in dir:
#         nr = r + d[0]
#         nc = c + d[1]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         if visited[nr][nc]:
#             continue
#         #맨 마지막 좌표는 제일 우선 순위가 크다
#         if nr == N-1 and nc == N-1:
#             sum += maps[nr][nc]
#             break
#         heapq.heappush(pq, [maps[nr][nc], nr, nc])
#         visited[nr][nc] = True
#
# print(sum)

# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 9
# 0
# 1
# 2
# 1
# 1
# 1
# 5
# 3
# 3
# 5
# 3
# 1
# 3
# 42


#맨 마지막은 우선순위가 제일 큰데, 맨 마지막보다 더 작은 수가 있으면 그게 먼저 들어온다
# while pq:
#     w, r, c = heapq.heappop(pq)
#     print(w)
#     sum += w
#     if r == N-1 and c == N-1:
#         break
#
#     #pq는 레벨마다 초기화
#     pq = []
#     for d in dir:
#         nr = r + d[0]
#         nc = c + d[1]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         if visited[nr][nc]:
#             continue
#         heapq.heappush(pq, [maps[nr][nc], nr, nc])
#         visited[nr][nc] = True
#

# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
#
# #더 먼저 들어온 5가 7대신 나옴 -> 레벨에 따라 초기화하는 부분 있어야함
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3
# 3
# 2
# 5
# 4
# 1
# 7
#
#
# import sys
# import heapq
# N = int(input())
# maps = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
# dir = [[-1,0],[1,0],[0,-1],[0,1]]
# visited = [[False for _ in range(N)] for _ in range(N)]
# pq = [[maps[0][0],0,0]]
# visited[0][0] = True
# sum = 0
# while pq:
#     w, r, c = heapq.heappop(pq)
#     print(w)
#     sum += w
#     if r == N-1 and c == N-1:
#         break
#     for d in dir:
#         nr = r + d[0]
#         nc = c + d[1]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N:
#             continue
#         if visited[nr][nc]:
#             continue
#         heapq.heappush(pq, [maps[nr][nc], nr, nc])
#         visited[nr][nc] = True
#
# print(sum)