def solution(ingredient):
    answer = 0
    # 1 빵, 2 야채, 3 고기, 1빵
    # 스택 써야될거 같은데
    stack = []

    for i in ingredient:
        stack.append(i)

        if len(stack) > 3:
            if (stack[-4:] == [1, 2, 3, 1]):
                answer += 1
                del stack[-4:]

    return answer
