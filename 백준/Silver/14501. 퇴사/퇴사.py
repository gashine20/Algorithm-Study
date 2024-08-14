# 퇴사

N = int(input())
schedule = [[] for _ in range(N + 1)]
D = [0] * (N + 2)  # i번째 날부터 퇴사일까지 벌 수 있는 최대 수입

for i in range(1, N + 1):
    schedule[i] = list(map(int, input().split()))

for i in range(N, 0, -1):
    T = schedule[i][0]
    P = schedule[i][1]

    # 퇴사일 넘어서 일 할 수 없는 경우
    if i + T > N + 1:
        D[i] = D[i + 1]
    else:
        D[i] = max(D[i + 1], P + D[i + T])

print(D[1])
