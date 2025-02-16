# 일곱 난쟁이

from itertools import combinations

heights = [] * 9
for _ in range(9):
    heights.append(int(input()))

result = []
for height in list(combinations(heights, 7)):
    if sum(height) == 100:
        result = height
        break

result = sorted(result)
for i in result:
    print(i)
