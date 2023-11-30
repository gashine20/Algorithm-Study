# 블랙잭

N, M = map(int, input().split(" "))
num = list(map(int, input().split(" ")))

diff = M

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            sum = num[i]+num[j]+num[k]
            if sum > M:
                pass
            elif M-sum <= diff:
                diff = M-sum
                card = sum

print(card)
