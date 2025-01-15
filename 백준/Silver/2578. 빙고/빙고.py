# 빙고

check_board = [[False for _ in range(5)] for _ in range(5)]
board = []
for i in range(5):
    board.append(list(map(int, input().split())))

call = []
for i in range(5):
    call_list = list(map(int, input().split()))
    for num in call_list:
        call.append(num)


def find_index(num):
    for x in range(5):
        for y in range(5):
            if board[x][y] == num:
                return x, y


def bingo():
    count = 0
    # 행
    for i in range(5):
        if all(check_board[i]):
            count += 1
    # 열
    for i in range(5):
        if all(check_board[j][i] for j in range(5)):
            count += 1
    # 대각선
    if all(check_board[i][i] for i in range(5)):
        count += 1
    if all(check_board[i][4 - i] for i in range(5)):
        count += 1

    if count >= 3:
        return True
    return False


result = 0
for i in range(25):
    num = call[i]
    x, y = find_index(num)
    check_board[x][y] = True

    if bingo():
        result = i + 1
        break

print(result)
