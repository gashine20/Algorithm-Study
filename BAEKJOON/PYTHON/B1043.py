# 거짓말 들은 파티원이 나중에 진실을 아는 파티원과 함께 파티에 나타날 수도 있음
# 이런 경우는?
# 2번 for문 하네

N, M = map(int, input().split())
people = [i for i in range(N + 1)]
party = [[] for _ in range(M)]

knowPeople = list(map(int, input().split()))
del knowPeople[0]

for i in range(len(knowPeople)):  # 진실을 아는 사람 하나의 부모 값으로 설정
    people[knowPeople[i]] = knowPeople[0]


def find(num):  # 대표 값이 누군지
    if people[num] != num:
        people[num] = find(people[num])
    return people[num]


def union(a, b):
    parent1 = find(a)
    parent2 = find(b)

    if parent1 != parent2:
        people[b] = parent1


def checkKnowPeople(a, b):
    parent1 = find(a)
    parent2 = find(b)

    if parent1 == parent2:
        return True
    else:
        return False


for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]

    firstPeople = party[i][0]  # 첫번째 파티원으로 union
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

answer = 0
for i in range(M):  # 거짓말할 수 있는 파티 개수 세기
    isLie = True
    firstPeople = party[i][0]

    for j in range(len(knowPeople)):  # 첫번째 파티원으로 다 union했는데,
        if checkKnowPeople(firstPeople, knowPeople[j]):  # 진실을 아는 사람의 대표값이 첫번째 파티원과 같으면
            isLie = False  # 거짓말을 할 수 없음
            break

    if isLie:
        answer += 1

print(answer)
