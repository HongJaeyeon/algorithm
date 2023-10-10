def solution(n, m, section):
    cnt = 1
    pre = section[0]
    
#     [1, 5], 4
    
    for cur in section:
        if cur - pre >= m:
            pre = cur
            cnt += 1
        
    return cnt