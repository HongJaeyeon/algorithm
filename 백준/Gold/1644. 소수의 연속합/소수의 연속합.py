import math

target = int(input())
ls = []
# for i in range(2, target+1): # 2부터 n까지의 수들 중에 (1은 어차피 소수가 아니므로 2부터 시작, 문제 조건에서 자기 자신도 넣음)
#     for j in range(2, math.ceil(math.sqrt(target))+1): #소수인 것을 판별(소수: 1과 자기 자신으로만 나누어져야함)
#         if i != j and i % j == 0: #나누어 떨어진다면 소수가 아니다
#             break
#     #break를 만나지 않았다면
#     else:
#         ls.append(i)


tmp = [True for _ in range(target+1)]
tmp[0] = False
tmp[1] = False
for i in range(2, math.ceil(math.sqrt(target))+1): #소수인 것을 판별(소수: 1과 자기 자신으로만 나누어져야함)
    j = 2
    if tmp[i]:
        # i로 나누어지면 i의 모든 배수들로도 나누어짐 -> 소수가 아님
        while i*j <= target:
            tmp[i*j] = False
            j += 1
for i in range(len(tmp)):
    if tmp[i]:
        ls.append(i)

s = 0
e = 0
sumValue = 0
cnt = 0

while True:
    if sumValue > target:
        sumValue -= ls[s]
        s += 1
    elif sumValue < target:
        if e == len(ls):
            break
        sumValue += ls[e]
        e += 1
    else:
        cnt += 1
        sumValue -= ls[s]
        s += 1


print(cnt)