while True:
    n = int(input())
    if n == -1:
        break

    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    divSum = 0
    for j in divisor:
        divSum += j

    if divSum == n:
        print(n, "=", end=" ")
        for k in divisor:
            if k == divisor[len(divisor) - 1]:
                print(k)
            else:
                print(k, "+", end=" ")
    else:
        print(n, "is NOT perfect.")
