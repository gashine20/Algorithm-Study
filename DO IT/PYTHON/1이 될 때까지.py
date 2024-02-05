import sys

input = sys.stdin.readline

N, K = map(int, input().split())

count = 0

# 기하급수적으로
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K
    count += (N - target)
    N = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    # K로 나누기
    count += 1
    N //= K

# while True:
#     if N % K == 0:
#         N = N // K
#         count += 1
#     else:
#         N -= 1
#         count += 1
#
#     if N == 1:
#         break

print(count)
