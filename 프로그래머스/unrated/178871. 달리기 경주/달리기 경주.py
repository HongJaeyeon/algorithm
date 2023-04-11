def solution(players, callings):
    #(50,000 * 1,000,000)
    # # 1초에 1억
    # for call in callings:
    #     for i in range(len(players)):
    #         if call == players[i]:
    #             tmp = players[i-1]
    #             players[i-1] = players[i]
    #             players[i] = tmp
    #             break
    # return players
    
    # callings되면 자기 인덱스에서 -1해주고 그 앞 인덱스는 +1해주면됨 -> 인덱스를 저장할 배열을 따로 만들어봄
    
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
        
    for call in callings:
        callIdx = dic[call]
        players[callIdx-1], players[callIdx] = players[callIdx], players[callIdx-1]
        
        dic[call] -= 1
        dic[players[dic[call]]] += 1
        
        
        print(players)
        print(dic)
        
#     dic = {}
#     for i in range(len(players)):
#         dic[players[i]] = i
        
#     for call in callings:
#         callIdx = dic[call] #지금 불린 애
#         callIdx_Pre = dic[players[dic[call]]-1] # 지금 불린 애 앞의 순위 었던 애
#         callIdx -= 1
#         dic[call] -= 1 #지금 인덱스
#         dic[players[dic[call]]-1] += 1
        
        
#         tmp = players[dic[call]]
#         dic[players[dic[call]]] = players[dic[call]]
#         players[dic[call]] = tmp
#         print(dic)

    # ans = []
    # for i in dic.keys():
        # players[dic[i]] = i
    return players
    