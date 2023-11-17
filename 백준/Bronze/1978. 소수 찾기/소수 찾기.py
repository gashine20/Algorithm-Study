def is_prime(a):
    if a == 1: 
        return 0

    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            return 0

    return 1


count = 0
N = int(input())
number = map(int, input().split(" "))

for i in number:
    count += is_prime(i)

print(count)