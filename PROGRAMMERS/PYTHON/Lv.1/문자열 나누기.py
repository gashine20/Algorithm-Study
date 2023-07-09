# 문자열 나누기
def solution(s):
    answer = 0

    # count 사용 x_count인것과 xx_count아닌것

    x_count = 0
    xx_count = 0
    x = s[0]
    for i in range(len(s)):
        if (s[i] == x):
            x_count += 1
        else:
            xx_count += 1

        if (x_count == xx_count):  # x_count와 xx_count 같아지면
            answer += 1  # 분리
            x_count = 0
            xx_count = 0
            if i + 1 < len(s):
                x = s[i + 1]  # 분리할 때마다 첫번째 글자 x를 다시 갱신해야됨
            pass
        elif i + 1 == len(s):  # 더 이상 읽을 글자가 없다면
            answer += 1

    return answer