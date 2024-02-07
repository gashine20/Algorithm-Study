S = input()

alpha = []
num = []
for i in range(len(S)):
    if S[i].isalpha():  # A~Z
        alpha.append(S[i])
    else:
        num.append(S[i])

alpha.sort()
num.sort()

for a in alpha:
    print(a, end='')
for n in num:
    print(n, end='')
