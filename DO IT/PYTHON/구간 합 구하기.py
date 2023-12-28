import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 트리 초기화
length = 1
while length < N:
    length *= 2

length *= 2
main_index = int(length / 2)

tree = [0] * length

for i in range(N):
    tree[main_index + i] = int(input())

# 트리 채워넣기
for i in range(main_index - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]


# 특정 부분 변경
def changeVal(index, value):
    change_index = main_index + index - 1
    tree[change_index] = c

    # 합
    parent_index = int(change_index / 2)
    while parent_index > 0:
        tree[parent_index] = tree[parent_index * 2] + tree[parent_index * 2 + 1]
        parent_index = int(parent_index / 2)

    # print(tree)


# 구간 합
def getSum(start_index, end_index):
    index_sum = 0

    while start_index <= end_index:
        if start_index % 2 == 1:
            # print("start_index = ", start_index)
            index_sum += tree[start_index]
            start_index += 1
        if end_index % 2 == 0:
            # print("end_index = ", end_index)
            index_sum += tree[end_index]
            end_index -= 1

        start_index = start_index // 2
        end_index = end_index // 2

    return index_sum


for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:  # 변경
        changeVal(b, c)
    elif a == 2:  # 구간 합
        start_index = b + main_index - 1
        end_index = c + main_index - 1

        print(getSum(start_index, end_index))
