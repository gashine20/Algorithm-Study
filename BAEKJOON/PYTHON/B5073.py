# 삼각형과 세 변
# 배열 포함 여부!!

while True:
    a, b, c = map(int,input().split(' '))
    if a == 0 and b == 0 and c == 0: break
    
    line = [a,b,c]
    line.sort()

    if a+b <= c:
        print("Invalid")
    else:
        if a == b == c: # 세 변의 길이가 모두 같은 경우
            print("Equilateral")
        elif line.count(a) > 1 or line.count(b) > 1 or line.count(c)>1: # 두 변의 길이만 같은 경우
            print("Isosceles") 
        else:
            print("Scalene")
    