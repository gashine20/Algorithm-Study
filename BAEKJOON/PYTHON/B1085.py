# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

# 삼항 연산자
len1 = abs(x-w) if abs(x-w) < abs(x-0) else abs(x-0)
len2 = abs(y-h) if abs(y-h) < abs(y-0) else abs(y-0)

print(len1) if len1 < len2 else print(len2)
