n = 7
member = [2, 5, 6, 13, 14, 16, 35]  # 답 [14, 2, 16, 6, 35, 5, 13]

remember = [[] for _ in range(n)]
answer = []
visited = [False] * n

member.sort()
for i in member:
    remain = i % n
    remember[remain].append(i)

print(remember)


# 그 자리에 부합하는 원소가 있는지 확인 - 1번 조건
def checkThere(index, answer):
    if len(remember[index]) == 0:  # ***
        print("index에 해당하는 원소 없음")
        return True
    for num in remember[index]:
        if answer[index] == num:  # index에 해당하는 원소라면
            print("1번 조건 충족 = index:", index, "num", num)
            return True

    print("1번 조건 충족X")
    return False


# 2번 조건 - 사전순으로 배치되어 있는지 확인하는.. .
def backtracking(depth, k, m):  # 깊이, 인덱스, m
    if depth == m and k == m - 1:  # 끝
        print("끝:", answer)

    print("depth:", depth, "k : ", k)
    if len(answer) > 1:
        if not checkThere(k - 1, answer):  # 이전 index 값이 1번 조건 충족하는지 체크
            return

    index = 0  # 어떤 원소 넣을 건지 저장
    if len(remember[k]) >= 1:
        for element in remember[k]:
            index = member.index(element)  # 방문 하지 않았으면
            if not visited[index]:
                answer.append(element)
                visited[index] = True
                break
        if len(answer) == depth:  # 다른 데에서 가져가 쓰면 ?
            print("다른 데에서 가져다 씀")
            return
        print("1 -", answer)
    else:
        for i in range(n):
            if not visited[i]:
                index = i
                answer.append(member[i])
                visited[index] = True
                break
        print("2 -", answer)

    # answer k번째가 정해진 후
    backtracking(depth + 1, k + 1, m)
    # 만약에 return 돼서 돌아 온다면 - 1번조건 만족하지 않은 거라
    answer.pop()
    visited[index] = False
    print("3 - ", answer)


backtracking(0, 0, n)
