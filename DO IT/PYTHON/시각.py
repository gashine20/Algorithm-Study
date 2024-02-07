n = int(input())

# 00시 00분 00초 ~  n시 00분 00초

hour = 0
minute = 0
hour_range = [3, 13, 23]
minute_range = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
result = 0
while hour <= n:
    if hour in hour_range:
        result += 3600
        hour += 1
        continue
    if minute in minute_range:
        result += 60
    else:
        result += 15

    if minute + 1 >= 60:
        minute = 0
        hour += 1
    else:
        minute += 1

print(result)

# 다른 풀이
count = 0
for i in range(hour + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가 -> str로 변경
            if '3' in str(hour) + str(j) + str(k):
                count += 1
