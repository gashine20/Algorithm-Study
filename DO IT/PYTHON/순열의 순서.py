# 조합

import sys

input = sys.stdin.readline

F = [0] * 21  # 팩토리얼 정보
S = [0] * 21  # 실제 자리 수

visited = [False] * 21
N = int(input())

F[0] = 1

for i in range(1, N + 1):
    F[i] = F[i - 1] * i

inputList = list(map(int, input().split()))

if inputList[0] == 1:
    K = inputList[1]

    for i in range(1, N + 1):
        cnt = 1

        for j in range(1, N + 1):
            # print("i = ", i, " j = ", j, " cnt = ", cnt, " F[N-i] = ", F[N - i])
            # print(K, "<=", cnt, "*", F[N - i])
            if visited[j]:
                continue
            if K <= cnt * F[N - i]:
                # print(K, "<=", cnt, "*", F[N - i])
                K -= (cnt - 1) * F[N - i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, N + 1):
        print(S[i])

else:
    K = 1
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1  # 미사용 숫자 개수만큼 카운트
        K += cnt * F[N - i]  # 자릿수에 따라 순서 더하기
        visited[inputList[i]] = True

    print(K)
