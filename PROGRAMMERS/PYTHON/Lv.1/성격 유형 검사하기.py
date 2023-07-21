def solution(survey, choices):
    answer = ''
    # choices 1 2 3 4 5 6 7 선택지 = (비동의)3 2 1 0 1 2 3(동의)
    # "TR" : T 비동의, R 동의

    scores = [3, 2, 1, 0, 1, 2, 3]

    R = 0;
    T = 0;
    C = 0;
    F = 0;
    J = 0;
    M = 0;
    A = 0;
    N = 0

    for i in range(len(survey)):
        if survey[i] == 'RT':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                R = R + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                T = T + score
        if survey[i] == 'TR':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                T = T + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                R = R + score
        if survey[i] == 'CF':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                C = C + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                F = F + score
        if survey[i] == 'FC':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                F = F + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                C = C + score
        if survey[i] == 'JM':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                J = J + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                M = M + score
        if survey[i] == 'MJ':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                M = M + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                J = J + score
        if survey[i] == 'AN':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                A = A + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                N = N + score
        if survey[i] == 'NA':
            if choices[i] < 4:
                score = scores[choices[i] - 1]
                N = N + score
            elif choices[i] > 4:
                score = scores[choices[i] - 1]
                A = A + score

    if (R >= T):
        answer = answer + 'R';
    elif (R < T):
        answer = answer + 'T';
    if (C >= F):
        answer = answer + 'C';
    elif (C < F):
        answer = answer + 'F';
    if (J >= M):
        answer = answer + 'J';
    elif (J < M):
        answer = answer + 'M';
    if (A >= N):
        answer = answer + 'A';
    elif (A < N):
        answer = answer + 'N';

    return answer