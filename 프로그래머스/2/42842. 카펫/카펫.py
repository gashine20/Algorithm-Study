import math

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for row in range(1, int(math.sqrt(total))+1):
        if total % row == 0:
            column = total // row
            yellow_count = (column -2) * (row -2)
            if yellow_count == yellow:
                answer.append(column)
                answer.append(row)
            else:
                continue
    
    return answer



# brown + yellow = 전체 타일의 개수
# n x m = 전체 타일, 완전 탐색
# 항상 가로길이 >= 세로 
# 4*3 = 전체 타일 (4-2) * (3-1) = yellow
