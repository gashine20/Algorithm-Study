# 크로아티아 알파벳 - 27m 37s
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
count = 0

for alpha in croatia:
    if alpha in word:  # 입력받은 word에 alpha를 찾음 -> 반복할 수 있음
        #print(alpha, word.index(alpha))
        #print("count",word.count(alpha)) # 반복한 갯수
        #count += word.count(ap)  # 치환한 알파벳
        #al_count += len(ap)* word.count(ap) # ex) dz= 길이를 합함
        word = word.replace(alpha,'*') # 포함되어있으면 그 부분 없애기
        #print(word)


#alpha_count = len(word) - al_count # 치환된 알파벳을 제외한 정상 알파벳 개수세기
count = len(word) # 남은 알파벳 더하기

print(count)
