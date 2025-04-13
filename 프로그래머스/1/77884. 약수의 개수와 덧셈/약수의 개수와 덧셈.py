def solution(left, right):
    answer = 0
    # 제곱근의 약수의 개수는 홀수
    for i in range(left, right+1):
        if int(i**(0.5)) == i**(0.5):
            answer -= i
        else:
            answer += i
    return answer