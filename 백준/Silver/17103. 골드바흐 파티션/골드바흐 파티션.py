# 골드바흐 파티션
# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

MAXSIZE = 1000000


def Prime(num):  # O(log n)
    arr = [True] * (num + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, num + 1):
        if arr[i]:
            j = 2
            while (i * j) <= num:
                arr[i * j] = False
                j += 1

    return arr


def countGoldBah(arr, n):
    count = 0

    for i in range(2, int(n/2) + 1):
        if arr[i]:
            remain = n - i
            if arr[remain]:
                count += 1

    return count


T = int(input())
arr = Prime(MAXSIZE)

for _ in range(T):
    N = int(input())
    count = countGoldBah(arr, N)
    print(count)
