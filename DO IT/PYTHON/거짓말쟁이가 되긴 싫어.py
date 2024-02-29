import sys

# 거짓말 - 1043
input = sys.stdin.readline

N, M = map(int, input().split())  # 사람의 수 N, 파티의 수 M
truth = list(map(int, input().split()))
del truth[0]

party = [] * M

parent = [0] * (N + 1)
for i in range(len(parent)):
    parent[i] = i


def find(a):
    if a == parent[a]:
        return a
    else:
        return find(parent[a])


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


def checkSame(a, b):
    if find(a) == find(b):
        return True
    return False


for _ in range(M):
    people = list(map(int, input().split()))
    del people[0]

    firstPeople = people[0]
    for p in people:
        if p in truth:
            union(firstPeople, p)
            # print(parent)

    party.append(people)

result = 0
for people in party:
    firstPeople = people[0]

    result += 1
    for t in truth:
        # print("p:", p, "parent:", parent[p])
        # print("result", result)
        if checkSame(firstPeople, t):
            result -= 1
            break

print(party)
print(parent)
print(result)

# result = 0
# for people in party:
#     firstPeople = people[0]
#     isPossible = True
#
#     for t in truth:
#         # print("p:", p, "parent:", parent[p])
#         # print("result", result)
#         if checkSame(firstPeople, t):
#             isPossible = False
#             break
#     if isPossible:
#         result += 1
#
# print(result)
