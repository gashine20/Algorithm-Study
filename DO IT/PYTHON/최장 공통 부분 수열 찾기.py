# LCS - Longest common subsequence

import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

A = list(input())
A.pop()  # '\n' 제거
B = list(input())
B.pop()

DP = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
Path = []  # LCS 저장 리스트

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            # print("i=", i, A[i-1])
            DP[i][j] = DP[i - 1][j - 1] + 1
        else: # 다르면 왼쪽과 위의 값 중 큰 수
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

# for i in range(1, len(A) + 1):
#     for j in range(1, len(B) + 1):
#         print(DP[i][j], end=' ')
#     print()

print(DP[len(A)][len(B)])


# LCS 구현 함수

def getText(r, c):
    if r == 0 or c == 0:
        return
    if A[r - 1] == B[c - 1]:
        Path.append(A[r - 1])
        getText(r - 1, c - 1)
    else:
        if DP[r - 1][c] > DP[r][c - 1]:
            getText(r - 1, c)  # 왼쪽으로
        else:  # 위쪽
            getText(r, c - 1)


getText(len(A), len(B))

for i in range(len(Path) - 1, -1, -1):
    print(Path.pop(i), end='')

print()
