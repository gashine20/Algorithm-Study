# 약수 구하기

N, K = map(int, input().split())

index = 0
number = []
for i in range(1, N + 1):
    if (N % i == 0):
        number.append(i)
        index = index + 1

if len(number) < K:
    print("0")
else:
    print(number.pop(K - 1))
