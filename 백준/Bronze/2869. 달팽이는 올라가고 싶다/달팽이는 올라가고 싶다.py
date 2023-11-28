import math 

A, B, V = map(int, input().split())

last_V = V-B
move = A-B

# (A-B) * day + A >= V - 오답
# move * day >= last_v

# A * day + B * (day -1) >= V

day = last_V / move
print(math.ceil(day))