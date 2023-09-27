N = int(input())
for i in range(N - 1, -1, -1):  # 4~0
    for j in range(i):  # 4~0 빈칸 출력
        print(" ", end='')
    for j in range(N - i):  # 별 출력
        print("*", end='')
    print("")  # 줄바꿈