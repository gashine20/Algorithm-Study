# 그룹 단어 체커
N = int(input())

count = 0

for _ in range(N):
    group = 1  # true false
    alph = {}
    word = input()

    pre = ''
    for w in word:
        if pre == w:  # 앞에 있는 알파벳과 같으면
            # 추가
            if w in alph:  # alph에 값이 있으면
                alph[w] += 1  # 1추가
            else:  # 값이 없으면
                alph[w] = 0  # 0으로 추가
        else:  # 앞에 있는 알파벳과 다르면
            # alph 안에 있으면 break = 연속적이지 않음
            if w in alph:
                group = 0
                break;
            # alph 안에 없으면 alph에 추가하고 pre 갱신
            else:
                alph[w] = 0
                pre = w

    if group:
        count += 1

print(count)
