# 2 x n 타일링

n = int(input())
mod = 10007

D = [0] * 1001
D[1] = 1
D[2] = 2

result = 0


for i in range(3, n + 1):
    D[i] = (D[i - 2] + D[i - 1]) % mod

result = D[n]
print(result)
