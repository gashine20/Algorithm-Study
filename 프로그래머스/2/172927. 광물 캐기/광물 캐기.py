import sys

def solution(picks, minerals):
    answer = sys.maxsize
    dia = [1, 1 ,1]
    iron = [5, 1, 1]
    stone = [25, 5, 1]
    minerals_dict = {"diamond": 0, "iron": 1, "stone": 2}
    
    picks_line = [ i for i in range(3) for _ in range(picks[i])]
    max_use_picks = len(minerals)//5 + 1 if len(minerals)//5 + 1 < len(picks_line) else len(picks_line)
    
    used = [False] * len(picks_line)
    picks_example = []
    def make_permutation(path):        
        if len(path) == max_use_picks:
            picks_example.append(path[:])
            return
        
        for i in range(len(picks_line)):
            if used[i]:
                continue
            if i > 0 and picks_line[i] == picks_line[i-1] and not used[i-1]:
                continue
            
            used[i] = True
            path.append(picks_line[i])
            make_permutation(path)
            path.pop()
            used[i] = False
    
    def do_pick(picks, minerals):
        nonlocal answer
        
        i, n = 0, len(minerals)
        result = 0
        
        for pick in picks:
            j = i + 5
            while i < j and i < n:
                mineral_index = minerals_dict[minerals[i]]
                if pick == 0:
                    result += dia[mineral_index]
                elif pick == 1:
                    result += iron[mineral_index]
                elif pick == 2:
                    result += stone[mineral_index]
                i+=1
                
        answer = min(answer, result)
        
    make_permutation([])  
    # print(picks_example)

    for picks_iter in picks_example:
        do_pick(picks_iter, minerals)
        
    
    return answer