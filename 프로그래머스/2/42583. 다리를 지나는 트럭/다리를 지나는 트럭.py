from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    queue = deque()
    i = 1
    n = len(truck_weights)
    
    queue.append(truck_weights[0])
    current_weight = truck_weights[0] # 현재 다리 위에 있는 총 무게
    
    while queue:        
        if len(queue) == bridge_length:
            out_weight = queue.popleft()
            current_weight -= out_weight
            
        if i >= n and current_weight == 0:
            break
            
        if len(queue) < bridge_length:            
            if i < n and current_weight + truck_weights[i] <= weight:
                queue.append(truck_weights[i])
                current_weight += truck_weights[i]
                i+=1
            else:
                queue.append(0)
        
        answer+=1
    
    return answer + 1