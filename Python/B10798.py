# 세로 읽기

num = []
for _ in range(5):
    num.append(input())

sentence = ''
for i in range(15):
    for j in range(5):
        if len(num[j]) > i: #그 줄의 길이가 i보다 크면 = 있으면
            sentence += num[j][i]


print(sentence)




