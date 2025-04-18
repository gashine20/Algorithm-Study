def solution(food):
    result = []
    for i in range(1, len(food)):
        count = food[i] // 2
        for _ in range(count):
            result.append(str(i))
        
    result_reversed = sorted(result, reverse = True)
    
    answer = ''.join(result)
    answer2 = ''.join(result_reversed)
    
    return answer + '0' + answer2