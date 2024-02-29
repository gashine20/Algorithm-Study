import sys

input = sys.stdin.readline

N = int(input())
candy = [list(input()) for _ in range(N)]


# 1. 색이 다른 인접한 두 칸을 고른다. (오른쪽, 아래)
# 2. 그 두 사탕을 교환한다.
# 3. 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른다.
# 4. 그 사탕을 다 먹는다.

def checkCandy():  # O(2n)
    max_cnt = 1  # total_max_cnt
    for i in range(N):
        # 가로 먼저 확인
        cnt = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        # 세로 확인
        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt


# def printCandy():
#     for c in candy:
#         print(c)


result = 0
for i in range(N):
    for j in range(N):
        now = candy[i][j]
        # 오른쪽
        if j + 1 < N and now != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            result = max(result, checkCandy())
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]  # 원래 대로
        # 아래
        if i + 1 < N and now != candy[i + 1][j]:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            result = max(result, checkCandy())
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j] # 원래 대로

        # printCandy()
        # print()

print(result)