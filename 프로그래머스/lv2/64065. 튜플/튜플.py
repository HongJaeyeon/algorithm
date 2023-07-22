def solution(s):
    # 원소가 1개 있는 튜플 -> result의 첫번째 수
    ## 원소가 2개 있는 튜플에서 처음 나온 수 -> result의 두번째 수
    ### 원소가 3개 있는 튜플에서 처음 나온 수 -> result의 세번째 수
    # -> 제일 많이 등장한 게 result의 첫번째 수
    answer = []
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(",")
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0) + 1
        
    a = sorted(dic.items(), key=lambda x: -x[1])
    for i in a:
        answer.append(int(i[0]))
    return answer