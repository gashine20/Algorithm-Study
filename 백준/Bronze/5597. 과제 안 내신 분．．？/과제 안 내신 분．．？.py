# 과제 안 내신 분..?
bucket = [0] * 31
for _ in range(28):
    bucket[int(input())] = 1

#print(bucket)

for i in range(1, 31):
    if bucket[i] == 0:
        print(i)