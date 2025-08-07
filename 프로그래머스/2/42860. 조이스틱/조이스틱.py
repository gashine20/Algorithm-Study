def solution(name):
    answer = 0
    pos = []
    n = len(name)
    
    # 위/아래 조작 개수 세기
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

        
    # 오/왼 조작 개수 세기
    move = n -1
    for i in range(n):
        next_i = i+1
        # A가 연속되는 구간 찾기
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        # 좌로 갔다가 우로 돌아오거나 (i + i + n - next_i)
        # 우로 갔다가 좌로 돌아오는 경우
        move = min(move, 2 * i + n - next_i)
        move = min(move, i + 2 * (n-next_i))
        
    return answer + move