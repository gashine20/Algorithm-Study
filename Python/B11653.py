# 소인수분해

N = int(input())
if N == 1 : print("")

while N > 1:
    for i in range(2,N+1):
        if N % i == 0:
            print(i)
            N = int(N/i)
            break # for문을 벗어남