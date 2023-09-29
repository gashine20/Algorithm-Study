# 별 찍기 -7 -20m 계속 틀렸대.. 아 별 띄어쓰기
N = int(input())

# 위
for i in range(1, N + 1):  # 1~5
    for _ in range(N - i):  # 공백 출력 , 4 3 2 1 0
        print(" ", end='')
    for _ in range(2 * i - 1):  # 별 출력, 1,3,5,7,9
        print("*", end='')

    print("")

# 아래
for i in range(1, N):  # 5~2 , 1,2,3,4
    for _ in range(i):  # 공백 출력, 1 2 3 4
        print(" ", end='')
    for _ in range(2 * N - 2 * i - 1):  # 별 출력, 7,5,3,1
        print("*", end='')
    print("")