def solution(people, limit):
    people.sort(key = lambda x: -x)
    print(people)
    s = 0
    e = len(people)-1
    cnt = 0
    while(s <= e):
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            
        else:
            s += 1
        cnt += 1
        
    return cnt