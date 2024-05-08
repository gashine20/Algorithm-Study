# 베르트랑 공준

def Prime(a):
    arr = [True] * (2 * a + 1)
    arr[0] = False
    arr[1] = False
    count = 0

    for i in range(2, 2 * a + 1):
        if arr[i]:
            j = 2
            while (i * j) <= 2 * a:
                arr[i * j] = False
                j += 1
    return arr


def CountPrime(a, arr):
    count = 0
    for i in range(a+1, 2 * a + 1):
        if arr[i]:
            count += 1
    return count


while True:
    n = int(input())

    if n == 0:
        break
    elif n == 1:
        answer = 1
    else:
        arr = Prime(n)
        answer = CountPrime(n, arr)
    print(answer)
