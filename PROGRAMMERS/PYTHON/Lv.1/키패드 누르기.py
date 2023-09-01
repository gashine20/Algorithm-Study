def solution(numbers, hand):
    answer = ''

    distance = {2: {0: 3, 1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2, 9: 3, '*': 4, '#': 4},
                5: {0: 2, 1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 1, 9: 2, '*': 3, '#': 3},
                8: {0: 1, 1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, '*': 2, '#': 2},
                0: {0: 0, 1: 4, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, '*': 1, '#': 1}}

    left = "*"
    right = '#'

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            left = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            right = num
            answer += 'R'
        else:
            left_distance = distance[num][left]
            right_distance = distance[num][right]
            print(left_distance, right_distance)

            if left_distance < right_distance:  # left
                left = num
                answer += 'L'
            elif left_distance == right_distance:  # 거리가 같으면
                if hand == "left":  # 왼손잡이이면
                    left = num
                    answer += 'L'
                else:
                    right = num
                    answer += 'R'
            else:
                right = num
                answer += 'R'

    return answer