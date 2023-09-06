def solution(board, moves):
    answer = 0

    # 1번 행에서 제일 위에있는걸 뽑아서 바구니에 담음
    basket = []

    for move in moves:
        for row in range(len(board)):
            basket_len = len(basket)

            pick = board[row][move - 1]
            board[row][move - 1] = 0  # 뽑은거 없애줘야함
            if pick == 0:
                pass
            else:  # 뽑은게 0이 아니면 바구니에 넣음
                if basket and basket[-1] == pick:  # 바구니 체크 : 겹치면 없앰
                    basket.pop()
                    answer += 2  # 터트려져 사라진 인형의 개수를 return
                else:
                    basket.append(pick)
                    # print(basket)
                break

    return answer