# 평균
N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

sum_score = 0
for score in scores:
    sum_score += (score / max_score) * 100

print(sum_score / N)