import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
menu = A[0]

ff = [0] * (n + 1)
ff[0] = 1

for i in range(1, n + 1):
    ff[i] = ff[i - 1] * i  ## 자리 수 바뀌는 주기

visited = [False] * 21
s = [0] * 21
if menu == 1:  # k 입력
    k = A[1]
    for i in range(1, n + 1):
        cnt = 1
        for j in range(1, n + 1):
            if visited[j]:
                continue
            if k <= cnt * ff[n - i]:
                k -= (cnt - 1) * ff[n - i]
                s[i] = j
                visited[j] = True
                break
            cnt += 1

    for i in range(1, n + 1):
        print(s[i], end=" ")
elif menu == 2:  # 수열 입력
    K = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, A[i]):
            if not visited[j]:
                cnt += 1

        K += cnt * ff[n - i]
        visited[A[i]] = True

    print(K)
