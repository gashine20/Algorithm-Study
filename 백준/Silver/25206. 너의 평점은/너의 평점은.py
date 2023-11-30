# 너의 평점은
scores = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 
         'D+':1.5, 'D0':1.0, 'F':0.0}

avg_score = 0
sum_credit = 0

for _ in range(20):
    major, credit, score = input().split(' ')
    credit = float(credit)

    if score != "P": # 등급이 P인 과목은 계산 제외
        score = scores[score]
        # print(credit, score)
        avg_score += credit * score
        sum_credit += credit

#print(avg_score)
avg_score /= sum_credit

print(avg_score)
