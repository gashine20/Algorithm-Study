# 공 넣기
# N 바구니 개수, M번 공을 넣음
N, M = map(int, input().split())

bucket = [0] * (N + 1)  # 배열 크기 지정 ! ! !

for _ in range(M):
    i, j, k = map(int, input().split())
    for p in range(i, j + 1):  # i~j k번호 적혀있는 공을 넣음
        bucket[p] = k  # -> index out of range 오류 뜸

for i in range(1, len(bucket)):  # 처음 바구니는 [0] 비어 있음
    print(bucket[i], end=' ')