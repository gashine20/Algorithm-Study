import math

m, n = map(int, input().split())

def Prime(n):
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False
    
    for i in range(2, int(math.sqrt(n))+1):
        j = 2
        if arr[i]:
            while i * j <= n:
                arr[i * j] = False
                j += 1
                
    return arr


arr = Prime(n)

for i in range(m, n + 1):
    if arr[i]:
        print(i)
