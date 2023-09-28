# X보다 작은 수
# X보다 작은 수를 A에서 찾아라

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

count = []
for a in A:
    if a < X:
        count.append(a)

for c in count:
    print(c, end=' ')