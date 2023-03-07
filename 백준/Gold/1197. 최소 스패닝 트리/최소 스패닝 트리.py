import sys

def makeset():
    global arr, v, e, parents
    for i in range(v+1):
        parents[i] = i;

def findparent(i):
    global arr, v, e, parents
    if parents[i] == i:
        return i

    #재귀, 경로 압축
    parents[i] = findparent(parents[i])
    return parents[i]

def union(i,j):
    global arr, v, e, parents

    #대표 찾기
    i = findparent(i)
    j = findparent(j)

    if i == j:
        return False

    parents[j] = i
    return True

v, e = map(int,sys.stdin.readline().strip().split())
arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(e)]
parents = [0 for _ in range(v+1)]
total = 0
cnt = 0

#무게에 대해서 정렬
arr.sort(key= lambda x : x[2])
makeset()

for start, to, weight in arr:
    if union(start, to) :
        total += weight
        cnt += 1
        if cnt == v-1 : break

print(total)