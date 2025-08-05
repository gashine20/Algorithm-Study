from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    def play_dungeons(turn, now_k):
        nonlocal dungeons
        
        count = 0
        for t in turn:
            if now_k >= dungeons[t][0]:
                now_k -= dungeons[t][1]
                count +=1
        
        return count 
                
    turn = [i for i in range(len(dungeons))]
    for t in permutations(turn):
        answer = max(answer, play_dungeons(t, k))
    
    return answer


# 유저가 탐험할 수 있는 최대 던전을 구하라
# k: 현재 피로도
# 탐험할 수 있는가. 깊게 파고들어야 한다. dfs로 풀어보자?
# 1-2-3 또는 2-3-1 순서로해야할수도있다.