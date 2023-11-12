# 소수 찾기
# 소수는 약수가 1과 본인만 있는 녀석

def findNum(a):
    if a == 1: return 0
    for i in range(2,int(a/2)+1):
        if(a % i == 0):
            return 0

    return 1

N = int(input())
num = map(int, input().split())

sum = 0
for i in num:
    sum += findNum(i)

print(sum)

