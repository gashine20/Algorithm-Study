# 피보나치 수 2

n = int(input())
D = [0 for _ in range(n + 1)]
D[1] = 1

for i in range(2, n + 1):
    D[i] = D[i - 1] + D[i - 2]

print(D[n])
