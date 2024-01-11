R, C = map(int, input().split())
dir = [[-1,0], [0, 1], [1,0], [0, -1]]
cr, cc, cd, = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(R)]
clean = [[False for _ in range(C)] for _ in range(R)]

# 현재 위치가 청소 되었는지 확인
def checkCurClean():
    return clean[cr][cc]

# 현재 위치 청소
def cleanCur():
    clean[cr][cc] = True

# 현재 위치에서 4방항 중 청소되지 않은 빈 칸이 없는지 확인
# 청소 해야하면 True
def checkArroundClean():
    shouldClean = False

    for d in dir:
        nr = cr + d[0]
        nc = cc + d[1]
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            continue

        if ls[nr][nc] == 1:
            continue

        if not clean[nr][nc]:
            shouldClean = True

    return shouldClean

# 방향을 유지하면서 한칸 뒤로 이동
def moveBack():
    global cr, cc
    tod = (cd + 2) % 4
    cr += dir[tod][0]
    cc += dir[tod][1]

# 뒤쪽 칸이 벽이라 후진할 수 없는지 확인
# 후진 할 수 있으면 True
def checkBack():
    tod = (cd + 2) % 4
    nr = cr + dir[tod][0]
    nc = cc + dir[tod][1]

    if nr < 0 or nc < 0 or nr >= R or nc >= C:
        return False

    if ls[nr][nc] == 1:
        return False

    return True

# 반시계 방향으로 90도 회전
def rotate():
    global cd
    cd = (cd + 3) % 4

# 앞쪽 칸이 청소되지 않은 빈 칸인지 확인
# 청소 되지 않은 빈칸이면 True
def checkForwardClean():
    nr = cr + dir[cd][0]
    nc = cc + dir[cd][1]

    if nr < 0 or nc < 0 or nr >= R or nc >= C:
        return False

    if ls[nr][nc] == 1:
        return False

    if clean[nr][nc]:
        return False

    return True

# 한 칸 전진
def moveforward():
    global cr, cc
    cr += dir[cd][0]
    cc += dir[cd][1]

cnt = 0
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not checkCurClean():
        cleanCur()
        cnt += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if not checkArroundClean():
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if checkBack():
            moveBack()
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        while True:
            # 반시계 방향으로 90도 회전한다.
            rotate()
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if checkForwardClean():
                moveforward()
                break
                
print(cnt)