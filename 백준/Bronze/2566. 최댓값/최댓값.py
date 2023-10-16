# 최댓값

num = [[0]*9]*9

for i in range(9):
    num[i] = list(map(int,input().split()))

max = num[0][0]
row = 0
col = 0 
#print(max)
for i in range(9):
    for j in range(9):
        if(num[i][j]>max):
            max = num[i][j]
            row = i
            col = j

print(max)
print(row+1,col+1)