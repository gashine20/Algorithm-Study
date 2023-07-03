# 수 정렬하기

N = int(input())

a = []
for _ in range(N):
    b = int(input())
    a.append(b)

a.sort()
for i in a:
    print(i)
