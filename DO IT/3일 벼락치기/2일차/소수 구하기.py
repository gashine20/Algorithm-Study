import math

m, n = map(int, input().split())


def ifPrim(num):
    if num == 1:  # 1 조건 !! **
        return False
    prim = int(math.sqrt(num))
    # print(num, prim)
    for i in range(2, prim + 1):
        if num % i == 0:
            return False

    return True


for i in range(m, n + 1):
    if ifPrim(i):
        print(i)
