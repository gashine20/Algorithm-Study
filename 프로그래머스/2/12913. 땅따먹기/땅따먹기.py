def solution(land):
    answer = 0
    n = len(land)
    
    for i in range(1, n):
        for j in range(4):
            land[i][j] = land[i][j] + max([land[i-1][k] for k in range(4) if j != k])
            
    return max(land[-1])


# land[1] 기준으로 보면
# land[1][0] 은 위에서 밟을 수 있는 방법이 land[0][0] 빼고 다 가능하다.