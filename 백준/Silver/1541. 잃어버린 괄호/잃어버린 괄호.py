# 그리디
# 100-40+50+74-30+29-45+43+11
expression = list(map(str, input().split("-")))
# print(expression)


def mySum(exp):
    mysum = 0
    arr = list(map(int, exp.split("+")))

    for a in arr:
        mysum += a

    return mysum


answer = 0
for i in range(len(expression)):
    value = mySum(expression[i])

    if i == 0:
        answer += value
    else:
        answer -= value

print(answer)