def solution(ingredient):
    answer = 0
    # 1 빵, 2 야채, 3 고기, 1빵
    # 스택 써야될거 같은데
    stack = []

    for i in range(len(ingredient)):
        if i > 4:
            print(ingredient[i-4:i])


    return answer
