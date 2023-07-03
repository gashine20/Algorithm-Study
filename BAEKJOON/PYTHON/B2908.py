#상수

s1, s2 = input().split()

s1 = int(s1[::-1])
s2 = int(s2[::-1])

if(s1<s2):
    print(s2)
else:
    print(s1)
