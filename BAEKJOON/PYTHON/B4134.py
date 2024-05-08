# 다음 소수
import math

n = int(input())


def Prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False

    return True


for _ in range(n):
    num = int(input())
    if num == 0 or num == 1 or num == 2:
        num = 2
    else:
        while True:
            if Prime(num):
                break
            num += 1

    print(num)
