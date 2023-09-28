# 공 바꾸기
# N 바구니 개수, M번 바꿈
N, M = map(int, input().split())

bucket = [0] * (N + 1)  # 0으로 채워줘야함
for i in range(1, len(bucket)):
    bucket[i] = i

for _ in range(M):
    i, j = map(int, input().split())
    tmp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = tmp

for i in range(1, len(bucket)):
    print(bucket[i], end=' ')
