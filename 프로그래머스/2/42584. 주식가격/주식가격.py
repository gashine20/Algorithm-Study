from collections import deque

def solution(prices):
    answer = []
    
    queue = deque() # {초, 가격}
    
    for i, price in enumerate(prices):
        queue.append([i+1, price])
        
    queue.append([len(prices), 0])
    
    # print(queue)
    
    while len(queue) > 1:
        now = queue.popleft()
        
        for next_item in queue:
            if(next_item[1] < now[1]):
                # print("now:", now, " next:", next_item)
                answer.append(next_item[0] - now[0])
                break
                
    return answer