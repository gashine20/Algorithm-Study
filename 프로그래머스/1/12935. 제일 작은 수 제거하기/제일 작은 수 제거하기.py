import sys

def solution(arr):
    answer = []    
    min_num = sys.maxsize
    index = 0   

    for i in range(len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            index = i
    
    arr.pop(index)
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    
    return answer