# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)-1):
#         for j in range(i+1,len(numbers)):
#             sum = numbers[i] + numbers[j]
            
#             if sum not in answer:
#                 answer.append(sum)
            
#     answer.sort()
    
#     return answer

from itertools import combinations

def solution(numbers):
    answer = []
    for number in combinations(numbers,2):
        sum_number = sum(number)
        if sum_number not in answer:
            answer.append(sum_number)
    answer.sort()
    
    return answer