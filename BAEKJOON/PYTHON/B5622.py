#다이얼

word = ['ABC','DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']

num = input()
count =0

for n in num:
    for i in range(len(word)):
        if n in word[i]:
            count = count+i+3

print(count)
