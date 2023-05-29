# 삼각형 외우기

angle = [3]
sum = 0

def findEqual(a):
    # print(angle.count(a))
    return angle.count(a)


for i in range(3):
    a = int(input())
    angle.append(a)
    sum += a

if sum != 180:
    print("Error")
else:
    for i in angle:
        c = findEqual(i)
        if c == 3:
            print("Equilateral")
            break
        elif c == 2:
            print("Isosceles")
            break
    else:
        print("Scalene")
