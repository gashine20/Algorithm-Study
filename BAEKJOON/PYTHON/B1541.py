# 잃어버린 괄호

sentence = list(map(str, input().split('-')))

answer = 0

for i in range(len(sentence)):
    plusSentence = sentence[i].split('+')
    sum = 0
    for plus in plusSentence:
        sum += int(plus)

    if i == 0:
        answer += sum
    else:
        answer -= sum

print(answer)
