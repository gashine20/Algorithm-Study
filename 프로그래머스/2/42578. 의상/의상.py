def solution(clothes):
    answer = 1
    dicts = {}
    
    for cloth, cloth_type in clothes:
        if cloth_type in dicts.keys():
            dicts[cloth_type] += 1
        else:
            dicts[cloth_type] = 1
    
    for type_count in dicts.values():
        answer *= (type_count +1)
        
    return answer-1