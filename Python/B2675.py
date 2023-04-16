# 문자열 반복

T = int(input())  # 케이스의 개수

for i in range(T):
    R, S = input().split()  # 반복횟수
    text = ''
    for y in S:
        text += y * int(R)
    print(text)
