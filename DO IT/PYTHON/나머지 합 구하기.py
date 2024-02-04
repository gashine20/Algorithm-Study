import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))

S = [0] * N
C = [0] * M  # 같은 나머지의 인덱스를 카운트하는 리스트
S[0] = num[0]

answer = 0

for i in range(1, N):
    S[i] = S[i - 1] + num[i]

for i in range(N):
    remainder = S[i] % M
    if remainder == 0:
        answer += 1

    C[remainder] += 1  # 나머지가 같은 인덱스의 개수 값 증가시키기

for i in range(M):
    # 나머지가 같은 인덱스 중 2개를 뽀는 경우의 수 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
