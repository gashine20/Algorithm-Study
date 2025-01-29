# 1로 만들기

N = int(input())
A = [0] * (N + 1)  # 1을 만들기 위해서 연산해야하는 경우의수
A[1] = 0

for i in range(2, N + 1):
    A[i] = A[i - 1] + 1
    if i % 3 == 0:
        A[i] = min(A[i], 1 + A[i // 3])
    if i % 2 == 0:
        A[i] = min(A[i], 1 + A[i // 2])

print(A[N])
