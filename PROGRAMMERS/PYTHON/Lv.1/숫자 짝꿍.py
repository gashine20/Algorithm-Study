def solution(X, Y):
    answer = ''
    # 존재하지 않으면 -1, 0으로만 구성되어 있으면 0
    # X = 5525, Y = 1255

    x_num = {}
    max_num = []
    # X에 해당 숫자 몇 개 있는지 입력
    for x in X:
        if x in x_num:
            x_num[x] = x_num.get(x) + 1
        else:
            x_num.setdefault(x, 1)

    # print(x_num)
    # x,y 비교
    for x in x_num:
        if x in Y:
            count = Y.count(x)
            count = count if count < x_num.get(x) else x_num.get(x)
            # print(count)
            for _ in range(0, count):
                max_num.append(x)

    # print(max_num)
    if not max_num:  # 존재하지 않으면 -1
        answer = '-1'
    elif max_num.count('0') == len(max_num):  # 0으로만 구성되어 있으면 0
        answer = '0'
    else:
        max_num = list(map(int, max_num))
        max_num.sort(reverse=True)
        # print(max_num)
        for m in max_num:
            answer += str(m)

    return answer