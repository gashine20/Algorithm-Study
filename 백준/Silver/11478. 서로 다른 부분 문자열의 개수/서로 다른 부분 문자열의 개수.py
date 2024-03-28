# 서로 다른 부분 문자열의 개수

S = input()

d = {}
length = 0
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        if S[i:j] not in d:
            d[S[i:j]] = 0

print(len(d))
