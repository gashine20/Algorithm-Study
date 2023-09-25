# 두 수 비교하기
A, B = list(map(int, input().split()))

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")

# 시험 성적
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

# 윤년
# = 연도가 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때

# A이면서 B 또는 C
# AB 또는 AC
# A B 그리고 C
year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

# 사분면 고르기
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

# 알람 시계
H, M = list(map(int, input().split()))

if M - 45 < 0:
    if H - 1 < 0:
        H = 23
    else:
        H -= 1
    M += 15
else:
    M -= 45
print(H, M)

# 오븐 시계
H, M = list(map(int, input().split()))
time = int(input())

# time이 120분일 수도 있음 => H+=2

if M + time < 60:
    M += time
else:
    H += time // 60
    M += time % 60
    if M >= 60:
        H += 1
        M -= 60
    if H >= 24:
        H -= 24

print(H, M)

# 주사위 세개
A, B, C = list(map(int, input().split()))

if A == B == C:
    print(10000 + A * 1000)
elif A == B:
    print(1000 + A * 100)
elif A == C:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
else:
    # 최대값 찾기
    temp = A
    if temp < B:
        temp = B
    if temp < C:
        temp = C
    print(temp * 100)
