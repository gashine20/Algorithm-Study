import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

m = int(input())
finds = list(map(int, input().split()))

A.sort()

for find in finds:
    start = 0
    end = n - 1

    flag = False
    while start <= end:
        midi = int((start + end) / 2)
        if A[midi] == find:
            flag = True
            break
        elif A[midi] > find:  # 작을 때
            end = midi - 1
        else:  # 클 때
            start = midi + 1

    if flag:
        print(1)
    else:
        print(0)
