# 새싹
# print("""         ,r'"7""")
# print("r`-_   ,'  ,/")
# print(""" \. ". L_r'""")
# print("   `~\/")
# print("      |")
# print("      |")

# 킹, 퀸, 룩, 비숍, 나이트, 폰 - 4m 19s
# 1, 1, 2, 2, 2, 8
# correct_count = [1, 1, 2, 2, 2, 8]
# white_piece = list(map(int, input().split()))
#
# for i in range(len(white_piece)):
#     white_piece[i] = correct_count[i] - white_piece[i]
#
# for piece in white_piece:
#     print(piece, end=' ')

# 별 찍기 -7 -20m 계속 틀렸대.. 아 별 띄어쓰기
# N = int(input())
#
# # 위
# for i in range(1, N + 1):  # 1~5
#     for _ in range(N - i):  # 공백 출력 , 4 3 2 1 0
#         print(" ", end='')
#     for _ in range(2 * i - 1):  # 별 출력, 1,3,5,7,9
#         print("*", end='')
#
#     print("")
#
# # 아래
# for i in range(1, N):  # 5~2 , 1,2,3,4
#     for _ in range(i):  # 공백 출력, 1 2 3 4
#         print(" ", end='')
#     for _ in range(2 * N - 2 * i - 1):  # 별 출력, 7,5,3,1
#         print("*", end='')
#     print("")


# 팰린드롬인지 확인하기 -> for문 어떻게 벗어날건지 - 8m
# word = input()
# answer = 1
# for i in range(len(word)):
#     # print(word[i], word[len(word)-1-i])
#     if word[i] != word[len(word) - 1 - i]:
#         answer = 0
#         break
#
# if answer != 0:
#     answer = 1
# print(answer)

# word = list(input()) # list 사용해서 reverse() 함수 사용
# if list(reversed(word)) == word:
#     print(1)
# else:
#     print(0)


# 단어 공부 -22m
# word = input()
# word = word.upper()  # upper() 원본 수정x
#
# alpha = {}
# for w in word:
#     if w not in alpha:
#         alpha[w] = 1
#     else:
#         alpha[w] += 1
#
# answer = max(alpha) # 최대 개수를 가지고 있는 key
# max_count = alpha.get(max(alpha))  # 최대 개수
# print(answer)
#
# count = 0
# for word_count in alpha.values():
#     if word_count == max_count:  # 여러개 있으면
#         count +=1
#
# if count > 1:
#     answer="?"
# print(answer)


# 크로아티아 알파벳 - 27m 37s
# croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
#
# word = input()
# count = 0
#
# for alpha in croatia:
#     if alpha in word:  # 입력받은 word에 alpha를 찾음 -> 반복할 수 있음
#         print(alpha, word.index(alpha))
#         print("count",word.count(alpha)) # 반복한 갯수
#         #count += word.count(ap)  # 치환한 알파벳
#         #al_count += len(ap)* word.count(ap) # ex) dz= 길이를 합함
#         word = word.replace(alpha,'*') # 포함되어있으면 그 부분 없애기
#         print(word)
#
#
# #alpha_count = len(word) - al_count # 치환된 알파벳을 제외한 정상 알파벳 개수세기
# count = len(word) # 남은 알파벳 더하기
#
# print(count)


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
