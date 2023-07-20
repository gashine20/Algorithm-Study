# 약수들의 합

while True:
    a = int(input())
    if (a == -1): break
    
    num = []
    for i in range(1,a):
        if(a % i ==0):
            num.append(i)

    sum = 0
    for i in num:
        sum += i
    if(sum == a):
        print(a, "=", end =" ")
        print(*num, sep=" + ") # 배열은 point 처리!
    else:
        print(a,"is NOT perfect.")
