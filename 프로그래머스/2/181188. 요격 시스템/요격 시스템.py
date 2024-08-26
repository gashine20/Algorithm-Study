def solution(targets):
    answer = 0
    targets.sort(key = lambda x : [x[1],x[0]]) # 2번째 인자, e를 오름차순으로 그다음엔 1번째 인자를 오름차순으로
        
    e = 0
    for target in targets:
        if target[0] >= e:
            answer+=1
            e = target[1]
    
    
    return answer