import sys

def solution(arr):
    answer = []    
    min_num = min(arr)
    arr.remove(min_num)
    
    answer = [-1] if len(arr) == 0 else arr
    
    return answer