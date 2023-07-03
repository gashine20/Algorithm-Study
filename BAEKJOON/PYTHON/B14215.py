# 세 막대

a, b, c = map(int, input().split(" "))
line = [a, b, c]

line.sort()

if line[0] + line[1] <= line[2]:
    print((line[0] + line[1]) * 2 - 1)  # 제일 긴 변이 나머지 두 변의 합보다 1작은 수까지 줄여야한다
else:
    print(a + b + c)
