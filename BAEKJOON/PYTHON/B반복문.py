# 구구단 - 1m 19s
N = int(input())
for i in range(1, 10):
    print(N, "*", i, "=", N * i)

# A+B-3 - 1m 20s
T = int(input())
for i in range(T):
    A, B = list(map(int, input().split()))
    print(A + B)

# 합 - 1m 40s
n = int(input())
sum_num = 0
for i in range(1, n + 1):
    sum_num += i

print(sum_num)

# 영수증 -3m 3s
X = int(input())  # 영수증에 적힌 금액
N = int(input())  # 구매한 물건 종류 수

price = 0
for i in range(N):
    a, b = list(map(int, input().split()))
    price += a * b

if price == X:
    print("Yes")
else:
    print("No")

# 코딩은 체육과목 입니다 - 3m 44s
N = int(input())
N = N // 4
for i in range(N):
    print("long", end=' ') # -> 줄 바뀜.. end 사용! end=' '

print("int")

# 빠른 A+B - 5m 27s
import sys

T = int(sys.stdin.readline())

for i in range(T):
    A, B = list(map(int, sys.stdin.readline().split()))
    print(A + B)

# A+B -7 - 4m 41s
T = int(input())
for i in range(1, T + 1):
    A, B = list(map(int, input().split()))
    print(f"Case #{i}: {A + B}") # f 사용!

# A+B-8 -1m 44s
T = int(input())
for i in range(1, T + 1):
    A, B = list(map(int, input().split()))
    print(f"Case #{i}: {A} + {B} = {A + B}")

# 별 찍기-1 -2m 17s
N = int(input())
for i in range(1, N + 1):
    for j in range(i):
        print("*", end='')
    print("")  # 줄바꿈

# 별 찍기-2 - 5m
N = int(input())
for i in range(N - 1, -1, -1):  # 4~0
    for j in range(i):  # 4~0 빈칸 출력
        print(" ", end='')
    for j in range(N - i):  # 별 출력
        print("*", end='')
    print("")  # 줄바꿈

# A+B-5 - 2m 22s
while True:
    A, B = list(map(int, input().split()))
    if A == 0 and B == 0:
        break
    print(A + B)

# A+B-4 - 2m 42s
while True:
    try:
        A, B = list(map(int, input().split()))
        print(A + B)
    except:  # -> except 사용!
        break
