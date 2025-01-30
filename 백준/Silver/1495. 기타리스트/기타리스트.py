# 기타리스트

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = set()
dp.add(S)

for v in V:
    next_dp = set()
    for vol in dp:
        if vol + v <= M:
            next_dp.add(vol + v)
        if vol - v >= 0:
            next_dp.add(vol - v)
    if not next_dp:
        print(-1)
        exit()
    dp = next_dp

print(max(dp))