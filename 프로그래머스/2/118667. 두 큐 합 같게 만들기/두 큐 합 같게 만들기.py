from collections import deque

def solution(queue1, queue2):
    
    total_sum = sum(queue1) + sum(queue2)
    if(total_sum % 2 !=0):
        return -1
    
    limit_move = len(queue1) * 4
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    
    move = 0
    while sum1!=sum2:
        # 움직임 횟수 넘으면 break
        if limit_move == move:
            break
            
        if sum1 > sum2: # queue1 에서 queue2로
            removed = q1.popleft()
            q2.append(removed)
            # print("removed:",removed)
            sum2 += removed
            sum1 -= removed
        elif sum1 < sum2:
            removed = q2.popleft()
            q1.append(removed)
            # print("removed:",removed)
            sum1 += removed
            sum2 -= removed
            
        move+=1 
    
    if move == limit_move:
        return -1
    else:
        return move
    
    
# 처음 풀이 - 배열 시간 초과   
# def solution(queue1, queue2):
    
#     total_sum = sum(queue1) + sum(queue2)
#     if(total_sum % 2 !=0):
#         return -1
    
#     goal_sum = int(total_sum/2)
#     limit_move = len(queue1) * 4
    
#     move = 0
#     while sum(queue1)!= goal_sum and sum(queue2)!= goal_sum:
#         # 움직임 횟수 넘으면 break
#         if limit_move == move:
#             break
            
#         if sum(queue1) > sum(queue2): # queue1 에서 queue2로
#             removed = queue1.pop(0)
#             # print("removed:",removed)
#             queue2.append(removed)
#         elif sum(queue1) < sum(queue2):
#             removed = queue2.pop(0)
#             # print("removed:",removed)
#             queue1.append(removed)
        
#         move+=1 
    
#     if move == limit_move:
#         return -1
#     else:
#         return move
    
