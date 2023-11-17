def is_prime(a):
    if a == 1:
        return 0

    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            return 0

    return 1

M = int(input())
N = int(input())

primeSum = 0
primeMin = N

for i in range(M, N + 1):
    if is_prime(i) == 1:
        primeSum += i
        if i < primeMin:
            primeMin = i

if primeSum == 0:
    print("-1")
else:
    print(primeSum)
    print(primeMin)