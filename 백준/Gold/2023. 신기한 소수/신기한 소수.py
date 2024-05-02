# 신기한 소수
import math

N = int(input())
prime = [2, 3, 5, 7]


def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def dfs(n):  # 시작 수
    if len(str(n)) == N:
        print(n)
    else:
        for i in range(1, 10, 2):
            if isPrime(10 * n + i):
                dfs(10 * n + i)


for i in prime:
    dfs(i)
