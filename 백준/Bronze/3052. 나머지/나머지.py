# 나머지
remain = []
for _ in range(10):
    r = int(input()) % 42
    if r not in remain: # 배열에 없으면 넣어라
        remain.append(r)

print(len(remain)) # 배열 길이 return