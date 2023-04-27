# 바구니 순서 바꾸기
# N 바구니 갯수 , M 번 회전
# 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 회전시키는데
# 그 때 기준 바구니는 k번째 바구니라는 뜻이다.

N, M = map(int, input().split(' '))

bucket = []

for i in range(N):
    bucket.append(i + 1)

for _ in range(M):
    begin, end, mid = map(int, input().split(' '))

    # 1 3 3 일 때, 4 6 1 2 3 7 10 5 8 9
    # 1 4 6 2 3 7 10 5 8 9

    begin, end, mid = begin - 1, end - 1, mid - 1

    bucket[begin:end + 1] = bucket[mid:end + 1] + bucket[begin:mid]

for i in bucket:
    print(i, end=' ')
