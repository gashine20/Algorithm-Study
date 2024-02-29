import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

count = 1


def isPrime(number):
    for i in range(2, int(number / 2 + 1)):
        if number % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)

    for i in range(1, 10):
        if (number * 10 + i) % 2 == 0:
            continue
        if isPrime(number * 10 + i):
            DFS(number * 10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)
