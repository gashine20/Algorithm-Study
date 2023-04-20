# # 27866 문자와 문자열
# S = input()
# i = input(input())
# print(S[i-1])
#
#
# # 2743 단어 길이 재기
# word = input()
# print(len(word))
#
#
# # 9086 문자열
# T = int(input())
#
# for i in range(T):
#     word = input()
#     print(word[0] + word[-1])
#
#
# # 11654 아스키 코드
# word = input()
# print(ord(word))


# 11720 숫자의 합
# 공백 없는 input
# N = int(input())
# sum = 0
#
# num = input()
# for i in range(N):
#     sum += int(num[i])
#
# print(sum)


# 10809 알파벳 찾기
# S = input()
#
# alpa = [-1 for _ in range(26)]
#
# # 아스키 코드 97~122
# for i in range(len(S)):
#     code = ord(S[i])  # 97
#     # print(code)
#     if alpa[int(code) - 97] == -1:
#         alpa[int(code) - 97] = i
#
# for i in range(26):
#     print(alpa[i], end=' ')


#1152 단어의 개수
word = input().split()
print(len(word))