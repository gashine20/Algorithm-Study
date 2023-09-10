def solution(answers):
    student = {1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = {1: 0, 2: 0, 3: 0}
    answer = []

    # 완전 탐색..
    person1 = []
    person2 = []
    person3 = []

    # answers 길이 만큼 student 찍는 번호 배열 다시 정의
    for i in range(len(answers)):
        person1.append(student[1][i % len(student[1])])
        person2.append(student[2][i % len(student[2])])
        person3.append(student[3][i % len(student[3])])

    # print(person1, person2, person3)

    # 정답 갯수 세기
    for i in range(len(answers)):
        if person1[i] == answers[i]:
            scores[1] += 1
        if person2[i] == answers[i]:
            scores[2] += 1
        if person3[i] == answers[i]:
            scores[3] += 1

    # 제일 큰 수 찾기
    max = 0

    # 다 같으면 넣고
    if scores[1] == scores[2] == scores[3]:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    else: # 제일 큰 수 찾아 넣기
        for i in range(1, 4):
            if scores[i] > max:
                max = scores[i]
        for i in range(1, 4): # 같으면 넣기
            if max <= scores[i]:
                answer.append(i)

    return answer