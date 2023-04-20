def solution(genres, plays):
    dic_cnt = {}
    dic_song = {}
    idx = 0
    answer = []
    
    for g, p in zip(genres, plays):
        dic_cnt[g] = dic_cnt.get(g, 0)
        dic_cnt[g] += p
        
        dic_song[g] = dic_song.get(g, [])
        dic_song[g].append([idx, p])
        
        idx+=1
    
    dic_cnt = sorted(dic_cnt.items(), key = lambda x: -x[1])
    
    for key, value in dic_song.items():
        value.sort(key = lambda x: -x[1])
        
    
        
    print(dic_cnt)
    print(dic_song)
    
    #sorted 때문에 dic의 자료구조 잃고 list됨
    for k, v in dic_cnt:
        for i in range(len(dic_song[k])):
            if i==2: break
            answer.append(dic_song[k][i][0])
            
    return answer