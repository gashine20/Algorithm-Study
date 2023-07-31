def solution(players, callings):
    for i in callings:
        # 해당 이름 찾아서 index return
        fast = players.index(i)  # index return # 3
        slow = fast - 1  # 2

        # 스왑
        players[slow], players[fast] = players[fast], players[slow]

    return players