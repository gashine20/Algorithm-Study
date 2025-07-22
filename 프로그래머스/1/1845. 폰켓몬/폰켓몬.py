from collections import Counter

def solution(nums):
    answer = 0
    N = len(nums)//2
    dicts = Counter(nums)
    type_count = len(dicts)
    
    if N >= type_count:
        return type_count
    else:
        return N
    