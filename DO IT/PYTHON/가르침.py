import sys

input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().strip()) for _ in range(N)]

# print(words)

answer = 0
letter_set = {"a", "c", "i", "n", "t"}
learn = [0] * 26


def count_readable_words():
    readcnt = 0
    for word in words:
        check = True
        for w in word:
            if not learn[ord(w) - ord('a')]:
                check = False
                break
        if check:
            readcnt += 1
    return readcnt


def dfs(idx, cnt):
    global answer

    # print(idx, cnt)
    if cnt == K - 5:
        answer = max(answer, count_readable_words())
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


if K < 5:
    answer = 0
elif K == 26:
    answer = N
elif K > 5:
    # a,c,i,n,t 있으면 배움
    for c in letter_set:
        learn[ord(c) - ord('a')] = 1

    dfs(0, 0)

print(answer)
