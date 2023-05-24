# 색종이

count = int(input())

paper = [[0 for _ in range(101)] for _ in range(101)] 

for i in range(count):
    x , y = map(int, input().split(" "))
    
    for row in range(x,x+10):
        for col in range(y,y+10):
            paper[row][col] = 1

width = 0

for i in paper:
    width += i.count(1)
print(width)
