import sys

input = sys.stdin.readline

N = int(input())

sp = list(map(int, input().split()))
sp.insert(0, 0)

index = 0
maxLength = 1
B = [0] * (N + 1)
D = [0] * (N + 1)
ans = [0] * (N + 1)
B[maxLength] = sp[1]
D[1] = 1


def binarysearch(l, r, now):
    while l < r:
        mid = (l + r) // 2
        if B[mid] < now:
            l = mid + 1
        else:
            r = mid

    return l


for i in range(2, N + 1):
    if B[maxLength] < sp[i]:
        maxLength += 1
        B[maxLength] = sp[i]
        D[i] = maxLength
    else:
        index = binarysearch(1, maxLength, sp[i])
        B[index] = sp[i]
        D[i] = index

print(maxLength)
index = maxLength
x = B[maxLength] + 1

for i in range(N, 0, -1):
    if D[i] == index:
        ans[index] = sp[i]
        index -= 1

for i in range(1, maxLength + 1):
    print(ans[i], end=' ')

# D = [0] * (N + 1)
# ans = []
# B = [0] * 1000001
#
#
# def findFirstMin(len):
#     max_val = sp[len]
#     for i in range(len):
#         if sp[i] < max_val:
#             return i
#
#     return -1
#
#
# def findLength(length):
#     max_val = sp[length]
#     # max_val 보다 작은 수 , 첫 번째로 작은 수를 찾아내야 한다.
#     before_val = findFirstMin(length)
#     if before_val == -1:
#         return 0
#
#     count = 1  # 자기 자신 포함
#
#     for i in range(length):
#         if before_val < sp[i] < max_val:  # max으로 찾아내야함
#             print(sp[i], end=" ")
#             count += 1
#             before_val = sp[i]
#         else:
#
#     print(max_val)
#
#     return count
#
#
# def findAns(length):
#     max_val = sp[length]
#     # max_val 보다 작은 수 , 첫 번째로 작은 수를 찾아내야 한다.
#     before_val = findFirstMin(length)
#
#     for i in range(length):
#         if before_val < sp[i] < max_val:
#             ans.append(sp[i])
#             before_val = sp[i]
#
#     ans.append(max_val)
#
#
# for i in range(1, N):
#     D[i] = findLength(i)
#     print("count", D[i])
#
# index = D.index(max(D))
# findAns(index)
#
# print(len(ans))
# for i in ans:
#     print(i, end=" ")
