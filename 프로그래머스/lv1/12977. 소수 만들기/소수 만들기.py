# 19m, 다른 사람 코드 참조 .. 
import math
from itertools import combinations 

#num_list = []

# 소수 찾기
def checkDemical(num):
    #print("num",num)

    for i in range(2,int(math.sqrt(num))+1): # 16이면 16 제곱근 4까지 나눠봄
        if num % i == 0:
            return 0 # 나눠떨어지면 소수x -> 0으로 리턴
    return 1
    # 소수이면
#     if num not in num_list: # num_list에 없으면 저장
#         num_list.append(num)
#         #print(num_list)
    
#     return len(num_list) # num_list 길이 리턴

# 조합
def solution(nums):
    answer = 0

    #sum_num=0

    # for i in range(len(nums)-2): # 3개의 합 for문 0 1 2 3
    #     for j in range(i+1,len(nums)-1): # 1 2
    #         for q in range(j+1,len(nums)): # -> 범위 첫 시작은 j로!!!!
    #             #print(nums[i],nums[j],nums[q] )
    #             sum_num = nums[i] + nums[j] + nums[q]
    #             if checkDemical(sum_num) != 0: #소수가 맞다면
    #                answer = checkDemical(sum_num) # num_list 리턴 
    
    #print(list(combinations(nums,3)))
    cn = list(combinations(nums,3)) # 조합
    for comList in cn:
        sum = 0
        for num in comList:
            sum+=num
            
        if checkDemical(sum) :
                answer+=1    
            
    return answer

